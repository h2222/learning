#! python
#coding=utf-8

import aiohttp, asyncio
import time
 
#使用示例, 进行一次请求    
# async def main():#aiohttp必须放在异步函数中使用
#     async with aiohttp.request('GET', 'https://api.github.com/events') as resp:
#         text = await resp.text(encoding='utf-8')
#         print(text)
 

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.github.com/events') as resp:
#              print(await resp.text(encoding='utf-8'))
            


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


 
async def main(pool):#启动
    sem = asyncio.Semaphore(pool)
    async with aiohttp.ClientSession() as session:#给所有的请求，创建同一个session
        tasks = []
        [tasks.append(control_sem(sem, 'https://api.github.com/events?a={}'.format(i), session)) for i in range(10)]#十次请求
        await asyncio.wait(tasks)
 
async def control_sem(sem, url, session):#限制信号量
    async with sem:
        await fetch(url, session)
 
async def fetch(url, session):#开启异步请求
    async with session.get(url) as resp:
        json = await resp.json()
        print(json)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main(pool=2))