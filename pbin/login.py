import requests
from pathlib import Path
import json
from helpers import *


def login():
    config = get_config('defaults.ini')

    username = input('username : ').strip()
    password = input('password : ').strip()
    data = {
        'api_dev_key': config['DEVELOPER']['key'],
        'api_user_name': username,
        'api_user_password': password
    }
    response = requests.post(url=config['URL']['login'], data=data,
                             headers={'Content-Type': 'application/x-www-form-urlencoded'})

    print(response.content.decode('utf-8'))



    #config['USER'] = {f'{username}': response.content.decode('utf-8')}
    # config.set('USER', username, response.content.decode('utf-8'))
    # with open(config_file_path, 'w') as f:
    #     config.write(f)


if __name__ == '__main__':
    login()
