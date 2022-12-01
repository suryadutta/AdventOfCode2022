from aocd import get_data
import logging
import sys


logger = logging.getLogger("advent_of_code_2022_day_1")
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger.setLevel(logging.INFO)


def run_part_a() -> str:
    data = get_data(day=1, year=2022).splitlines()

    top_calorie_count = 0

    calorie_count = 0
    for line in data:
        if line == "":
            if calorie_count > top_calorie_count:
                top_calorie_count = calorie_count
            calorie_count = 0
            continue
        calorie_count += int(line)

    return str(top_calorie_count)


def run_part_b() -> str:
    data = get_data(day=1, year=2022).splitlines()

    top_three_calorie_counts = [0, 0, 0]

    calorie_count = 0

    for line in data:
        if line == "":
            if calorie_count > top_three_calorie_counts[0]:
                top_three_calorie_counts.pop(0)
                top_three_calorie_counts.append(calorie_count)
                top_three_calorie_counts.sort()
            calorie_count = 0
            continue
        calorie_count += int(line)

    return str(sum(top_three_calorie_counts))


if __name__ == "__main__":

    try:
        logger.info(f"Part A Answer: {run_part_a()}")
    except NotImplementedError:
        logger.error("Part A not started yet")

    try:
        logger.info(f"Part B Answer: {run_part_b()}")
    except NotImplementedError:
        logger.error("Part B not started yet")
