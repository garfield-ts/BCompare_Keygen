import os
import re
import base58
from typing import Literal
from Crypto.Util.number import bytes_to_long
from Crypto.Util.Padding import pad
from const import LicType
from rsa_key import RsaKeyInfo


RSA_KEY = RsaKeyInfo()


def int_to_bytes(n: int, order: Literal["little", "big"] = 'little') -> bytes:
    # 获取整数的位长度
    bit_length = n.bit_length()
    # 计算所需的最小字节数
    byte_length = (bit_length + 7) // 8
    # 转换为字节序列，使用大端字节序
    byte_array = n.to_bytes(byte_length, byteorder=order)
    return byte_array


def gen_padding_lic(data: bytes) -> bytes:
    ret = b'\x00'
    sz = len(data)
    if sz:
        ret = len(data).to_bytes(1, 'little') + data
    return ret


def check_serial(serial: str) -> bool:
    pattern = r'^[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}$'
    match = re.match(pattern, serial)
    return bool(match)


class LicenseEncoder:
    username: str
    atsite: str
    user_num: int
    serial_num: str
    license_type: LicType

    def __init__(self, username: str = "Test", atsite: str = "Home", user_num: int = 1, serial_num='Abcd-Efgh',
                 lic_type: LicType = LicType.ALL):
        self.username = username
        self.atsite = atsite
        self.user_num = user_num
        self.serial_num = serial_num if check_serial(serial_num) else 'Abcd-Efgh'
        self.license_type = lic_type

    def gen_lic(self):
        # 生成授权数据的[头部]
        lic = b'\x04SCTR'
        lic += gen_padding_lic(b'')
        lic += gen_padding_lic(b'')
        lic += gen_padding_lic(b'')
        lic += gen_padding_lic(b'')
        lic += gen_padding_lic(b'')
        # 生成授权数据的[机构信息]部分
        lic += b'\x01'
        lic += gen_padding_lic(b'73051')
        lic += gen_padding_lic(f'{self.user_num}|{self.atsite}'.encode())
        lic += b'\x06'
        # 生成授权数据的[版本]部分
        lic += self.license_type.value.to_bytes(1, 'little')
        # 生成授权数据的[随机数]部分
        lic += os.urandom(5)
        lic += b'\x09'
        lic += self.serial_num.encode()
        lic += gen_padding_lic(b'0')
        lic += gen_padding_lic(b'30')
        lic += gen_padding_lic(b'15')
        # 生成授权数据的[用户信息]部分
        lic += gen_padding_lic(f'{self.username}'.encode())
        # 生成授权数据的[尾部]
        lic += gen_padding_lic(b'0')
        lic += gen_padding_lic(b'0')
        lic = pad(lic, 0xff)
        return lic

    def encode(self):
        lic = self.gen_lic()
        lic_data = int.from_bytes(lic, 'little')
        enc_data = RSA_KEY.enc(lic_data)
        data = int_to_bytes(enc_data)
        lic_key = '--- BEGIN LICENSE KEY ---\r\n' + base58.b58encode(
            data).decode() + '\r\n--- END LICENSE KEY -----\r\n'
        return lic_key


class LicenseDecoder:
    data: bytes

    def __init__(self, lic_key: str):
        lic_key = lic_key.replace('--- BEGIN LICENSE KEY ---\r\n', '')
        lic_key = lic_key.replace('\r\n--- END LICENSE KEY -----\r\n', '')
        enc_lic_data = base58.b58decode(lic_key.encode())
        enc_data = int.from_bytes(enc_lic_data, 'little')
        raw_lic_data = RSA_KEY.dec(enc_data)
        self.data = int_to_bytes(raw_lic_data)

    def dec_org(self) -> (int, str):
        pre_uname = b'\x0573051'
        pre_idx = self.data.index(pre_uname) + len(pre_uname) + 1
        tmp_data = self.data[pre_idx:]

        post_uname = b'\x06'
        post_idx = tmp_data.index(post_uname)
        num, atsite = tmp_data[:post_idx].decode().strip().split('|')[:2]
        self.data = tmp_data
        return int(num), atsite

    def dec_version(self) -> str:
        pre_uname = b'\x06'
        pre_idx = self.data.index(pre_uname) + len(pre_uname)
        tmp_data = self.data[pre_idx:]
        ver = bytes_to_long(tmp_data[:1])
        self.data = tmp_data
        return hex(ver)

    def dec_random(self) -> (int, str):
        pre_rand = b'\x09'
        pre_idx = self.data.index(pre_rand)
        rand_1 = bytes_to_long(self.data[1:pre_idx])

        tmp_data = self.data[pre_idx:]
        post_rand = b'\x010\x0230\x0215'
        post_idx = tmp_data.index(post_rand)
        rand_2 = tmp_data[1:post_idx].split(b'-')[:2]
        self.data = tmp_data
        return hex(rand_1), f'{rand_2[0].decode()}-{rand_2[1].decode()}'

    def dec_uname(self) -> str:
        pre_uname = b'\x01\x30\x0230\x0215'
        pre_idx = self.data.index(pre_uname) + len(pre_uname) + 1
        tmp_data = self.data[pre_idx:]

        post_uname = b'\x010\x010'
        post_idx = tmp_data.index(post_uname)
        username = tmp_data[:post_idx].decode()
        self.data = tmp_data
        return username

    def decode(self):
        num, atsite = self.dec_org()
        version = self.dec_version()
        rand, serial_num = self.dec_random()
        username = self.dec_uname()
        print('--- Begin Decode Information ---')
        print(f"Version: {version}")
        print(f"Serial: {serial_num}")
        print(f"Username: {username}")
        print(f"Company: {atsite}")
        print(f"Max users: {num}")
        print(f"Random: {rand}")
        print('--- End Decode Information ---')
