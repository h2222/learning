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



