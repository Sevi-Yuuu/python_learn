"""
 集合推导式
 new_set = {expression for item in iterable if condition}
"""

# 生成 0 到 9 的平方数集合
squares_set = {x ** 2 for x in range(10)}
print(squares_set)  # 输出: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 生成偶数的平方数列表
even_squares_set = set()
for x in range(10):
    if x % 2 == 0:
        even_squares_set.add(x ** 2)
print(even_squares_set)  # 输出: [0, 4, 16, 36, 64]

# 生成偶数的平方数集合 -- 推导式
even_squares_set = {x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares_set)  # 输出: {0, 4, 16, 36, 64}
