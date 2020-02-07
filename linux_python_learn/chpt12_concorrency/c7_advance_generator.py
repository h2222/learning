#! python
#coding=utf-8


'''
生成器高级特性, yield 赋值, close 关闭生成器, throw

'''

def gen_1():
    yield 1
    yield 2
    yield 3

    return 'end'




def gen():

    # yield赋值: 
    # 左边为从外部调用传进来的html值
    # 右边为本次yield返回的 url值
    html = yield 'http://projects.com'

    # 验证参数是否传递成功
    print('外部调用传入的html:', html)
    
    yield 2
    return 'end'



def gen_2():

    # throws 方法需要自己定义异常
    try:
        yield 2
    except Exception as e:
        pass


    yield 3
    return 'end'


if __name__ == "__main__":
    g1 = gen()

    # next(g1)的作用是首先进入生成器, 拿到生成器返回的结果,即url
    # 或者也可以使用g1.send(None)来启动生成器
    url = next(g1)

    html = 'bobby'
    # 然后如果在本轮yield中需要参数出传递, 使用send方式发送
    # 同时如果你打印 print(g2.send(html)) 会得到2, 说明send方法不仅可以传递参数, 
    # 同时还可以启动生成器让其继续迭代
    g1.send(html)
    print('从生成器返回的url:', url)


    # print(next(g1))
    # print(next(g1))
    # print(next(g1))


    # 测试生成器 close方法
    g2 = gen_2()
    print(next(g2))
    g2.close()


    # 测试 throws
    g3 = gen_2()
    print(next(g3))
    print(g3.throw(Exception, "my error"))
    print(next(g3))



    