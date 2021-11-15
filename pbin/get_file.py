import requests
from helpers import *


def download_raw_file(args):
    # if the paste is public or unlisted, then no keys are required
    if len(args.id) != 8:
        raise Exception
    if args.user:
        # write a user handling code
        pass

    config = get_config(DEFAULT_CONFIG_PATH)
    paste_id = input('enter paste id - ').strip()
    response = requests.get(
        url=config['URL']['public_raw_content'] + paste_id
    )

    response_content = response.content.decode('utf-8')


if __name__ == '__main__':
    download_raw_file()
