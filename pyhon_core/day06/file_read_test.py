"""
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常   -  用得少
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""
from pyhon_core.day06 import __constant

__file_resource = 'resource/read_1.txt'


def read1():
    f = open(__file_resource, 'r', encoding=__constant.__encoding)
    print(f.read())
    f.close()


def read2():
    print('*' * 200)
    try:
        with(open(__file_resource, 'r', encoding=__constant.__encoding)) as f:
            print(f.read())
    finally:
        if f:
            f.close()


def read3():
    print('*' * 200)
    try:
        with(open(__file_resource, 'r', encoding=__constant.__encoding)) as f:
            lineNum = 1
            for line in f:
                print(f'第{lineNum}行内容:{line}', end='')
                lineNum += 1
        print()
    finally:
        if f:
            f.close()


def read4():
    print('*' * 200)
    try:
        with(open(__file_resource, 'r', encoding=__constant.__encoding)) as f:
            # 这里lines 是list
            lines = f.readlines()
            print(lines)
    finally:
        if f:
            f.close()


def main():
    read1()  # 读取文件 read()
    read2()  # 读取文件 try with read()
    read3()  # 读取文件 for in read()
    read4()  # 读取文件 readline()


if __name__ == '__main__':
    main()
