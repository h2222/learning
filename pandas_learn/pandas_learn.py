#! python
# coding = utf-8


import pandas as pd
import numpy as np
import random
print(pd.__version__)



# 列表
index = ['a', 'b', 'c' ,'d', 'e']
s = pd.Series([1,2,3,4,5], index=index)
print('列表',s)


# 字典创建series
s2 = pd.Series({1:'a',2:'2'})
print('从字典创建列表', s2)


# 修改Series的 index
s.index = ['A', 'B', 'C', 'D', 'E']
print(s.index)


# 横向拼接
print('横向拼接', s.append(s2))



# 指定索引值drop
print('删除E', s.drop('E'))

# 修改指定元素
s['E'] = '4e'
print('s, index-E, 修改为 4e:', s)



# DataFrame values, index, columns
df = pd.DataFrame(data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        )

print(df)



# values, index, columns
print(df.values)
print(df.index)
print(df.columns)



# 切片操作, 针对于查询行
print(df[1:3])


# 映射操作, 对应列
print(df['age'])
print(df[['age', 'priority']])
# 第 age 和 priority 列, 1, 2, 行
print(df[['age', 'priority']][1:3])


# 拷贝
dfc = df.copy()
# 深拷贝
print(id(dfc) == id(df))


# 添加一列新数据
dfc['new'] = pd.Series([random.randint(1, 10) for i in range(len(df))])
print(dfc)


# 取2到5行
print(dfc.loc[2:5])

# 取第3列
print(dfc.iloc[:, 3])

# 取age列
print(dfc.loc[:, 'age'])


# 取多列
print(df[['age', 'name']])


# 判断空值, 非空返回False, null 返回 True
print(dfc.isnull(), dfc['age'].isnull())

# 根据一个值修改另外一个值
dfc.loc[dfc['age'] > 2, 'prority'] = 'mt2'
print(dfc)


# 拿到一个特殊值的index
index = dfc.loc[dfc['age']>2].index
print(dfc.loc[index])


# 拿到特殊值的idnex并数一下某一列的元素
print(dfc.loc[dfc['age']>2]['age'].value_counts())


# 交换行位置
df.insert(loc=0, column='age' ,value=df.pop('age'))

print(df)


# 循环每一行
for i, info in df.iterrows():
    print(i, info)


# 重新设置 index
df.reset_index()

# 重新设置 name
df = df.rename(columns ={'age':'AGE'})
print(df)


# 划分数据集
# from sklearn.model_select import train_test_split
# x_train, x_test, y_train，y_test = train_test_split(x, y, test_size=0.25, ramdon_state=0)

train_set = df.sample(frac=0.8, random_state=0, axis=0)
print(train_set)
test_set = df.loc[~df.index.isin(train_set.index)]
print(test_set)





## 在xxx里, 或有xxx

# 如果 df 的 out_nodes列中, 有元素在 ['z', 'm'] 中, 则将type改为3
df.loc[df['out_node'].isin(['z', 'm']), 'type'] = 3

# 如果 df 的 out_node列中, 有元素包含 z或m,  例如 'zhang' 中包含'z', 则将type改为3
df.loc[df['out_node'].str.contains('z|m'), 'type'] = 3

# 可以利用求反进行, 反选
df.loc[~df['out_node'].str.contains('z|m'), 'type'] = 1



# 将 表groupby 并且 将 没有group的column做成list

df1 = df.groupby('a')['b'].apply(list).reset_index(name='new')

"""
In [1]: df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6]})
        df

Out[1]: 
   a  b
0  A  1
1  A  2
2  B  5
3  B  5
4  B  4
5  C  6

In [2]: df.groupby('a')['b'].apply(list)
Out[2]: 
a
A       [1, 2]
B    [5, 5, 4]
C          [6]
Name: b, dtype: object

In [3]: df1 = df.groupby('a')['b'].apply(list).reset_index(name='new')
        df1
Out[3]: 
   a        new
0  A     [1, 2]
1  B  [5, 5, 4]
2  C        [6]
"""






