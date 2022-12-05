from dataclasses import dataclass
from typing import Tuple
from utils import get_data


DATA = get_data()


@dataclass
class AssignmentRange:
    start: int
    end: int

    def contains_number(self, num: int) -> bool:
        return self.start <= num <= self.end

    def contains_range(self, other_range: "AssignmentRange") -> bool:
        return other_range.start >= self.start and other_range.end <= self.end


def parse_raw_assignment_data_to_ranges(
    line: str,
) -> Tuple[AssignmentRange, AssignmentRange]:

    assignments = line.split(",")

    raw_first_range = assignments[0].split("-")
    first_range = AssignmentRange(
        start=int(raw_first_range[0]), end=int(raw_first_range[1])
    )

    raw_second_range = assignments[1].split("-")
    second_range = AssignmentRange(
        start=int(raw_second_range[0]), end=int(raw_second_range[1])
    )

    return first_range, second_range


def run_part_a() -> str:

    fully_contained_assignments = 0
    for line in DATA:
        first_range, second_range = parse_raw_assignment_data_to_ranges(line)
        if first_range.contains_range(second_range) or second_range.contains_range(
            first_range
        ):
            fully_contained_assignments += 1

    return str(fully_contained_assignments)


def run_part_b() -> str:

    overlapping_assignments = 0
    for line in DATA:
        first_range, second_range = parse_raw_assignment_data_to_ranges(line)
        if first_range.contains_number(
            second_range.start
        ) or second_range.contains_number(first_range.start):
            overlapping_assignments += 1

    return str(overlapping_assignments)
