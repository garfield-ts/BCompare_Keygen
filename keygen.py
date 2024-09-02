from lic_manager import LicenseEncoder, LicenseDecoder


if __name__ == '__main__':
    # key = LicenseEncoder().encode()  # 使用默认信息生成注册密钥 (Test / Home / 1 user / Random serial)
    # 使用自定义信息生成注册密钥 (Garfield / SZTS / 1 user / 0666-8888)
    key = LicenseEncoder(username="Garfield", atsite="SZTS", user_num=1, serial_num=(666,8888)).encode()
    print(key)
    # 密钥解码功能，解码出对应的用户名等信息
    LicenseDecoder(key).decode()
