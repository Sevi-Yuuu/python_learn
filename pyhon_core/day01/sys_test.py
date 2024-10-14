"""
sys模块
"""
import sys

print(sys.version_info)
print(sys.version)


def _for_each():
    for _ in range(100, 2):
        if _ == 2:
            sys.exit()
        print(_)


if __name__ == '__main__':
    _for_each()
    print('good')
