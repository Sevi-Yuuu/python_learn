"""
根据uid 或者 注单id 获取用户的 url
1. 注单id-> 获取uid 继续下一步
2. uid获取缓存继续下一步 loginUrl
3. 没有值 ,通过商户信息,用户信息调用登录接口
4. 返回loginUrl
"""

import argparse
import configparser
import hashlib
import json
import re
import threading
import time

import requests

_content_type_from_data = {'Content-Type': 'application/x-www-form-urlencoded'}

config = configparser.ConfigParser()
config.read('config.ini')
# thread_local
thread = threading.local()
env_total = {
    't': 'test',
    'u': 'uat',
    's': 'try',  # sandbox
    'p': 'prod'
}


class Constant(object):
    manager_login_url = '/login'
    manager_getOrderDetail_url = '/tOrder/detail'
    manager_getCacheByUidOrToken_url = '/userManage/getCacheByUidOrToken'
    manager_getMerchantList_url = '/tMerchant/list'
    manager_get_userInfo_by_uid_url = '/tuser/list'
    user_login_url = '/api/user/login'

    @staticmethod
    def get_js_time_str():
        return '?jstime=' + str(int(time.time() * 1000))


def build_manager_token_to_env(trust_refresh=False):
    """
    登录业务后台,获取TOKEN
    """
    if len(config[thread.env]['manager_login_token']) != 0 and not trust_refresh:
        return config[thread.env]['manager_login_token']
    conn = config[thread.env]
    url = conn['manager_base_url'] + Constant.manager_login_url + Constant.get_js_time_str()
    manager_data = {'username': conn['manager_login_username'],
                    'password': conn['manager_login_password']}
    response_str = ''
    try:
        response = requests.post(url, headers=_content_type_from_data, data=manager_data, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        config[thread.env]['manager_login_token'] = result_dict['data']
        # 强制写回到文件
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print('业务后台登录成功---go on')
    except json.JSONDecodeError:
        print(f'业务后台登录,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'request,error,msg:{e}')


def get_uid_by_order_no(order_no):
    """
    根据order_no 查询uid
    """
    conn = config[thread.env]
    url = conn[
              'manager_base_url'] + Constant.manager_getOrderDetail_url + Constant.get_js_time_str() + '&orderNo=' + str(
        order_no)
    header = {
        'Cookie': 'visid_incap_3031666=hv/r8USqRWqHmxnhoXau1/9J/mUAAAAAQUIPAAAAAACuiAHzI1msFNfeNG3iUHEa; visid_incap_3061995=WCxgfoxyQ8emOLU1YphVyvYsWGYAAAAAQUIPAAAAAACrNKoxYWInGX+A1mUDAuoP; route=1729237973.037.351829.311299; Authorization=' +
                  config[thread.env]['manager_login_token']
    }
    response_str = ''
    try:
        response = requests.post(url, headers=header, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        if result_dict['code'] != 200:
            print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
            if result_dict['code'] == 1500:
                run_core(True)
            return None
        uid = result_dict['data']['uid']
        print(f'您输入的是注单号, 查询出来的uid为==>{uid}, --- go on')
        return uid
    except json.JSONDecodeError:
        print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'request,error,msg:{e}')


def get_merchant_info_by_merchant_code(merchant_code):
    conn = config[thread.env]
    url = (conn[
               'manager_base_url'] + Constant.manager_getMerchantList_url + Constant.get_js_time_str() + '&page=1&limit=10&appDomain=&merchantCode='
           + str(merchant_code))
    header = {
        'Cookie': 'visid_incap_3031666=hv/r8USqRWqHmxnhoXau1/9J/mUAAAAAQUIPAAAAAACuiAHzI1msFNfeNG3iUHEa; visid_incap_3061995=WCxgfoxyQ8emOLU1YphVyvYsWGYAAAAAQUIPAAAAAACrNKoxYWInGX+A1mUDAuoP; route=1729237973.037.351829.311299; Authorization=' +
                  config[thread.env]['manager_login_token']
    }
    response_str = ''
    try:
        response = requests.post(url, headers=header, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        if result_dict['code'] != 0:
            print(f'业务后台查询merchant信息,返回错误JSON,msg:{response_str}')
            if result_dict['code'] == 1500:
                run_core(True)
                return None
        if result_dict is None or result_dict['data'] is None:
            return None
        merchant_info = result_dict['data'][0]
        # print(f'商户号{merchant_code}, 查询出来的商户信息为==>{merchant_info}, --- go on')
        return merchant_info
    except json.JSONDecodeError:
        print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'request,error,msg:{e}')


def prepare_param_get_user_info_by_id(uid):
    conn = config[thread.env]
    url = conn[
              'manager_base_url'] + Constant.manager_get_userInfo_by_uid_url + Constant.get_js_time_str() + 'page=1&limit=10&username=&uid=' + str(
        uid)
    header = {
        'Cookie': 'visid_incap_3031666=hv/r8USqRWqHmxnhoXau1/9J/mUAAAAAQUIPAAAAAACuiAHzI1msFNfeNG3iUHEa; visid_incap_3061995=WCxgfoxyQ8emOLU1YphVyvYsWGYAAAAAQUIPAAAAAACrNKoxYWInGX+A1mUDAuoP; route=1729237973.037.351829.311299; Authorization=' +
                  config[thread.env]['manager_login_token']
    }
    response_str = ''
    try:
        response = requests.post(url, headers=header, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        if result_dict['code'] != 0:
            print(f'业务后台查询分组用户信息,返回错误JSON,msg:{response_str}')
            if result_dict['code'] == 1500:
                run_core(True)
                return None
        if result_dict is None or result_dict['data'] is None:
            return None
        user_info_dict = result_dict['data'][0]
        # print(f'商户号{merchant_code}, 查询出来的商户信息为==>{merchant_info}, --- go on')
        return user_info_dict
    except json.JSONDecodeError:
        print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'prepare_param_get_user_info_by_id-request,error,msg:{e}')


def md5_encrypt(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def login_user(uid):
    user_info_dict = prepare_param_get_user_info_by_id(uid)
    if uid is None:
        print(f'用户id:{uid} 不存在')
    merchant_code = user_info_dict['merchantCode'].split('--->')[0]
    merchant_code_group_code = user_info_dict['merchantCode'].split('--->\u7EC4:')[1]
    merchant_info = get_merchant_info_by_merchant_code(merchant_code)
    user_name = user_info_dict['username']
    timestamp = str(int(time.time() * 1000))
    terminal = 'pc'
    sign = merchant_info['key']
    param_a = md5_encrypt(f"{merchant_code}&{user_name}&{terminal}&{timestamp}")
    signature = md5_encrypt(f"{param_a}&{sign}")
    if thread.env in ['try', 'prod']:
        login_url_per_fix = config[thread.env]['api_login_url']
    else:
        login_url_per_fix = config[thread.env][f'api_login_url_{merchant_code_group_code}']

    if thread.env in ['test', 'uat', 'try']:
        login_url_per_fix += '/yewu7new'

    url = login_url_per_fix \
          + Constant.user_login_url \
          + f'?userName={user_name}&terminal={terminal}&merchantCode={merchant_code}&timestamp={timestamp}&signature={signature}'
    header = {
        'x-forwarded-for': ''
    }
    response_str = ''
    try:
        print(f'用户登录开始-------------->:{url}\r\n msg:{response_str}')
        response = requests.post(url, headers=header, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        if result_dict['code'] not in '0000':
            print(f'用户登录,返回错误JSON,param_url-------------->:{url}\r\n msg:{response_str},headers:{header}')
        if result_dict is None or result_dict['data'] is None:
            print(f'用户登录,返回错误JSON,param_url-------------->:{url}\r\n msg:{response_str}')
            return None
        login_url = result_dict['data']['loginUrl'] + '&pb=0'
        print(f'自动用户登录成功, 返回重要信息:{login_url}')
    except json.JSONDecodeError:
        print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'login_user-request,error,msg:{e}')


def build_user_login_url(user_info_str):
    url = config[thread.env][
              'manager_base_url'] + Constant.manager_getCacheByUidOrToken_url + Constant.get_js_time_str()
    header = {
        'Cookie': 'visid_incap_3031666=hv/r8USqRWqHmxnhoXau1/9J/mUAAAAAQUIPAAAAAACuiAHzI1msFNfeNG3iUHEa; '
                  'visid_incap_3061995=WCxgfoxyQ8emOLU1YphVyvYsWGYAAAAAQUIPAAAAAACrNKoxYWInGX+A1mUDAuoP; '
                  'route=1729237973.037.351829.311299; Authorization=' +
                  config[thread.env]['manager_login_token']
    }
    manager_data = {'uid': user_info_str}
    response_str = ''
    try:
        response = requests.post(url, headers=header, data=manager_data, timeout=3)
        response_str = response.text
        result_dict = json.loads(response_str)
        if result_dict['code'] != 200:
            print(f'业务后台查询userInfo,返回错误JSON,msg:{response_str}')
            if result_dict['code'] == 1500:
                run_core(True)
            return None
        result = result_dict['data']
        match = re.search(r'\{.*}', result)
        if not match:
            # print(f'返回的数据不对:{result}')
            if len(thread.param) == 40:
                print(f'TOKEN:【{user_info_str}】 已经过期了, 无法登录')
                return
            print('开始拼装用户登录参数,进行登录' + '.' * 25)
            login_user(user_info_str)
            # 重新查询下用户信息
            time.sleep(2)  # 休息个2秒,等等缓存
            build_user_login_url(user_info_str)
            return
        data = json.loads(match.group(0))

        login_url = data['loginUrl']
        merchant_code = data['merchantCode']
        terminal = data['terminal']
        uid = data['userId']
        apiDomain = data['apiDomain']
        # 这个时候要查一下商户的使用中的域名
        merchant_info_dict = get_merchant_info_by_merchant_code(merchant_code)
        user_info = {'uid': uid, 'terminal': terminal, 'merchant_code': merchant_code}
        print('\r\n\r\n\r\n')
        print(f'得到的用户常规信息==>\r\n{user_info}')
        print('\r\n\r\n\r\n')
        print(f'得到的用户登录原始路径如下==>\r\n{login_url}' + '&pb=0')
        if merchant_info_dict is not None:
            pc_login_url = merchant_info_dict['pcDomain'] + '?' + login_url.split('?')[1] + '&pb=0'
            h5_login_url = merchant_info_dict['h5Domain'] + '?' + login_url.split('?')[1] + '&pb=0'
            print(f'得到的用户PC登录路径如下==>\r\n{pc_login_url}')
            print(f'得到的用户H5登录路径如下==>\r\n{h5_login_url}')

    except json.JSONDecodeError:
        print(f'业务后台查询uid,返回错误JSON,msg:{response_str}')
    except Exception as e:
        print(f'build_user_login_url-request,error,msg:{e}')


def run_core(param=True):
    """
    主单号 16位
    uid 18位
    token 40位
    :return: Login_Url
    """
    # 登录业务后台
    build_manager_token_to_env(param)
    print(thread.param)

    if bool(re.fullmatch(r'\d{16}', thread.param)):
        uid = get_uid_by_order_no(thread.param)
        if uid is None:
            return
        thread.param = uid
    if bool(re.fullmatch(r'\d{18}', thread.param)) or len(thread.param) == 40:
        build_user_login_url(thread.param)

    print(thread.param)


if __name__ == '__main__':
    # 初始化解析器
    parser = argparse.ArgumentParser(description="注意环境信息使用简写")
    # 添加参数
    parser.add_argument("env", type=str, default='p', help="t(test) u(uat) (s)sandbox (p) prod")
    parser.add_argument("param", type=str, help="这是主单号或者uid或者token")
    # 可选参数
    parser.add_argument("--h", action="store_true", help="t(test) u(uat) (s)sandbox (p) prod")
    # 解析参数
    args = parser.parse_args()
    if len(args.env) is 1:
        thread.env = env_total.get(args.env)
    else:
        thread.env = args.env
    thread.param = args.param
    run_core()
