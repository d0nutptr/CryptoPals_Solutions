from CryptoPals.statistics import char_freq
from CryptoPals.crypto import xor
from CryptoPals import utils
from binascii import unhexlify, hexlify

file = open("4.txt")

scored_strings = []

for line in file:
    data = unhexlify(line.replace("\n", ""))

    for key in range(0, 256):
        test_decrypt = xor.decrypt(data, bytes([key]))

        try:
            test_string = test_decrypt.decode()
            score = char_freq.score_resemblance_to_english(test_string)
            scored_strings.append((score, key, data, test_string))
        except:
            pass

scored_strings = sorted(scored_strings, key=lambda elem: elem[0])

print("Message: \"%s\"\n\tScore: %s\n\tOriginal: \"%s\"\n\tKey: 0x%s" % (repr(scored_strings[0][3]), scored_strings[0][0], hexlify(scored_strings[0][2]).decode(), hexlify(utils.int_to_bytes(scored_strings[0][1])).decode()))