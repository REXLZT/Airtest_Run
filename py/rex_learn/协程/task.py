import time
import asyncio
 
 
async def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print("OK {}".format(url))
 
 
async def main(urls):
#    tasks = [asyncio.create_task(crawl_page(url) for url in urls)]
#看起来你的代码片段中有一个错误。这个错误与异步编程有关，特别是在创建任务时使用了生成器表达式。
#在你的代码中，你试图使用生成器表达式来创建任务，但是asyncio.create_task期望一个协程对象，而不是一个生成器。
#你可以尝试将生成器表达式更改为列表推导式，以便为每个URL创建一个任务。以下是一个可能的修正：
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#这样，tasks列表将包含每个URL的任务对象，然后你可以使用await asyncio.gather(*tasks)来等待所有任务完成。

#这个修改应该可以解决你遇到的RuntimeError。
    await asyncio.gather(*tasks)
 
 
# 开始计时
start = time.perf_counter()
# Python 3.7+
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end = time.perf_counter()
print("took {} s".format(end - start))