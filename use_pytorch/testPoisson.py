# author: miaoyin
# time: 2023-11-14 14:08
import numpy as np

if __name__ == '__main__':
    # 在固定时间间隔内发生的预期事件数
    lam = 3
    random_numbers = np.random.poisson(lam, 100)

    # [1 3 2 2 3 2 3 3 3 1 2 6 5 2 4 4 2 1 4 2 6 1 4 2 2 6 3 3 4 4 2 5 4 2 5 3 3
    #  3 0 3 3 2 5 3 6 4 5 0 3 3 5 6 5 4 5 2 1 3 3 4 3 5 4 1 3 4 3 2 2 3 2 1 4 6
    #  0 3 6 7 4 4 1 9 2 1 1 4 2 2 3 7 5 0 4 4 0 1 4 3 3 3]
    print(random_numbers)
