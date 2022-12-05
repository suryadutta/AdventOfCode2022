import importlib
import logging
import os
import sys

DAY = int(os.environ["AOC_DAY"])
YEAR = 2022

logger = logging.getLogger(f"advent_of_code_2022_day_{DAY}")
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger.setLevel(logging.INFO)


def run_code():

    answers_module = importlib.import_module(f"src.day{DAY:02d}")

    run_part_a = getattr(answers_module, "run_part_a")
    try:
        logger.info(f"Part A Answer: {run_part_a()}")
    except NotImplementedError:
        logger.error("Part A not started yet")

    run_part_b = getattr(answers_module, "run_part_b")
    try:
        logger.info(f"Part B Answer: {run_part_b()}")
    except NotImplementedError:
        logger.error("Part B not started yet")


if __name__ == "__main__":
    run_code()
