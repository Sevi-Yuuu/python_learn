def pi_spigot_generator():
    """使用 Spigot 算法逐位生成 π 的小数位，带缓存机制"""
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    pi_digits = []  # 缓存已计算的 π 小数位
    while True:
        if len(pi_digits) > 0 and len(pi_digits) % 10000 == 0:
            # 每计算 10000 位 π 后，输出一次进度
            print(f"已生成 {len(pi_digits)} 位 π，继续计算……")

        if 4 * q + r - t < n * t:
            pi_digits.append(str(n))  # 添加当前位到缓存
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            r = nr
            n = nn

        current_digit = str(n) if len(pi_digits) == 0 else pi_digits[-1]
        pi_digits.append(current_digit)  # 返回缓存中的当前位

        yield current_digit  # 返回当前位


def find_birthday_in_pi(birthday):
    """在使用 Spigot 算法的 π 生成器中查找生日字符串的位置"""
    pi_digits = pi_spigot_generator()  # π 生成器
    window = ""  # 滑动窗口存储当前 π 小数位
    position = 0  # 记录当前是第几位

    for digit in pi_digits:
        window += digit
        position += 1

        # 如果窗口长度超过生日长度，保持窗口大小
        if len(window) > len(birthday):
            window = window[1:]

        # 查找窗口中是否包含生日
        if window == birthday:
            print(f"生日 {birthday} 出现在 π 的第 {position - len(birthday) + 1} 位")
            return

        # 提示信息
        if position % 100000 == 0:
            print(f"还在计算 π，请稍等……, 当前计算到了 = {position}")

    print(f"生日 {birthday} 未在 π 的小数部分中找到（可能位数不够）")


# 示例调用
birthday = "19990808"  # 示例生日
find_birthday_in_pi(birthday)
