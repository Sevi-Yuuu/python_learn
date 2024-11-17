import json;import pandas;pandas.read_csv('aaa.csv', sep='\t', header=None).apply(lambda row: print("UPDATE t_merchant_config SET switch_config = '{}' WHERE merchant_code = {};".format(json.dumps((json.loads(row[0]) if pd.notna(row[0]) else {'h5VersionSwitch': 0, 'pcVersionSwitch': 0})).replace('"', '\\"'),row[1])), axis=1)


# print(type(1731042238000))