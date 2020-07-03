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
    tokens = table.lookup(features)
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

    def model_fn(features, labels, mode, params, confing):
        '''
        features: input_fn 的返回值, 切记返回顺序
        labels:   input_fn 的返回值, 切记返回顺序
        mode:     TRAIN, TEST, EVAL
        params:   初始化estimator时, 传入的参数列表, dict类型
        config:   初始化estimator时的 Runconfig
        '''

        # 训练过程
        if not (mode == tf.estimator.ModeKeys.PREDICT):
            labels = tf.reshape(lables, [-1, 1]) #labels压缩为1维
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
            tf.logging.info('cls_prob shape:'+str(cls_prob.shape))

        # 梯度优化
        if not (mode == tf.estimator.ModeKeys.PREDICT):
            loss = tf.losses.sigmoid_cross_entropy(labels, logits=logits)

            # 定义评估函数(未完成)
            def metric_fn(label, )



#%%
if __name__ == "__main__":
    download_and_load_datasets(download=False)