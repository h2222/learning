# coding=utf-8
import os
import re
import pandas as pd
import tensorflow as tf

from tqdm import tqdm


#%% 
## loading data functions
def load_data(path):
    data = {}
    data['sentence'] = []
    data['sentiment'] = []
    for fp in tqdm(os.listdir(path)):
        with tf.gfile.GFile(os.path.join(path, fp), 'r') as f:
            data['sentence'].append(f.read())
            data['sentiment'].append(re.match('\d+_(\d+)\.txt', fp).group(1))
    
    return pd.DataFrame.from_dict(data)


def load_dataset(path):
    pos_df = load_data(os.path.join(path, 'pos'))
    neg_df = load_data(os.path.join(path, 'neg'))
    pos_df['polarity'] = 1
    neg_df['polarity'] = 0
    return  pd.concat([pos_df, neg_df])\
              .sample(frac=1)\
              .reset_index(drop=True)


def download_and_load_datasets(download=False):
    print('### Loading dataset ###')
    if download:
        dataset = tf.keras.utils.get_file(fname='aclImdb.tar.gz',
                                          origin='http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
                                          cache_dir='D:\\Python\\jiaxiang_1\\estimator\\data',
                                          extract=True)
    else:
        dataset = 'D:\\Python\\jiaxiang_1\\estimator\\data\\datasets\\aclImdb.tar.gz'
    print(dataset)
    print(os.path.dirname(dataset))

    train_df = load_dataset(os.path.join(os.path.dirname(dataset), 'aclImdb', 'train'))
    test_df = load_dataset(os.path.join(os.path.dirname(dataset), 'aclImdb', 'test'))

    return train_df, test_df


#%%
## creating model

def create_model(features, 
                 vocab_size,
                 embedding_size,
                 drop_out,
                 output_cls,
                 max_seq_len):
    
    if isinstance(features, dict):
        features = features['text']
    
    #### 建立 vocab list ####
    vocab = tf.contrib.lookup.index_table_from_file(vocabulary_file='data/dataset/aclImdb/imdb.vocab',
                                                    default_value=0)
    # 从 vocab list 中获取text的index
    tokens = vocab.lookup(features)
    # 从 embedding table 中获取embedding vector
    table = tf.get_variable(name='embedding', 
                            shape=[vocab_size, embedding_size], 
                            dtype=tf.float32)
    
    lstm_input = tf.nn.embedding_lookup(table,
                                        tokens,
                                        name='embedding_layer')

    #### 定义:bi-lstm网络 ####
    lstm = tf.keras.layers.LSTM(units=embedding_size,
                                dropout=drop_out,
                                return_sequences=False) # 分类任务, 只返回最后一个时刻的状态输出, 不需要返回sequence的输出
    bi_lstm = tf.keras.layers.Bidirectional(lstm,
                                            merge_mode='concat',
                                            name='bi_lstm')
    # 前馈神经网络 1 层, 中间接relu作为activation
    dense_1 = tf.keras.layers.Dense(units=embedding_size,
                                    activation='relu',
                                    name='dense')
    dense_2 = tf.keras.layers.Dense(units=output_cls,
                                    name='output_layer')
    # dropout
    dropout = tf.keras.layers.Dropout(rate=drop_out,
                                      name='dropout')
    
    #### 构建bi-lstm 网络 ####
    dense1_input = bi_lstm(lstm_input)
    dense2_input = dense_1(dense1_input)
    dense2_intput_drop = dropout(dense2_input)
    logtis = dense_2(dense2_intput_drop)

    return logtis


