import json

from pyhon_core.day06 import __constant

"""
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""

__dict = {
    'name': '骆昊',
    'age': 38,
    'qq': 957658,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}

__file_resource = 'resource/write_json.json'

"""
json.dump()
__dict : 要写入文件的字符串
fs : 文件
ensure_ascii : 禁用了默认的 Unicode 转义
indent : 每一级嵌套的缩进
"""


def write_dict_to_file():
    try:
        with open(__file_resource, 'w', encoding=__constant.__encoding) as fs:
            json.dump(__dict, fs, ensure_ascii=False, indent=4)
    except IOError as e:
        print(e)
    print('保存数据完成!')


def read_file_to_dict():
    try:
        with open(__file_resource, 'r', encoding=__constant.__encoding) as f:
            dict_result = json.load(f)
    except IOError as e:
        print(e)
    print(f'读取数据完成!:{dict_result}')


def read_file_to_dict2():
    try:
        with open(__file_resource, 'r', encoding=__constant.__encoding) as f:
            dict_result = json.loads(f.read())
    except IOError as e:
        print(e)
    print(f'读取数据完成!:{dict_result}')


def main():
    # 将str写入文件
    write_dict_to_file()
    # 从文件中读取json,转为dict并且打印
    read_file_to_dict()  # load() 传入 file
    read_file_to_dict2()  # loads() 传入 str , 比如file.read()


if __name__ == '__main__':
    main()
