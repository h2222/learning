# coding=utf-8

import pandas as pd



def fit(path, path2):
    
    origin = pd.read_csv(path, encoding='utf-8-sig')
    hand = pd.read_excel(path2, sheet_name=0, encoding='utf-8-sig')

    origin.loc[origin['in_node'] == origin['out_node'], 'type_user'] = '无效语义'
    origin['type_handle'] = ['*' for i in range(len(origin))]

    for i, x in hand.iterrows():
        print(i)
        sid = int(x['session_id'])
        in_node = x['in_node']
        msg = x['msg']
        handle = x['type_handle']
    
        # 根据session id 查找对应的idx1
        indicate = origin.loc[origin['session_id']==sid]
        # print(indicate)

        idx1 = indicate.index
        indicate2 = origin.loc[idx1].loc[origin['in_node'] == in_node]

        # print(indicate2)
        # 根据idx1 和 in_node 查找对应的idx2
        idx2 = indicate2.index
        # print(origin.loc[idx2, 'msg'])
        idx3 = origin.loc[idx2].loc[origin['msg'].str.contains(msg)].index            

        # 如果type_handle 是空值， 或者是无效语义, 设置type_handle, 如果不是, 直接跳过
        # 根据 idx3 查找并， 设定对应的 type_handle值
        if origin.loc[idx3, 'type_handle'].tolist()[0] in ['', '*', '无效语义']:
            origin.loc[idx3, 'type_handle'] = [handle for i in range(len(idx3))]

    return origin    




def eval(df=None, if_csv=False, save_p=''):
    
    df = df.dropna(subset=['type_handle'])
    df = df.loc[df['type_handle'] != '*']
    total = len(df)

    error = df.loc[df['type_user'] != df['type_handle']]
    error = len(error)

    e_rate = error/total
    r_rate = 1 - e_rate
    print(r_rate)
    
    if if_csv:
        df.to_csv(save_p, index=False, encoding='utf-8-sig')



# 去重标注数据 -> 未去重未标注数据
def mapping(path, path2):
    target = pd.read_excel(path, sheet_name=0, encoding='utf-8-sig' )
    label = pd.read_excel(path2, sheet_name=0, encoding='utf-8-sig')


    for i, l in label.iterrows():
        print(i)
        sid = l['session_id']
        in_node = l['in_node']
        msg = l['msg']
        handle = l['type_handle']

        first = target.loc[target['session_id'] == sid].index
        second = target.loc[first].loc[target['in_node'] == in_node].index
        final = target.loc[second].loc[target['msg'] == msg].index

        target.loc[final, 'type_handle'] = handle

    target.to_excel('./m1/hayinm1_nodel_tag_biaozhu.xlsx', encoding='utf-8-sig')

        




if __name__ == "__main__":
    
    # 评估文件
    path = './m2/eval_m2.csv'
    
    # 拼接文件
    path_del_tag = './m2/hayinm2_tag_biaozhu.xlsx'
    
    # 未去重复文件和未去重拼接文件
    # path_nodel = './m1/hayinm1_nodel_tag.xlsx'
    path_nodel_tag ='./m2/m2_tag_biaozhu_nodel.xlsx' 

    origin = fit(path, path_nodel_tag) 
    eval(origin, if_csv=True, save_p='./m2/eval_nodel_result.csv')
    # mapping(path_nodel, path2)