#%%
def model_fn_builder(lr, threshold):
    """
    该方法用于创建 estimator中的model_fn
    """

    def model_fn(features, labels, mode, params, config):
        '''
        features: input_fn 的返回值, 切记返回顺序
        labels:   input_fn 的返回值, 切记返回顺序
        mode:     TRAIN, TEST, EVAL
        params:   初始化estimator时, 传入的参数列表, dict类型
        config:   初始化estimator时的 Runconfig
        '''

        # 训练过程
        # 如果mode 为 EVAL 或 TRAIN
        if not (mode == tf.estimator.ModeKeys.PREDICT):
            labels = tf.reshape(labels, [-1, 1]) #labels压缩为1维
            logits = create_model(features=features,
                                  vocab_size=params['vocab_size'],
                                  embedding_size=params['embedding_size'],
                                  drop_out=params['drop_out'],
                                  output_cls=params['output_cls'],
                                  max_seq_len=params['max_seq_len'])
            # 2分类pos/neg,  sigmoid
            pre_prob  = tf.nn.sigmoid(logits)            

            # 根据threshold极化pre_prob
            # where 函数, (判断, 情况1, 清空2)
            pre_cls = tf.where(pre_prob<threshold, 
                               tf.zeros_like(pre_prob), 
                               tf.ones_like(pre_prob))        

            # logging
            tf.logging.info('label shape:'+str(labels.shape))
            tf.logging.info('logits shape:'+str(logits.shape))
            tf.logging.info('cls_prob shape:'+str(pre_prob.shape))

        # 梯度优化
        if not (mode == tf.estimator.ModeKeys.PREDICT):
            loss = tf.losses.sigmoid_cross_entropy(labels, logits=logits)

            # 定义评估函数(未完成)
            def metric_fn(label, predictions):
                '''
                define metrics
                '''

                # (TP+TN) / (TP+FP+TN+FN)
                accuracy, accuracy_update = tf.metrics.accuracy(labels=label, 
                                                               predictions=predictions,
                                                               name='text_accuracy')
                # TP / TP+FN
                recall, recall_update = tf.metrics.recall(labels=labels,
                                                          predictions=predictions,
                                                          name='text_recall')

                # TP / TP+FP
                precision, precision_update = tf.metrics.precision(labels=labels,
                                                                   predictions=predictions,
                                                                   name='text_precision')

                return{'accuracy':(accuracy, accuracy_update),
                        'recall':(recall, recall_update),
                        'precision':(precision, precision_update)}
                
            if mode == tf.estimator.ModeKeys.EVAL:
                # 验证用 estimator 对象
                return tf.estimator.EstimatorSpec(mode=mode,
                                                  loss=loss,
                                                  eval_metric_ops=metric_fn(labels,pre_cls))
            
            train_op = tf.train.AdamOptimizer(learning_rate=lr).minimize(loss=loss,
                                                                         global_step=tf.train.get_global_step())

            # 测试用 estimator 对象
            return tf.estimator.EstimatorSpec(mode=mode,
                                              loss=loss,
                                              train_op=train_op,
                                              eval_metric_ops=metric_fn(labels, pre_cls))
        
        # 如果 mode == PREDICT
        elif mode == tf.estimator.ModeKeys.PREDICT:
            # tf.identity: Return a Tensor with the same shape and contents as input.
            # 算预测概率
            neg = tf.identity(input=1-pre_prob)
            prob = tf.where(pre_prob<threshold,
                            neg,
                            pre_prob)
            
            predictions = {'predict_cls':pre_cls, 'predict_prob':prob}

            return tf.estimator.EstimatorSpec(mode=mode,
                                              predictions=predictions)

    # 返回model_fn函数
    return model_fn
#%%
def input_fn_builder(input_x,
                     input_y,
                     batch_size,
                     epochs,
                     max_seq_len,
                     is_train=True):
    """
    创建输入闭包和函数
    """
    def pad_or_trunc(tensor):
        lens = tf.size(tensor)
        # tf.cond(Args, true_fn, false_fn) 判断, true返回, false返回
        # tf.cond 和 tf.where 用法相同, 都是判断并返回
        # 但 tf.cond 返回的是函数 例如 true_fn=lambda:t+1
        # 而 tf.where 直接回返回数值, 例如 x = t+1
        return tf.cond(pred = tf.equal(lens, max_seq_len), 
                       true_fn=lambda:tensor,
                       false_fn=lambda:tf.cond(
                           pred=tf.greater(lens, max_seq_len),
                           # 需要处理的tensor为input_, 从[0]维度开始, size每个维度取多少值, 即第0维度取 max_seq_le个值  
                           # tf.slice(input_=输入张量, begin=[维度1起点, 维度2起点, 维度3起点, ..], size=[维度1终点, 唯独2终点, 维度3终点, ...])
                           true_fn=lambda:tf.slice(input_=tensor, begin=[0], size=[max_seq_len]),
                           # tf.fill(dim, value, name='default')  填充, 创造 [dim维度的] 一个 xxx 填充的张量
                           false_fn=lambda:tf.concat([tensor, tf.fill([max_seq_len - lens], 'UNK')], 0)))


    def token(d, y):
        word = tf.string_split([d['text']])
        tokens = tf.sparse_tensor_to_dense(word, default_value='UNK')
        # tf.reshape(tensor, shape, name=None), 当shape 等于[-1] 将所有维度压缩到维度1,  但不知道所有维度压缩值为多少, 所有填-1自动处理
        tokens_with_pad = pad_or_trunc(tf.reshape(tokens, [-1]))

        # logging
        tf.logging.info('tokens 0 is type: '+str(type(tokens)))
        tf.logging.info('pad shape is: '+str(type(tokens_with_pad)))

        return {'text':tokens_with_pad}, y


    def input_fn():
        # logging
        tf.logging.info('call input_fn')
        # dataset 对象(features, labels)
        # 其中 features为字典, label 为具体的labels
        dataset = tf.data.Dataset.from_tensor_slices(({'text':input_x}, input_y))

        if is_train:
            dataset = dataset.shuffle(1000)\
                      .repeat(epochs)\
                      .map(token)\
                      .batch(batch_size)
        
        # 返回的顺序必须与mode_fn已知, 或者dataset的元素的格式为(features, labels)
        return dataset

    return input_fn
