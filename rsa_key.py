import base64
from const import ENCODE_TRANS, DECODE_TRANS, PUBLIC_KEY, HEX_D


def base64_encode_ext(input: bytes) -> bytes:
    return base64.b64encode(input).translate(ENCODE_TRANS)


def base64_decode_ext(input: bytes) -> bytes:
    pad = len(input) % 4
    if pad != 0:
        input += b'=' * pad
    return base64.b64decode(input.translate(DECODE_TRANS))


def reverse_by_word(data: bytes):
    ret = b''
    for i in range(0, len(data), 4):
        ret += data[i:i + 4][::-1]
    return ret

class RsaKeyInfo:
    E: int = 0
    D: int = 0
    N: int = 0

    def __init__(self):
        _bs_e, _bs_n = PUBLIC_KEY.split(B':')
        _bs_e = base64_decode_ext(_bs_e)
        _bs_n = base64_decode_ext(_bs_n)
        _bs_e_le = reverse_by_word(_bs_e)
        _bs_n_le = reverse_by_word(_bs_n)
        self.E = int.from_bytes(_bs_e_le, 'little')
        self.N = int.from_bytes(_bs_n_le, 'little')
        self.D = int(HEX_D, 16)

    def enc(self, i_msg: int) -> int:
        enc = pow(i_msg, self.D, self.N)
        return enc

    def dec(self, i_msg: int) -> int:
        dec = pow(i_msg, self.E, self.N)
        return dec