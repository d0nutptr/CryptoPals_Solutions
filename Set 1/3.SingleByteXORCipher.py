import sys
from binascii import unhexlify, hexlify
from CryptoPals.statistics import char_freq
from CryptoPals.crypto import xor
from CryptoPals import utils

str_input = input("Input Value: ")

value1 = unhexlify(str_input)

top_score = 0
top_key = 0

string_scores = []

for i in range(0, 256):

    test_string = xor.decrypt(value1, bytes([i]))

    try:
        test_string = test_string.decode()

        score = char_freq.score_resemblance_to_english(test_string)

        string_scores.append((score, test_string, i))
    except:
        pass

best_string = "NONE"
best_score = sys.maxsize
best_key = 0

for entry in string_scores:
    if entry[0] < best_score:
        best_score = entry[0]
        best_string = entry[1]
        best_key = int(entry[2])

print(string_scores)

print("\"%s\" (with score: %s and key 0x%s)"%(best_string, best_score, hexlify(utils.int_to_bytes(best_key)).decode()))
