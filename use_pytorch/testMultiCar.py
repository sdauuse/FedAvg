# author: miaoyin
# time: 2023-11-14 14:38
# 多线程模拟RSU背景任务
from threading import Thread
import time

possion = [1, 3, 2, 2, 3, 2, 3, 3, 3, 1, 2, 6, 5, 2, 4, 4, 2, 1, 4, 2, 6, 1, 4, 2, 2, 6, 3, 3, 4, 4, 2, 5, 4, 2, 5,
           3, 3, 3, 0, 3, 3, 2, 5, 3, 6, 4, 5, 0, 3, 3, 5, 6, 5, 4, 5, 2, 1, 3, 3, 4, 3, 5, 4, 1, 3, 4, 3, 2, 2, 3,
           2, 1, 4, 6, 0, 3, 6, 7, 4, 4, 1, 9, 2, 1, 1, 4, 2, 2, 3, 7, 5, 0, 4, 4, 0, 1, 4, 3, 3, 3]


# 自定义线程函数
def target(name, it):
    print("第", it, "轮,hello", name)


num = 1
for i in possion:
    for j in range(i):
        # 创建线程01，不指定参数
        # thread_01 = Thread(target=target)
        # 启动线程01
        # thread_01.start()

        # 创建线程02，指定参数，注意逗号
        thread_02 = Thread(target=target, args=("Car" + str(j), num))
        # 启动线程02
        thread_02.start()

    num = num + 1
    time.sleep(3)
