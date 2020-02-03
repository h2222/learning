#! python
# coding=utf-8
import os, sys
# 必须把根目录加载到sys path 中
# 本测试根路径是  
# /commen_learning, 所以 commen_learning 的路径如下, 加载到sys.path中 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from test_pkg_1 import (test1, test2, test3, test4)


test1()

test3()
