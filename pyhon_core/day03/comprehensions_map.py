"""
 字典推导式
 new_dict = {key_expression: value_expression for item in iterable if condition}
"""

# 生成字典，键为 0 到 4，值为它们的平方
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 生成偶数的平方数字典
even_squares_dict = dict()
for x in range(10):
    if x % 2 == 0:
        even_squares_dict[x] = x ** 2
print(even_squares_dict)  # 输出: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 生成偶数的平方数字典 -- 推导式
even_squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)  # 输出: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
