import sys
from aocd import submit

from main import run_part_a, run_part_b


def submit_part_a():
    submit(run_part_a(), part="a", day=3, year=2022)
    print("Part A submitted successfully")


def submit_part_b():
    submit(run_part_b(), part="b", day=3, year=2022)
    print("Part B submitted successfully")


if __name__ == "__main__":
    part = sys.argv[1]

    match part.lower():
        case "a":
            submit_part_a()
        case "b":
            submit_part_b()
        case other:
            raise RuntimeError(f"Invalid part argument: {part}")
