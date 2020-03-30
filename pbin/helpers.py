import configparser
import sys
from pathlib import Path


DEFAULT_CONFIG_PATH = 'config.ini'


def get_input():
    print('enter input need to upload: - ')
    input_str = sys.stdin.read()
    if not input_str:
        print(f'Error - input is empty, nothing to upload')
        sys.exit()

    return input_str


def get_config(config_file_path):
    if file_exists(config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            return config
        except configparser.Error as e:
            print(e)
            sys.exit()


def file_exists(file_path):
    p = Path(file_path).expanduser()
    if p.is_dir():
        print(f'Error - {file_path} is a directory')
        sys.exit()
    if not p.is_file():
        print(f'Error - {file_path} does not exists')
        sys.exit()
    else:
        return True


def get_file_content(file_path):
    if file_exists(file_path):
        with open(file_path, 'r') as f:
            file_content = f.readlines()

    if not file_content:
        print(f'Error - {file_path} is empty')
        sys.exit()

    return ''.join(file_content)


def get_user_key(config, username):
    _key = config.get('USER', username, fallback=None)
    if _key is not None:
        return _key
    else:
        print(f'Error - {username} cannot be found')
        sys.exit()


def check_for_bad_response(response_status, response_content):
    if response_status != 200 or 'Bad API request' in response_content:
        print(response_content)
        sys.exit()
    return False


if __name__ == '__main__':
    pass
