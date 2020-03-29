import configparser
import sys
from pathlib import Path


def get_config(config_file_path):
    if file_exists(config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            return config
        except configparser.Error as e:
            print(e)


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
        return ''.join(file_content)


def get_login_key(username):
    credentials = get_config('credentials.ini')
    return True if credentials['USER'][username] else False


if __name__ == '__main__':
    print(get_config(sys.argv[1]))
