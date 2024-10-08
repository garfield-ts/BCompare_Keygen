from enum import Enum


STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
CUSTOM_ALPHABET = b'+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ENCODE_TRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
DECODE_TRANS = bytes.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)
PUBLIC_KEY = b"++11Ik:7EFlNLs6Yqc3p-LtUOXBElimekQm8e3BTSeGhxhlpmVDeVVrrUAkLTXpZ7mK6jAPAOhyHiokPtYfmokklPELfOxt1s5HJmAnl-5r8YEvsQXY8-dm6EFwYJlXgWOCutNn2+FsvA7EXvM-2xZ1MW8LiGeYuXCA6Yt2wTuU4YWM+ZUBkIGEs1QRNRYIeGB9GB9YsS8U2-Z3uunZPgnA5pF+E8BRwYz9ZE--VFeKCPamspG7tdvjA3AJNRNrCVmJvwq5SqgEQwINdcmwwjmc4JetVK76og5A5sPOIXSwOjlYK+Sm8rvlJZoxh0XFfyioHz48JV3vXbBKjgAlPAc7Npn+wk"
HEX_D = "4860d32b474ff398b0058aaf111fe820f8bebad4342cb40b6fd7652b37a92cf077d58ca7374dcf65615fe846e73ababe6a729a59ebdd8b980bbeb47f3ef8041decc465118a40d76293b5fce1271d87865b3f1dc116f2637d8dfa338a5103ef14e9c28f620c325c1e241e2bfa9258d16b1239c5c06ce13ec2fe377fac038a0ff0eb0f5910018724fd4bf429f1c0fac86af083acdab388c18e281a5ea9976b385e6c0383485135f1e68cd7a3c0ab6d36b07aa1404e081083158e523129ace077972fc3bd9424fbe86c64b33e8916e0a15c0f5a346e2260fb565ee00741268e6987b978df646c81bd72b55e0ea94f5f51956bf80ffc4c51f6fcaaab96135c888523"


class LicType(Enum):
    WINDOWS = 4
    LINUX = 8
    MACOS = 0x10
    PRO = 0x21
    ALL = WINDOWS|LINUX|MACOS|PRO

    def __or__(self, other):
        return self.value | other.value