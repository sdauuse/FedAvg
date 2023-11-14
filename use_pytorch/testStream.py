# author: miaoyin
# time: 2023-11-10 16:50
import time
import psutil
import os
import cv2

if __name__ == '__main__':
    possion = [1, 3, 2, 2, 3, 2, 3, 3, 3, 1, 2, 6, 5, 2, 4, 4, 2, 1, 4, 2, 6, 1, 4, 2, 2, 6, 3, 3, 4, 4, 2, 5, 4, 2, 5,
               3, 3, 3, 0, 3, 3, 2, 5, 3, 6, 4, 5, 0, 3, 3, 5, 6, 5, 4, 5, 2, 1, 3, 3, 4, 3, 5, 4, 1, 3, 4, 3, 2, 2, 3,
               2, 1, 4, 6, 0, 3, 6, 7, 4, 4, 1, 9, 2, 1, 1, 4, 2, 2, 3, 7, 5, 0, 4, 4, 0, 1, 4, 3, 3, 3]

    for i in range(len(possion)):
        time.sleep(0.5)
        # 获取Python程序的进程ID
        pid = os.getpid()
        # 实例化进程对象
        process = psutil.Process(pid)
        cap = cv2.VideoCapture("file\streamFile.mp4")
        ret, frame = cap.read()
        while (1):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame', frame)
            # 计算当前占用内存
            memory_usage = process.memory_info().rss
            # 转换为MB
            memory_usage_mb = memory_usage / 1024 / 1024
            # my memory capacity
            memory_total = 8 * 1024 * 1024 * 1024
            # 内存占用百分比
            memory_percentage = memory_usage / memory_total * 100
            print("memory cos", memory_usage_mb, "MB", "\t内存占用百分比",
                  "{:.2f}".format(memory_percentage), "%")
