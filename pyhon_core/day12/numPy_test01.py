import numpy as np


def test_1d():
    print(np.pi)
    # 1D Array
    a = np.array([0, 1, 2, 3, 4])
    b = np.array((0, 1, 2, 3, 4))
    c = np.arange(5)
    d = np.linspace(0, 2 * np.pi, 5)

    print(a)  # >>>[0 1 2 3 4]
    print(b)  # >>>[0 1 2 3 4]
    print(c)  # >>>[0 1 2 3 4]
    print(d)  # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
    print(a[3])  # >>>3


def test_2d():
    # MD Array,
    a = np.array([[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35]])

    print(a[2, 4])  # >>>25
    print(type(a))  # >>><class 'numpy.ndarray'>
    print(a.dtype)  # >>>int64
    print(a.size)  # >>>25 size
    print(a.shape)  # >>>(5, 5) 数组的维度
    print(a.itemsize)  # >>>8 每个元素的字节大小
    print(a.ndim)  # >>>2 数组的维度数
    print(a.nbytes)  # >>>200 整个数组所占的字节数
    print('*' * 200)
    # 运算符
    print(a * 2)  # >>> 每一位都*2
    print(np.sum(a))  # >>>总和
    print(np.min(a))  # >>>最小
    print(np.max(a))  # >>>最大
    print(a.cumsum())  # >>>计算数组的累积和


def test_first():
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5.0, 6.0], [7.0, 8.0]])
    sums = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print(f"Sum = {sums}")
    print(f"Difference = {difference}")
    print(f"Product = {product}")
    print(f"Quotient = {quotient}")


def test_num():
    # Basic Operators
    a = np.arange(25)
    # 重新搞一遍形状
    a = a.reshape((5, 5))
    print(a)
    b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
                  4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
                  56, 3, 56, 44, 78])
    b = b.reshape((5, 5))
    print(b)
    print('*' * 25 + '结果结算' + '*' * 25)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** 2)
    print(a < b)
    print(a > b)
    # 计算两个数组的点积
    print(a.dot(b))


def main():
    # test_first()
    # test_1d()
    # test_2d()
    test_num()


if __name__ == '__main__':
    main()
