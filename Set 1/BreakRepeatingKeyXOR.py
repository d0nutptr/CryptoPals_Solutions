from CryptoPals.crypto import xor
import base64

file = open("6.txt")

base64_string = base64.b64decode(file.read().replace("\n", ""))

print(xor.break_vigenere(base64_string)[2].decode())
