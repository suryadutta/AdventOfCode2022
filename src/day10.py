from src.utils import get_data
from typing import Iterator, List


def get_cycle_results(instructions: Iterator[str]):
    register = 1
    cycle_counter = []

    while True:
        instruction: str
        try:
            instruction = next(instructions)
        except StopIteration:
            break

        cycle_counter.append(register)

        if "noop" in instruction:
            pass

        elif "addx" in instruction:
            add_value = int(instruction.split(" ")[1])
            # simulate extra cycle
            cycle_counter.append(register)
            register += add_value

    return cycle_counter


def generate_sprite_results(cycle_registers: List[int]):
    results = []
    current_row: str = ""

    for i, register in enumerate(cycle_registers):
        pixel_location = i % 40
        sprite_position = register

        if (
            pixel_location >= sprite_position - 1
            and pixel_location <= sprite_position + 1
        ):
            current_row += "#"
        else:
            current_row += "."

        if len(current_row) == 40:
            results.append(current_row)
            current_row = ""

    return results


def run_part_a() -> str:
    instruction_generator = (n for n in get_data())
    cycle_register_values = get_cycle_results(instruction_generator)
    cycles_to_calculate = [20, 60, 100, 140, 180, 220]
    total_signal_strength = sum(
        [cycle * cycle_register_values[cycle - 1] for cycle in cycles_to_calculate]
    )
    return str(total_signal_strength)


def run_part_b() -> str:
    instruction_generator = (n for n in get_data())
    cycle_register_values = get_cycle_results(instruction_generator)
    sprite_display = generate_sprite_results(cycle_register_values)
    return "\n" + "\n".join(sprite_display)
