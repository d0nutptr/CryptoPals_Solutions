import sys


__english_char_frequencies = {"e": 12.02, "t": 9.10, "a": 8.12, "o": 7.68, "i": 7.31, "n": 6.95, "s": 6.28, "r": 6.02, "h": 5.92, "d": 4.32, "l": 3.98, "u": 2.88, "c": 2.71, "m": 2.61, "f": 2.30, "y": 2.11, "w": 2.09, "g": 2.03, "p": 1.82, "b": 1.49, "v": 1.11, "k": 0.69, "x": 0.17, "q": 0.11, "j": 0.10, "z": 0.07}
__ignored_chars = ['\n', '\r', '\t', ' ', "\'", '!', '?', ',', '$']


def score_resemblance_to_english(message: str, frequencies: map =__english_char_frequencies) -> float:
    score = 0

    char_count = {}

    for c in message.lower():
        if c in char_count:
            char_count[c] = char_count[c] + 1
        else:
            char_count[c] = 1

    for key in char_count.keys():
        key = key.lower()
        freq = 100 * char_count[key] / len(message)
        expected = 1000

        if key in frequencies:
            expected = frequencies[key]

        if key not in __ignored_chars:
            score += abs(freq - expected) ** 2

    return score


def score_resemblance_to_english_bytes(message: bytes) -> float:
    score = sys.maxsize

    try:
        str_message = message.decode()
        score = score_resemblance_to_english(str_message)
    except:
        pass

    return score
