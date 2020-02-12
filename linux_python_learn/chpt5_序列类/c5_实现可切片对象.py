#! python
# coding = utf-8

'''
通过协议(实现特定魔法函数), 将普通类转换为可切片对象
'''



class Group:
    def __init__(self, name, company, group_numbers):
        self.name = name
        self.company = company
        self.group_numbers = group_numbers
    
    '''
    通过实现 reversed, getitem, len, iter, contains等魔法函数, 
    实现类实例化对象的可切片性

    reversed 翻转, 实现后可调用 reversed()函数
    getitem 返回可切片对象, 对象的可切片性主要通过该函数实现
    len 长度, 实现后可调用len()函数
    iter 迭代, 实现后可调用迭代器
    contains 容器, 实现后 可使用 in 关键句判断 某元素是否在 对象内
    '''

    def __reversed__(self):
        self.group_numbers.reverse()

    def __getitem__(self, item):
        # 本类主要希望切片对象内的group_numbers变量
        # 所以必须要保证group_numbers变量为可切片类型
        # 首先通过type拿实例化对象的类型
        cls = type(self)

        # 然后, 通过isinstance函数判断item是否为可切片类型
        # 如果可以拿到item
        if isinstance(item, slice):
            return cls(self.name, self.company, self.group_numbers[item])
        # 如果不是, 把group_numbers变成list(可切片)
        elif isinstance(item, str):
            return cls(self.name, self.company, [self.group_numbers[item]])

    def __len__(self):
        return len(self.group_numbers)

    def __iter__(self):
        return iter(self.group_numbers)

    # 如果item in group_numbers 返回True else False
    def __contains__(self, item):
        if item in self.group_numbers:
            return True
        else:
            return False

if __name__ == "__main__":
    g1 = Group('hao', 'bairong', ['hao', 'fangshu', 'siru'])

    # 测试 contains
    if 'hao' in g1:
        print('true')
    else:
        print('false')

    # 测试 for
    for x in g1:
        print(x, '\n')

    # 测试 len
    print(len(g1), '\n')


    # 测试reverse
    print(reversed(g1), '\n')