import matplotlib.pyplot as plt
import numpy as np

"""
所谓布尔屏蔽,就是我们定义好数组,根据条件再次筛选一次函数
"""


def plot_sin():
    a = np.linspace(0, 2 * np.pi, 50)
    b = np.sin(a)
    plt.plot(a, b)
    mask = b >= 0
    plt.plot(a[mask], b[mask], 'bo')
    mask = (b >= 0) & (a <= np.pi / 2)
    plt.plot(a[mask], b[mask], 'go')
    plt.show()


def plot_2_ci_func():
    a = np.linspace(-2000, 1000, 108)
    c = 2  # 假设 c 是 2
    # 定义函数 b
    b = a ** 2 + 5 * a + c
    # 绘制图像
    plt.plot(a, b)
    plt.xlabel('a')
    plt.ylabel('b')
    plt.title('b = a^2 + 5a + c')
    # 网格
    plt.grid(True)
    plt.show()


def main():
    # 画一个sin函数
    plot_sin()
    # 画一个一元二次方程图
    plot_2_ci_func()


if __name__ == '__main__':
    main()
