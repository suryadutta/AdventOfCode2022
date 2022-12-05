from src.utils import get_data
from dataclasses import dataclass, field
import re
from typing import List, Dict


@dataclass
class CrateStack:

    # first element is bottom of crate stack
    crates: List[str] = field(default_factory=list)

    def add(self, crate: str) -> None:
        # adds to top of stack
        self.crates.append(crate)

    def remove_n(self, num: int) -> List[str]:
        elements_removed = self.crates[-num:]
        del self.crates[-num:]
        return elements_removed

    def get_top_crate(self) -> str:
        return self.crates[-1]


@dataclass
class MoveInstruction:
    num_crates_to_move: int
    from_stack_index: int
    to_stack_index: int


class CrateMover:
    def __init__(self, can_move_multiple_crates_at_once: bool):
        self.can_move_multiple_crates_at_once = can_move_multiple_crates_at_once

    def move_crates(
        self, from_stack: CrateStack, to_stack: CrateStack, num_to_move: int
    ) -> None:

        crates_removed = from_stack.remove_n(num_to_move)

        if self.can_move_multiple_crates_at_once:
            for crate in crates_removed:
                to_stack.add(crate)

        else:
            # add in reverse order of removal
            for crate in reversed(crates_removed):
                to_stack.add(crate)


def generate_stacks_from_crate_diagram(diagram: List[str]) -> Dict[int, "CrateStack"]:

    # flip the diagram to make it easier to build crate stacks
    diagram.reverse()

    num_stacks = int(max(set(diagram[0])))
    indices = range(1, num_stacks + 1)

    stacks: Dict[int, CrateStack] = {i: CrateStack() for i in indices}

    for row in diagram[1:]:
        for i in indices:
            crate = row[4 * i - 3]
            if crate != " ":
                stacks[i].add(crate)

    return stacks


def parse_instruction_step(step: str) -> MoveInstruction:
    result = re.search(
        r"move\s(?P<num>\d+)\sfrom\s(?P<from_crate>\d+)\sto\s(?P<to_crate>\d+)", step
    )

    assert result is not None

    return MoveInstruction(
        num_crates_to_move=int(result.group("num")),
        from_stack_index=int(result.group("from_crate")),
        to_stack_index=int(result.group("to_crate")),
    )


def run_part_a() -> str:

    raw_data = get_data()

    split_index = raw_data.index("")

    crates_diagram = raw_data[:split_index]
    instructions = raw_data[split_index + 1 :]
    mover = CrateMover(can_move_multiple_crates_at_once=False)

    stacks: Dict[int, CrateStack] = generate_stacks_from_crate_diagram(crates_diagram)
    for step in instructions:
        instruction = parse_instruction_step(step)

        mover.move_crates(
            from_stack=stacks[instruction.from_stack_index],
            to_stack=stacks[instruction.to_stack_index],
            num_to_move=instruction.num_crates_to_move,
        )

    top_crates = [stack.get_top_crate() for stack in stacks.values()]

    return "".join(top_crates)


def run_part_b() -> str:
    raw_data = get_data()

    split_index = raw_data.index("")

    crates_diagram = raw_data[:split_index]
    instructions = raw_data[split_index + 1 :]
    mover = CrateMover(can_move_multiple_crates_at_once=True)

    stacks: Dict[int, CrateStack] = generate_stacks_from_crate_diagram(crates_diagram)
    for step in instructions:
        instruction = parse_instruction_step(step)

        mover.move_crates(
            from_stack=stacks[instruction.from_stack_index],
            to_stack=stacks[instruction.to_stack_index],
            num_to_move=instruction.num_crates_to_move,
        )

    top_crates = [stack.get_top_crate() for stack in stacks.values()]

    return "".join(top_crates)
