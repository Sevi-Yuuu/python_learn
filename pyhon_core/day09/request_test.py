import requests

__url = 'https://zimaoxy.com/q/post/msgbox/'


def main():
    resp = requests.get(__url)
    print(resp.json())


if __name__ == '__main__':
    main()
