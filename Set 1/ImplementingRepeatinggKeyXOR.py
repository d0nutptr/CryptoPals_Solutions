from binascii import hexlify
from CryptoPals.crypto import xor

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

cipher = xor.encrypt(message.encode(), "ICE".encode())

print(hexlify(cipher).decode())
