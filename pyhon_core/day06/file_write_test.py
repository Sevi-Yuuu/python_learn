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

__file_resource = 'resource/write_1.txt'
__need_write_str = 'aaa\nbbb\nccc'


def write1():
    f = open(__file_resource, 'w', encoding=__constant.__encoding)
    f.write(__need_write_str)
    f.close()


def write2():
    print('*' * 200)
    try:
        with(open(__file_resource, 'w', encoding=__constant.__encoding)) as f:
            f.write(__need_write_str)
    finally:
        if f:
            f.close()


def write3():
    print('*' * 200)
    try:
        with(open(__file_resource, 'a', encoding=__constant.__encoding)) as f:
            f.write('\n' + __need_write_str)
    finally:
        if f:
            f.close()


def main():
    write1()  # 写文件 w会truncate 重新写入
    write2()  # 写文件 try with write()
    write3()  # 写文件 try with write() 使用a模式


if __name__ == '__main__':
    main()
