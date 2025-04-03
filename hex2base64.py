# #!/usr/bin/env python3

import math
import string
from base64 import b64encode, b64decode

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

def hex2b64(hexStr):
    num = int(hexStr,16)
    numbits = 4 * len(hexStr)
    b64Str = ''
    while numbits >= 6:
        bitchar = num >> (numbits - 6)
        b64Str += alphabet[bitchar]
        num &= 2**(numbits - 6) - 1
        numbits -= 6
    if (numbits > 0):
        num = num << (6 - numbits)
        b64Str += alphabet[num]

    b64Str += (4 - len(b64Str) % 4) * '='
    return b64Str


if __name__ == "__main__":
    s = 'cafebabe'
    b64Str = b64encode(bytes.fromhex(s)).decode()
    assert b64Str == hex2b64(s)
