"""
实现图片的复制
rb 读取二进制
wb 写二进制
"""

__file_resource = 'resource/python_logo.png'
__file_target = 'resource/python_logo_2.png'


def main():
    try:
        with open(__file_resource, 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open(__file_target, 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print(f'指定的文件无法打开.{e}')
    except IOError as e:
        print(f'读写文件时出现错误.{e}')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
