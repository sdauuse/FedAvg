# author: miaoyin
# time: 2023-11-09 15:09
import time
import psutil
import os
import pygame
import cv2

if __name__ == '__main__':

    for i in range(10):
        start_time = time.time()

        # 执行一些操作

        time.sleep(1)
        end_time = time.time()
        time_diff = end_time - start_time

        print("时间差为：", time_diff, "秒")

        mem = psutil.virtual_memory()
        mem_utilization = mem.percent

        print("内存利用率：", mem_utilization, "%")

        # 初始化pygame
        pygame.init()
        # 加载音频文件
        pygame.mixer.music.load("file\streamFile2.mp3")
        # 播放音频文件
        pygame.mixer.music.play()
        # 获取Python程序的进程ID
        pid = os.getpid()
        # 实例化进程对象
        process = psutil.Process(pid)
        # 获取进程使用的内存，返回字节单位
        memory_usage = process.memory_info().rss
        # 将字节转换为兆字节
        memory_usage_mb = memory_usage / 1024 / 1024
        print("Python程序使用的内存为：", memory_usage_mb, "MB")
        # 等待播放结束
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            memory_usage = process.memory_info().rss
            # 转换为MB
            memory_usage_mb = memory_usage / 1024 / 1024
            # my memory capacity
            memory_total = 8 * 1024 * 1024 * 1024
            # 内存占用百分比
            memory_percentage = memory_usage / memory_total * 100
            print("memory cos", memory_usage_mb, "MB", "\t内存占用百分比",
                  "{:.2f}".format(memory_percentage), "%")

