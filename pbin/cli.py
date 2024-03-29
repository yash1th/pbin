import argparse
from upload import upload_file
import sys


def get_file(args):
    print('get file has been called')


def get_args():
    parser = argparse.ArgumentParser(description='pastebin cli...')
    subparsers = parser.add_subparsers(help='sub-command help')

    # parser and arguments for upload
    parser_upload = subparsers.add_parser('upload', help='uploading a file')
    user_type = parser_upload.add_mutually_exclusive_group()
    user_type.add_argument('--anon', default=False, action='store_true', help='upload anonymously')
    user_type.add_argument('--user', type=str, help='upload with user')
    file_type = parser_upload.add_mutually_exclusive_group(required=True)
    file_type.add_argument('--filepath', type=str, help='file path')
    file_type.add_argument('--input', action='store_true', help='type input')
    parser_upload.add_argument('--name', type=str, help='file name on pastebin')
    parser_upload.add_argument('--visibility',  choices=['public', 'private', 'unlisted'], default='unlisted',
                               help='paste visibility')

    parser_upload.add_argument('--expire', type=str.upper, default='1D',
                               choices=['N', '10MI', '1H', '1D', '1W', '2W', '1M', '6M', '1Y'], help='paste expiry date')

    parser_upload.set_defaults(func=upload_file)

    # parser and arguments for reading a file
    parser_get = subparsers.add_parser('get', help='get command')
    parser_get.add_argument('paste_id')
    parser_get.add_argument('--user', type=str.lower, help='user for private pastes')
    parser_get.add_argument('-w', '--write', type=str, help='write to a file')
    parser_get.set_defaults(func=get_file)

    args = parser.parse_args()

    args.func(args)

    return args
    # parser_user = subparsers.add_parser('user', help='user related')
    # parser_get = subparsers.add_parser('get', help='get command')


def main():
    args = get_args()
    print(args)


if __name__ == '__main__':
    main()
