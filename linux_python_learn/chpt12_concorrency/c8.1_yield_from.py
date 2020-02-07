#! python
# coding = utf-8




'''
yield from 后接 iterable 对象
意为 直接将 返回 iterable对象的中的元素 返回出来
'''

def test_yield():
    yield range(0,10)
    return 'end'

def test_yield_from():
    yield from range(0, 10)
    return 'end'

# yield 返回了 range(0, 10)
print(next(test_yield()))

# 可以看到 yield from 函数直接返回了 list中的值
g1 = test_yield_from()
print([x for x in g1])


'''
yield from 在协程中的应用

首先明确三个概念: 1.main 调用方, 2. g1 委托方生成器 3. gen 子生成器
yield from 可以在 调用方(main) 和 子生成器(gen) 建立通道联系

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(value)

按照常规的理解, g send会将value发送给 yield 传入的值, 例如 s = yield
但在yield from, g send 会将 value发送给 yield from 后的 gen 生成器(子生成器)
所以说, yield from 在 调用方(mian) 和 子生成器(gen)建立的连接




货物统计实例

说明: 现有 a 个不同种类的货品, 每个货品在不同的商店的销量
以list的是形式表现, 主要不是每一个商量都销售所以a类商品, list的值代表该货品在
该商店的销量

需求: 统计出每件商品在所有商店的总销量, 使用yield from

实现, 本人任务中:
    处理计算总销量的函数为sales_sum为子生成器
    middle 为连接调用方和子生成器的 委托生成器(yield from 实现)
    mian函数为 调用方

'''

final_result = {}


def sales_sum(key):
    total = 0
    nums = []
    while True:
        # 接受来自 value-> main(send) -> middle(yield from) -> x(一个值!)
        x = yield

        # x 不是空(说明list里还有x), 加和, 统计商店销量
        if not x:
            break
        total += x
        nums.append(x)
    
    # 当 send(None)信号时
    return total, nums



def middle(key):
    while True:
        # 将商品名称传入子生成器做处理, 将结果返回添加至 final_result[key]
        # 注意 key 只是普通的参数传递, 而生成器之间的参数传递是通过send完成的
        # 本实现中, value, 即销量list, 是通过send的方舒传入sales_sum中的
        final_result[key] = yield from sales_sum(key)
        print(key+"销量统计完成!")


def main():
    # 货品:[每个商店的销量], 可以看到list的动态数据, 不是写死的
    data_set = {"货品A":[100, 200, 150],
                "货品B":[50, 20, 100, 130],
                "货品C":[120, 20],
                "货品D":[120, 150, 160]}

    for key, data_set in data_set.items():
        print("货物为:", key)
        m = middle(key)
        m.send(None) # 预激 middle 协程, 启动生成器
        for value in data_set:
            # value 为每一个商品的在list中的销量(一个值), 给协程传递每一组的值
            # 在协程middle中, 因为 yield from的缘故, value会被发送给子生成器
            m.send(value) 
        m.send(None)# 发送None信号, 子生成器转为 return 返回
    
    print("final_resul:", final_result)


# 测试 
main()




