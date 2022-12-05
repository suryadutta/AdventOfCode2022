import string
from typing import Tuple, List
from src.utils import get_data

LETTER_NUM_MAPPING = {
    letter: i + 1
    for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

DATA = get_data()


def split_equal_string(input: str) -> Tuple[str, str]:
    size = int(len(input) / 2)
    first_sack = input[:size]
    second_sack = input[size:]
    return first_sack, second_sack


def find_common_letter(inputs: List[str]) -> str:
    assert len(inputs) > 1, "Must have more than 1 input"

    common_letters = list(
        set(inputs[0]).intersection(*map(lambda x: list(x), inputs[1:]))
    )

    assert (
        len(common_letters) == 1
    ), f"Expected 1 common letter, got {len(common_letters)}"
    return common_letters[0]


def run_part_a() -> str:

    priority_sum = 0
    for line in DATA:
        first_sack, second_sack = split_equal_string(line)
        common_letter = find_common_letter([first_sack, second_sack])
        priority_sum += LETTER_NUM_MAPPING[common_letter]

    return str(priority_sum)


def run_part_b() -> str:

    priority_sum = 0
    for i in range(1, len(DATA) + 1):
        if i % 3 == 0:
            common_letter = find_common_letter(DATA[i - 3 : i])
            priority_sum += LETTER_NUM_MAPPING[common_letter.lower()]

    return str(priority_sum)
