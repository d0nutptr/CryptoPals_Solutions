from CryptoPals.crypto import padding


message = input("Message: ").encode()
blocksize = int(input("Block size: "))

message = padding.pkcs7(message, blocksize)

print("Message: {}".format(message))