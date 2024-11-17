import numpy as np

str = 'abc'
print(str * 2)

a = np.arange(12)
print(a)
a = a ** 2
print(a)

palette = np.array([[0, 0, 0],  # black
                    [255, 0, 0],  # red
                    [0, 255, 0],  # green
                    [0, 0, 255],  # blue
                    [255, 255, 255]])  # white

image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
c = palette[image]  # the (2,4,3) color image
print(c)
