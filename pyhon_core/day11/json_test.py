"""
JSON 常用操作 demo
json.loads() - 将 JSON 字符串解析为 Python 字典或列表
"""
import json


def loads():
    """
    json.loads() - 将 JSON 字符串解析为 Python 字典或列表
    """
    json_str = '{"name": "Alice", "age": 25}'
    print(json.loads(json_str))  # dict

    json_str = '[{"name": "Alice", "age": 25},{"name": "ben", "age": 15}]'
    print(json.loads(json_str))  # list<dict>


def dumps():
    """
    json.dumps() - 将 Python 字典或列表转换为 JSON 字符串
    """
    _data_dict = {"name": "Alice", "age": 25}
    print(json.dumps(_data_dict))  # json_str

    _data_list = [{"name": "Alice", "age": 25}, {"name": "ben", "age": 15}]
    """
    indent 缩进
    ensure_ascii 为True 只保留ASCII
    """
    print(json.dumps(_data_list, indent=4, ensure_ascii=False))  # json_array


def main():
    loads()  # json_to_python
    dumps()  # python_to_json
    # load()   # json_file_to_python
    # dumps()  # python_to_json_file


if __name__ == '__main__':
    main()
