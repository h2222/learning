#! python
# coding = utf-8





import types


'''
python3.5 协程使用 yield from 来实现, 但是 yield from 即是生成器, 有是协程, 过于
复杂

在python3.5 引入了新的关键词字 async 和 await 专门用于定义协程, 用法与yield相同
'''
# 子生成器, 使用types.corountine 也可以达到async的效果
@types.coroutine
def downloader(url):
    yield "boddy"


# 定义协程
# await 代替yield from, async 表示该函数为协程
async def download_url(url):
    html = await downloader(url)


if __name__ == "__main__":
    # 普通的参数传入 url
    coro = download_url("http://www.baidu.com")

    # 预激协程
    coro.send(None)
    # 向协程发生数据(因为downloader内yield没有复制, 直接发送None, 转入return)
    coro.send(None)







