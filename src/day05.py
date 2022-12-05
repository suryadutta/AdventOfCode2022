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

    def move_n_to_other_stack(self, num: int, other_stack: "CrateStack"):
        for crate in self.remove_n(num):
            other_stack.add(crate)


@dataclass
class MoveInstruction:
    num_crates_to_move: int
    from_stack_index: int
    to_stack_index: int


def generate_stacks_from_crate_diagram(diagram: List[str]) -> Dict[int, "CrateStack"]:

    # flip the diagram to make it easier to build crate stacks
    diagram.reverse()

    num_stacks = int(max(set(diagram[0])))
    indices = range(1, num_stacks + 1)

    stacks: Dict["CrateStack"] = {i: CrateStack() for i in indices}

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
    return MoveInstruction(
        num_crates_to_move=int(result.group("num")),
        from_stack_index=int(result.group("from_crate")),
        to_stack_index=int(result.group("to_crate")),
    )


def run_part_a() -> str:

    raw_data = get_data()

    split_index = raw_data.index("")

    crates_diagram = raw_data[:split_index]
    instructions = raw_data[split_index + 1:]

    crates: Dict[int, CrateStack] = generate_stacks_from_crate_diagram(crates_diagram)
    for step in instructions:
        instruction = parse_instruction_step(step)
        crates[instruction.from_stack_index].move_n_to_other_stack(
            num=instruction.num_crates_to_move,
            other_stack=crates[instruction.to_stack_index],
        )

    top_crates = [stack.get_top_crate() for stack in crates.values()]

    return "".join(top_crates)


def run_part_b() -> str:

    raise NotImplementedError
