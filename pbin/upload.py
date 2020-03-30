import requests
from helpers import *


def upload_file(args):
    config = get_config(DEFAULT_CONFIG_PATH)

    if args.filepath:
        api_paste_code = get_file_content(args.filepath)

    if args.input:
        api_paste_code = get_input()

    data = dict()

    # required parameters
    data['api_dev_key'] = config['DEVELOPER']['key']
    data['api_option'] = config['API_OPTION']['upload']
    data['api_paste_code'] = api_paste_code

    # optional parameters
    data['api_paste_private'] = config['VISIBILITY'][args.visibility]
    data['api_paste_expire_date'] = config['PASTE_EXPIRE'][args.expire]
    if args.name:
        data['api_paste_name'] = args.name.strip()

    if args.user:
        data['api_user_key'] = get_user_key(config, args.user)

    response = requests.post(
        url=config['URL']['post'],
        data=data
    )

    content = response.content.decode('utf-8')
    if not check_for_bad_response(response.status_code, content):
        print(content)


if __name__ == '__main__':
    pass
