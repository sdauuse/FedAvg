# author: miaoyin
# time: 2023-11-13 15:18
import numpy as np
import time

import psutil


# 获取CPU速度

if __name__ == '__main__':

    freq = psutil.cpu_freq()
    min_freq = freq.min / 1000  # 最小频率

    max_freq = freq.max / 1000  # 最大频率

    cur_freq = freq.current / 1000  # 当前频率

    print(f"最小频率：{min_freq:.2f} GHz")

    print(f"最大频率：{max_freq:.2f} GHz")

    print(f"当前频率：{cur_freq:.2f} GHz")

'''def perform_flops_operation():
    # Example: Performing a matrix multiplication as a floating-point operation
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    result = np.dot(a, b)


# 记录开始时间
start_time = time.perf_counter()

# 执行测量的代码
perform_flops_operation()

# 记录结束时间
end_time = time.perf_counter()

# 计算执行时间
execution_time = end_time - start_time

# 估算FLOPS
flops = 2 * 1000 ** 3 * 1000 ** 2 / execution_time  # Assuming 2N^3 floating-point operations for matrix multiplication
flops = flops / 1000 / 1000 / 1000
print(f"Execution Time: {execution_time} seconds")
print(f"Estimated FLOPS: {flops} FLOPS（G）")
'''
