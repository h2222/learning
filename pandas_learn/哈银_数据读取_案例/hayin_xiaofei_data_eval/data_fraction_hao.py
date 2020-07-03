#coding=utf-8

import pandas as pd
import sys
sys.path.append('.')
from m2.m2_dict import ai_map, in_dct, out_dct
import re


def split(path, ai_map=None, in_dict=None, out_dict=None):

    cols = ['通话状态', '通话记录id', '通话记录']

    df = pd.read_excel(path, sheet_name=0, usecols=cols, encoding='utf-8-sig').values
    all_data = list(df)
    all_data = [x for x in all_data if x[0] == '已接听' and isinstance(x[2], str) and len(x[2]) != 0 ]
    print(all_data[0])


    in_node = []
    type_robot = []
    me = []
    out_node = []
    type_user = []
    AI = []
    sidl = []


    for line in all_data:
        texts = line[2].split('\n')
        sid = str(line[1]).strip('')

        # 初始化index, count
        index = 0
        pre_ai, rear_ai = '', '' # in_node 和 out_node
        pre_ai_k, rear_ai_k = '*', '**'

        # 遍历文本: ai 和 me
        while index < len(texts): # texts length 为当前行ai和me对话总行数
            temp = texts[index]
            if not texts[index].startswith('ME'):
                if texts[index].startswith('AI'):
                    tt = texts[index]# ai 话术
                    for k in ai_map: 
                        if k in texts[index]: # 如果ai话术中存在key word, 将pre_ai对应key_word的意图, 将pre_ai_k对应key
                            pre_ai = ai_map[k]
                            pre_ai_k = k
                            break
                        pre_ai_k = '*'
                index += 1
                continue # 检索找到下一个ai
            
            save_me = []
            save_id = []
            save_innode = []
            save_outnode = []
            save_type_robot = []
            save_type_user = []
            while texts[index].startswith('ME'):
                # print('break')
                kk = texts[index] # 用户回复
                index_ai = index
                # 如果没到最后一个且开头不是AI(开始是ME)
                
                save_me += [texts[index_ai][3:]] # 收集区间内的用户回复([3:]的作用是去除ME)
                save_id += [sid]
                
                while index_ai < len(texts) and (not texts[index_ai].startswith('AI')):
                    index_ai += 1 #迭代
                
                # ME 回答之后, AI的回答
                if index_ai < len(texts) and texts[index_ai].startswith('AI'):
                    for k in ai_map:
                        # 远端AI类型判断
                        if k in texts[index_ai]:
                            rear_ai = ai_map[k]
                            rear_ai_k = k
                            break
                        rear_ai_k = '*' #远端AI无结果


                save_innode += [in_dict[pre_ai_k][0]]
                save_type_robot += [in_dict[pre_ai_k][1]]
                
                save_outnode += [out_dict[rear_ai_k][0]]
                save_type_user += [out_dict[rear_ai_k][1]]
                
                rear_ai_k = '**' # 重置
                index += 1 # index加1, 循环下一条AI或ME
            # 添加话术
            # session id
            sidl.append(sid)
            me.append(save_me)
            in_node.append(save_innode)
            type_robot.append(save_type_robot)
            out_node.append(save_outnode)
            type_user.append(save_type_user)
    
    result = {}
    print('*'*20)
    print(len(sidl))
    print(len(in_node))
    print(len(type_robot))
    print(len(out_node))
    print(len(type_user))
    print(len(me))
    print('*'*20)


    
    # df3=pd.DataFrame(columns=['session_id', 'in_node', 'type_robot', 'out_node', 'type_user','p1','p2','p3','p4','p5','p6','p7','p8','p9'])
    df3=pd.DataFrame(columns=['session_id', 'in_node', 'type_robot', 'out_node', 'type_user','msg'])
    df3['msg'] = ['' for i in range(len(df3))]
    i = 0
    for e, s, ino, ti, o, to in zip(me, sidl, in_node, type_robot, out_node, type_user):
        temp = {}
        # temp = df2.iloc[i]
        temp['msg'] = ''
        temp['session_id'] = s
        temp['in_node'] = ino[0]
        temp['type_robot'] = ti[0]
        temp['out_node'] = o[0]
        temp['type_user'] = to[0]
        for j in range(9):

            print(i)
            try:
                msg = ''.join([ch for ch in e[j] if ('\u4e00' <= ch <= '\u9fa5')])
                temp['msg'] += msg+'|'
            except:
                temp['msg'] += ''
        i += 1
        # print(temp)
        df3 = df3.append(temp,ignore_index=True)



    target = ['1.1', '2.1', '2.2', '3.2', '3.4', '4.1', '4.3']
    df3 = df3.loc[df3['in_node'].isin(target)]

    print(df3)

    df3.to_csv('./m2/resulttt_m2.csv', index=False, encoding='utf-8-sig')







if __name__ == "__main__":
    path='./m2/m2_1000.xlsx'
    split(path, ai_map, in_dct, out_dct)