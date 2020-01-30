import pandas as pd
import numpy as np
print(pd.__version__)



# 列表
index = ['a', 'b', 'c' ,'d', 'e']
s = pd.Series([1,2,3,4,5], index=index)
print(s)


# 字典创建series
s2 = pd.Series({1:'a',2:'2'})
print(s2)


