import requests
from helpers import *


def new_user():
    config = get_config(DEFAULT_CONFIG_PATH)

    username = input('username : ').strip()
    password = input('password : ').strip()
    data = {
        'api_dev_key': config['DEVELOPER']['key'],
        'api_user_name': username,
        'api_user_password': password
    }
    response = requests.post(
        url=config['URL']['login'],
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    content = response.content.decode('utf-8')
    if not check_for_bad_response(response.status_code, content):
        config.set('USER', username, content)
        with open(DEFAULT_CONFIG_PATH, 'w') as f:
            config.write(f)


if __name__ == '__main__':
    new_user()
