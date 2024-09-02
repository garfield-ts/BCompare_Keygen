from lic_manager import LicenseEncoder, LicenseDecoder


if __name__ == '__main__':
    # key = LicenseEncoder().encode()
    key = LicenseEncoder(username="Garfield", atsite="SZTS", user_num=1, serial_num=(666,8888)).encode()
    print(key)
    LicenseDecoder(key).decode()
