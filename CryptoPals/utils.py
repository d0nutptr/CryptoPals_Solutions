def int_to_bytes(value: int, endianness: str ="big") -> bytes:
    bitlength = value.bit_length() if value.bit_length() > 0 else 1
    return value.to_bytes((bitlength + 7) // 8, endianness)


def bytes_to_int(value: bytes, endianness: str ="big") -> int:
    return int.from_bytes(value, endianness)


def hamming_distance(value1: bytes, value2: bytes) -> int:
    if len(value1) != len(value2):
        raise ValueError("Byte arrays must both have the same length")

    weight = 0

    v1: int = bytes_to_int(value1)
    v2: int = bytes_to_int(value2)

    for i in range(len(value1) * 8):
        weight += 1 & ((v1 >> i) ^ (v2 >> i))

    return weight
