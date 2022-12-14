from src.utils import get_data
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple
import numpy as np
import numpy.typing as npt


@dataclass
class Monkey:
    items: npt.NDArray
    divisibility_test: int
    operation: Callable
    true_monkey_index: int
    false_monkey_index: int

    items_inspected: int = field(default=0, init=False)

    def round(self, all_monkeys: Dict[int, "Monkey"], decrease_worry_level: bool):

        if len(self.items) > 0:
            new_worry_levels = self.operation(self.items)
            self.items_inspected += len(self.items)
            self.items = np.array([])

            if decrease_worry_level:
                new_worry_levels = np.floor(np.divide(new_worry_levels, 3))

            divisible_indices = np.where(new_worry_levels % self.divisibility_test == 0)
            true_worry_levels = new_worry_levels[divisible_indices]
            false_worry_levels = np.delete(new_worry_levels, divisible_indices)

            all_monkeys[self.true_monkey_index].add_items(true_worry_levels)
            all_monkeys[self.false_monkey_index].add_items(false_worry_levels)

    def add_items(self, items: npt.NDArray):
        self.items = np.append(self.items, items)


def _get_items_inspected(monkeys: Dict[int, Monkey]):
    return [monkey.items_inspected for monkey in monkeys.values()]


class MonkeyFactory:
    @staticmethod
    def _generate_monkey(lines: List[str]) -> Tuple[int, Monkey]:

        monkey_index = int(lines[0].lstrip().split(" ")[1].split(":")[0])

        monkey_items = [
            int(value) for value in lines[1].lstrip().split(":")[1].split(",")
        ]
        monkey_operation = lambda old: eval(lines[2].lstrip().split("= ")[1])
        monkey_divisibility_test = int(lines[3].lstrip().split(" ")[-1])
        true_monkey_index = int(lines[4].lstrip().split(" ")[-1])
        false_monkey_index = int(lines[5].lstrip().split(" ")[-1])

        new_monkey = Monkey(
            items=np.array(monkey_items).astype(int),
            divisibility_test=monkey_divisibility_test,
            operation=np.vectorize(monkey_operation),
            true_monkey_index=true_monkey_index,
            false_monkey_index=false_monkey_index,
        )

        return monkey_index, new_monkey

    @staticmethod
    def generate_monkey_barrel(lines) -> Dict[int, Monkey]:
        barrel = {}

        instruction_accum: List[str] = []
        for line in lines:
            if line == "":
                monkey_index, new_monkey = MonkeyFactory._generate_monkey(
                    instruction_accum
                )
                barrel[monkey_index] = new_monkey
                instruction_accum = []
            else:
                instruction_accum.append(line)

        if len(instruction_accum) > 0:
            monkey_index, new_monkey = MonkeyFactory._generate_monkey(instruction_accum)
            barrel[monkey_index] = new_monkey

        return barrel


def run_part_a() -> str:
    data = get_data()
    monkeys = MonkeyFactory.generate_monkey_barrel(data)

    for _ in range(20):
        for i in range(len(monkeys)):
            monkeys[i].round(monkeys, decrease_worry_level=True)

    items_inspected = _get_items_inspected(monkeys)
    items_inspected.sort(reverse=True)
    monkey_business = items_inspected[0] * items_inspected[1]

    return str(monkey_business)


def run_part_b() -> str:
    data = get_data()
    monkeys = MonkeyFactory.generate_monkey_barrel(data)

    for _ in range(10000):
        for i in range(len(monkeys)):
            monkeys[i].round(monkeys, decrease_worry_level=True)

    items_inspected = _get_items_inspected(monkeys)
    items_inspected.sort(reverse=True)
    monkey_business = items_inspected[0] * items_inspected[1]

    return str(monkey_business)
