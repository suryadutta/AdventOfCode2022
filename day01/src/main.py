import logging
import sys

# from aocd import get_data

logger = logging.getLogger("advent_of_code_2022_day_1")
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger.setLevel(logging.INFO)


def run_part_a() -> str:
    # data = get_data(day=1, year=2022)

    raise NotImplementedError


def run_part_b() -> str:

    # data = get_data(day=1, year=2022)

    raise NotImplementedError


if __name__ == "__main__":

    try:
        logger.info(f"Part A Answer: {run_part_a()}")
    except NotImplementedError:
        logger.error("Part A not started yet")

    try:
        logger.info(f"Part B Answer: {run_part_b()}")
    except NotImplementedError:
        logger.error("Part B not started yet")
