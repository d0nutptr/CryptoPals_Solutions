from enum import Enum
from Crypto.Cipher import AES


class Mode(Enum):
    ECB = 0
    CBC = 1
    CTR = 2
    CFB = 3
    GCM = 4


def encrypt(key: bytes, plaintext: bytes, mode: Mode, params=None):
    if mode == Mode.ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(plaintext)
    else:
        return None


def decrypt(key: bytes, ciphertext: bytes, mode: Mode, params=None):
    if mode == Mode.ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.decrypt(ciphertext)
    else:
        return None
