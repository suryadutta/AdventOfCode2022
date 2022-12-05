import string
from utils import get_data

LETTER_NUM_MAPPING = {
    letter: i + 1
    for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

DATA = get_data()


def run_part_a() -> str:

    priority_sum = 0
    for line in DATA:

        size = int(len(line) / 2)
        first_sack = set(line[:size])
        second_sack = set(line[size:])

        common_letter = None
        for letter in first_sack:
            if letter in second_sack:
                common_letter = letter
                break
        assert common_letter is not None

        priority_sum += LETTER_NUM_MAPPING[common_letter]

    return str(priority_sum)


def run_part_b() -> str:

    priority_sum = 0
    for i in range(1, len(DATA) + 1):
        if i % 3 == 0:
            first_sack = set(DATA[i - 3])
            second_sack = set(DATA[i - 2])
            third_sack = set(DATA[i - 1])

            common_letter = None
            for letter in first_sack:
                if letter in second_sack and letter in third_sack:
                    common_letter = letter
                    break
            assert common_letter is not None

            priority_sum += LETTER_NUM_MAPPING[common_letter.lower()]

    return str(priority_sum)