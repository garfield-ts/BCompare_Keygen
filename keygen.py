import argparse
from lic_manager import LicenseEncoder, LicenseDecoder, check_serial


def init_parser():
    arg_parser = argparse.ArgumentParser(description='Generate a license key for Beyond Compare 5.')
    arg_parser.add_argument('-v', '--version', action='version', help='Show version', version='BCompare_Keygen 1.1')
    arg_parser.add_argument('-u', '--user', help='Username', default='Test')
    arg_parser.add_argument('-c', '--company', help='Company', default='Home')
    arg_parser.add_argument('-s', '--serial', help='Serial number', default='Abcd-Efgh')
    arg_parser.add_argument('-n', '--num', help='Max user number', default=1)

    arg_list = arg_parser.parse_args()
    return arg_list

if __name__ == '__main__':
    args = init_parser()
    serial = args.serial
    if not check_serial(serial):
        print(f'Serial num [{serial}] invalid, use [Abcd-Efgh] as default.')
        serial = 'Abcd-Efgh'
    key = LicenseEncoder(username=args.user, atsite=args.company, user_num=args.num, serial_num=serial).encode()
    print(key)
    # 密钥解码功能，解码出对应的用户名等信息
    # LicenseDecoder(key).decode()
