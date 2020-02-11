#! python
# coding = utf-8


'''
python 的自省机制(利用__dict__函数遍历对象的属性)

理解dir(a) 方法
'''




class Student:
    school = 'high school'

    def __init__(self):
        self.name = 'hao'


if __name__ == "__main__":
    s1 = Student()


    # 利用__dict__返回类实例化对象的属性字典(key:属性名称, value:值)
    print(s1.__dict__)

    # 可以通过自省机制修改对象的属性
    d = {'age':18, 'school':'high school', 'gender':'male'}
    for j,k in d.items():
        s1.__dict__[j] = k
    print(s1.__dict__)


    # 类对象的自省机制, 同样会打印类变量键值对
    print(Student.__dict__, '\n')


    # dir方法, python 万物皆对象
    # 列举出当前类对象的所有属性(变量, 函数, ..)
    a = 'a'
    b = 1
    c = [1, 2]
    print(dir(c))
