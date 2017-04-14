from CryptoPals.crypto import aes
import base64

file = open("input.txt")
key = input("KEY: ").encode()
ciphertext = base64.b64decode(file.read().replace("\n", ""))

plaintext: bytes = aes.decrypt(key, ciphertext, aes.Mode.ECB)

print(plaintext.decode())
