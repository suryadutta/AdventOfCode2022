from src.utils import get_data
from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Iterator, List, Set, Tuple


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


@dataclass
class MoveInstruction:
    direction: Direction
    steps: int


@dataclass(frozen=True)
class Location:
    x: int = field(default=0)
    y: int = field(default=0)

    def get_diff(self, other_location: "Location") -> Tuple[int, int]:
        return other_location.x - self.x, other_location.y - self.y

    def is_touching(self, other_location: "Location"):
        diff = self.get_diff(other_location)
        return abs(diff[0]) <= 1 and abs(diff[1]) <= 1


@dataclass
class RopeElement:
    location: Location = field(default_factory=Location)

    def move_direction(self, direction: Direction):

        match direction:
            case Direction.RIGHT:
                self.location = replace(self.location, x=self.location.x + 1)

            case Direction.LEFT:
                self.location = replace(self.location, x=self.location.x - 1)

            case Direction.UP:
                self.location = replace(self.location, y=self.location.y + 1)

            case Direction.DOWN:
                self.location = replace(self.location, y=self.location.y - 1)


def get_tail_locations_from_instructions(
    instructions: Iterator[MoveInstruction], rope: List[RopeElement]
) -> Set[Location]:

    head = rope[0]
    tail = rope[-1]

    tail_locations: Set[Location] = {tail.location}

    for instruction in instructions:
        for _ in range(instruction.steps):

            head.move_direction(instruction.direction)

            for i in range(1, len(rope)):
                if not rope[i].location.is_touching(rope[i - 1].location):

                    x_diff, y_diff = rope[i].location.get_diff(rope[i - 1].location)

                    if y_diff > 0:
                        rope[i].move_direction(Direction.UP)
                    elif y_diff < 0:
                        rope[i].move_direction(Direction.DOWN)

                    if x_diff > 0:
                        rope[i].move_direction(Direction.RIGHT)
                    elif x_diff < 0:
                        rope[i].move_direction(Direction.LEFT)

                    assert rope[i].location.is_touching(rope[i - 1].location)

            tail_locations.add(tail.location)

    return tail_locations


def parse_instructions(line) -> MoveInstruction:

    instructions_raw = line.split(" ")

    instruction = MoveInstruction(
        direction=Direction(instructions_raw[0]), steps=int(instructions_raw[1])
    )

    return instruction


def run_part_a() -> str:
    data = get_data()

    tail_locations = get_tail_locations_from_instructions(
        instructions=(parse_instructions(line) for line in data),
        rope=[RopeElement() for _ in range(2)],
    )

    return str(len(tail_locations))


def run_part_b() -> str:
    data = get_data()

    tail_locations = get_tail_locations_from_instructions(
        instructions=(parse_instructions(line) for line in data),
        rope=[RopeElement() for _ in range(10)],
    )

    return str(len(tail_locations))
