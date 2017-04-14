from binascii import unhexlify
from CryptoPals.crypto import aes

file = open("input.txt")

for line in file:
    line = line.replace("\n", "")
    if aes.has_ecb_properties(unhexlify(line)):
        print("Might be using ECB mode:\n\t\"{}\"".format(line))
