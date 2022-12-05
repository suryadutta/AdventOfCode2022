from aocd import get_data
import logging
import sys
import string

logger = logging.getLogger("advent_of_code_2022_day_3")
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger.setLevel(logging.INFO)

DATA = get_data(day=3, year=2022).splitlines()

LETTER_NUM_MAPPING = {
    letter: i + 1
    for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


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


if __name__ == "__main__":

    try:
        logger.info(f"Part A Answer: {run_part_a()}")
    except NotImplementedError:
        logger.error("Part A not started yet")

    try:
        logger.info(f"Part B Answer: {run_part_b()}")
    except NotImplementedError:
        logger.error("Part B not started yet")
