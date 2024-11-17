import numpy as np


def where_func_test():
    """
    where 函数 返回的是索引, 而不是值
    """
    a = np.arange(0, 100, 10)
    b = np.where(a < 50)
    c = np.where(a >= 50)[0]
    print(a)  # >>>[ 0 10 20 30 40 50 60 70 80 90]
    print(b)  # >>> 返回的是索引
    print(a[c])  # >>> 返回的是值


def main():
    # where 函数测试
    where_func_test()


if __name__ == '__main__':
    main()