#%%
def serving_input_receiver_fn():
    """
    该函数用模型服务, 为tf_serving提供必要的pb文件
    """
    def pad_or_trunc(tensor):
        lens = tf.size(tensor)
        return tf.cond(pred = tf.equal(lens, max_seq_len), 
                       true_fn=lambda:tensor,
                       false_fn=lambda:tf.cond(
                           pred=tf.greater(lens, max_seq_len),
                           true_fn=lambda:tf.slice(input_=tensor, begin=[0], size=[max_seq_len]),
                           false_fn=lambda:tf.concat([tensor, tf.fill([max_seq_len - lens], 'UNK')], 0)))
    

    def process(text):
        """
        splite, padding and truncate
        """
        # tf.string_split 将list中的string,按照空格分分开, 
        # (默认生成稀疏矩阵, 也就说如string间如果维度不同也没关系),
        # 例如: text = ['hello world', 'a b c']
        # output_tensor  = [['hello', 'world', x], ['a', 'b', 'c']]
        # indice指有值的引索, 即[0,0] [0,1] [1,0] [1,1] [1,2]
        # output_tensor 的shape 为 (2, 3)
        words = tf.string_split([text])
        #tf.sparse_tensor_to_dense 作用是让稀疏矩阵变为dense, 使用default_value填充
        # 例如上面的例子填充后变为: [['hello', 'world', 'UNK'], ['a', 'b', 'c']]
        token = tf.sparse_tensor_to_dense(words, default_value='UNK')
        token_with_pad = pad_or_trunc(tf.reshape(tokens, [-1]))
        return token_with_pad
    
    
    input_ph = tf.placeholder(tf.string, shape=[None], name='texts')
    text_tensor = tf.map_fn(fn=process,
                            elems=input_ph,
                            back_prop=False,
                            dtype=tf.string) # 返回类型,
    
    # 输入返回类型
    # features 为输入类型tensor, dict
    # receiver_tensor 为接收tensor
    features = {'features':text_tensor}
    receiver_tensor={'text':input_ph}   

    # 返回estimator 模型服务
    return tf.estimator.export.ServingInputReceiver(features, receiver_tensor) 
#%%

def train_process(train, test):
    """
    train: dataFrame
    test: dataFrame
    """
    model_dir = r'D:\\Python\\estimator\\jiaxiang_1\\estimator\\model'
    params = {}
    params['epochs'] = 10
    params['batch_size'] = 128
    params['output_cls'] = 1
    params['vocab_size'] = 8000
    params['embedding_size'] = 50
    params['drop_out'] = 0.5
    params['max_seq_len'] = 128
    
    # 1. config (用于模型一些初始设置, 例如ckpt保存方案, summary保存方案, )
    config = tf.estimator.RunConfig(save_checkpoints_steps=100)
    # 2. Estimator 创建
    estimator = tf.estimator.Estimator(model_fn=model_fn_builder(lr=0.01, threshold=0.5),
                                       model_dir=model_dir,
                                       params=params,
                                       config=config)
    
    # 3. training
    train_result = estimator.train(input_fn=input_fn_builder(input_x=train['sentence'], 
                                                             input_y=test['polarity'],
                                                             batch_size=params['batch_size'],
                                                             epochs=params['epochs'],
                                                             max_seq_len=params['max_seq_len'],
                                                             is_train=True), steps=10000)
    
    # 4. evaluating
    eval_result = estimator.evaluate(input_fn=input_fn_builder(input_x=test['sentence'],
                                                               input_y=test['polarity'],
                                                               batch_size=params['batch_size'],
                                                               epochs=params['epochs'],
                                                               max_seq_len=params['max_seq_len'],
                                                               is_train=False), steps=10000)

    # saving model
    estimator.export_savedmodel(export_dir_base='export_base/text', 
                                serving_input_receiver_fn=serving_input_receiver_fn)         





#%%
if __name__ == "__main__":
    train, test = download_and_load_datasets(download=False)
    train_process(train, test)