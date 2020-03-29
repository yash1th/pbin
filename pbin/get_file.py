import requests


def get_file():
    URL = 'https://pastebin.com/raw/'
    paste_id = input('enter paste id - ').strip()
    response = requests.get(url=URL + paste_id)
    print(response.status_code)
    print(response.content.decode('utf-8'))


if __name__ == '__main__':
    get_file()