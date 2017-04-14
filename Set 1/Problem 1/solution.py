import binascii
import base64

value = input("Input: ")

binary = binascii.unhexlify(value)

print(base64.b64encode(binary).decode("utf-8"))