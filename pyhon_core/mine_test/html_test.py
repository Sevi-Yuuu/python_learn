import json

import pandas as pd


def main():
    # 读取 CSV 文件
    df = pd.read_csv('aaa.csv', sep='\t', header=None)
    for index, row in df.iterrows():
        if pd.isna(row[0]):
            json_dict = {'h5VersionSwitch': 0, 'pcVersionSwitch': 0}
        else:
            try:
                json_dict = json.loads(row[0])
                if 'h5VersionSwitch' not in json_dict or json_dict['h5VersionSwitch'] is 1:
                    json_dict['h5VersionSwitch'] = 0
                if 'pcVersionSwitch' not in json_dict or json_dict['pcVersionSwitch'] is 1:
                    json_dict['pcVersionSwitch'] = 0
            except json.JSONDecodeError:
                json_dict = {'h5VersionSwitch': 0, 'pcVersionSwitch': 0}
        result = json.dumps(json_dict).replace('"', '\\"')
        print(f'UPDATE t_merchant_config SET switch_config = \'{result}\' WHERE merchant_code = {row[1]};')


def main2():
    # 使用 apply 遍历 DataFrame 的每一行
    pd.read_csv('aaa.csv', sep='\t', header=None).apply(lambda row: print("UPDATE t_merchant_config SET switch_config = '{}' WHERE merchant_code = {};".format(json.dumps((json.loads(row[0]) if pd.notna(row[0]) else {'h5VersionSwitch': 0, 'pcVersionSwitch': 0})).replace('"', '\\"'), row[1])), axis=1)


if __name__ == '__main__':
    # main()
    main2()
