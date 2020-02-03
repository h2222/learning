#! python
# coding=utf-8

import os, sys
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# 只有将 common_learning 这个包加入到 sys path, 中 我们才能引用 commen_learning 这个包
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(BASE_DIR)


from test_pkg_1 import (test1, test2, test3, test4)

# 其中 test1(), test2()来自于 __init__.py 模组, 说明在引用 common_learning 包时, 模组会首先编译 __init__.py, 然后才编译 commen_learning 下的其他模组
# test3() test4() 来组与 commen_learning 下的 os_path_test_2_1.py模组, 当在当前py文件下引用 test3() 或 test4 时, 系统首先回去 __init__.py找
# 看是否引用了 os_path_2_1.py 模组, 如果引用了, 那就返回加载结果, 起始 test3 和 test4 是我们日常最常用的其他模组引用,  
test1()
test2()
test3()
test4()


# 获取当前文件的绝对路径, 主要是文件的绝对路径
# __file__ 指的就是当前正在编译的文件
print('当前文件绝对路径'+os.path.abspath(__file__))
# 获取当前文件的 dir 路径
print('获取前文件的路径dir路径'+os.path.dirname(os.path.abspath((__file__))))


# test3 打印系统环境变量
print(sys.path)


# 遍历文件 迭代器 返回元组 ('top',['dir1', 'dir2'], ['file1', 'file2'] ) 
# top 为当前正在文件夹本身的路径, 
# [dirs] 为该文件夹下的文件夹
# [files] 为该文件夹下的文件
# os.walk 会遍历该文件夹下的所有文件
print([i for i in (os.walk('../'))])