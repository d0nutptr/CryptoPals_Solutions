from CryptoPals.crypto import xor
import base64

file = open("input.txt")

base64_string = base64.b64decode(file.read().replace("\n", ""))

result = xor.break_vigenere(base64_string)

print("KEY: {}".format(result[1].decode()))
print("RESULT: {}".format(result[2].decode()))
