from binascii import unhexlify, hexlify

str1 = input("Input 1: ")
str2 = input("Input 2: ")

value1 = unhexlify(str1)
value2 = unhexlify(str2)

xor = int.from_bytes(value1, byteorder="big") ^ int.from_bytes(value2, byteorder="big")

xor = xor.to_bytes((xor.bit_length() + 7) // 8, byteorder="big")

print(hexlify(xor).decode("utf-8"))
