def pkcs7(data: bytes, blocksize: int = 8):
    remainder = blocksize - (len(data) % blocksize)

    # if the data is a perfect multiple of the blocksize,
    # we should add another block just for padding
    # remainder = remainder if remainder > 0 else blocksize

    padding = bytearray(bytes([remainder]) * remainder)
    data = bytearray(data)
    data.extend(padding)

    return bytes(data)

