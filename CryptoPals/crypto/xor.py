from CryptoPals import utils
from CryptoPals.statistics import char_freq


def encrypt(message: bytes, key: bytes) -> bytes:
    key_counter: int = 0
    size = len(message) - 1
    message = utils.bytes_to_int(message)

    for i in range(size + 1):
        message = message ^ (key[key_counter] << (size - i) * 8)
        key_counter += 1
        key_counter %= len(key)

    return utils.int_to_bytes(message)


def decrypt(message: bytes, key: bytes) -> bytes:
    return encrypt(message, key)


def break_vigenere(message: bytes) -> (float, bytes, bytes):
    """
    This will break a vigenere cipher assuming that the plaintext
    is in english. Just hand it bytes and it'll try to do the rest.
    :param message: the message in bytes
    :return: a tuple containing a score, key, and plaintext
    """
    key_sizes = []
    key_cap = 40 if len(message) > 40 else len(message)
    key_tests = 5 if key_cap > 5 else key_cap

    for i in range(2, key_cap):
        spliceable_blocks = (len(message) // i)
        weight = 0

        for j in range(spliceable_blocks - 1):
            weight += utils.hamming_distance(message[j*i:(j+1)*i], message[(j+1)*i:(j+2)*i])

        weight /= i * (spliceable_blocks - 1)
        key_sizes.append((weight, i))

    key_sizes = sorted(key_sizes, key=lambda x: x[0])

    autocracked_results = []

    for key_size in key_sizes[0:key_tests]:
        score, key, plaintext = break_vigenere_known_length(message, key_size[1])
        autocracked_results.append((score, key, plaintext))

    autocracked_results = sorted(autocracked_results, key=lambda x: x[0])

    return autocracked_results[0]


def break_vigenere_known_length(message: bytes, key_length: int) -> (float, bytes, bytes):
    final_key_arr: bytearray = bytearray()

    for i in range(key_length):
        test_block = message[i::key_length]

        single_key_scores = []

        for key in range(256):
            try:
                plaintext = decrypt(test_block, utils.int_to_bytes(key)).decode()
                score = char_freq.score_resemblance_to_english(plaintext)
                single_key_scores.append((score, key))
            except:
                pass

        single_key_scores = sorted(single_key_scores, key=lambda x: x[0])

        final_key_arr.append(single_key_scores[0][1])

    final_key = bytes(final_key_arr)
    final_plaintext = decrypt(message, final_key)
    final_score = char_freq.score_resemblance_to_english_bytes(final_plaintext)

    return final_score, final_key, final_plaintext
