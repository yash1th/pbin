"""
Uploads file to pastebin
"""
# TODO: file format
# TODO: arguments
# TODO: deal with responses

import sys
import requests
from helpers import *


def get_input():
    input_str = sys.stdin.read('enter input need to upload:\n')
    return input_str


def upload_file(args):
    config = get_config('default.ini')

    if args.filepath:
        api_paste_code = get_file_content(args.filepath)
    else:
        input_str = get_input()
        if not input_str:
            api_paste_code = input_str
        else:
            print('error - input is empty, nothing to upload')
            sys.exit()

    data = dict()

    # required parameters
    data['api_dev_key'] = config['DEVELOPER']['key']
    data['api_option'] = config['API_OPTION']['upload']
    data['api_paste_code'] = api_paste_code

    # optional parameters
    data['api_paste_private'] = config['VISIBILITY'][args.visibility]
    data['api_paste_expire_date'] = config['PASTE_EXPIRE'][args.expire]
    if not args.name:
        data['api_paste_name'] = args.name.strip()
    # TODO: add api user key
    # TODO: paste format

    response = requests.post(
        url=config['URL']['post'],
        data=data
    )

    print(response.status_code)
    print(response.content.decode('utf-8'))


if __name__ == '__main__':
    pass
