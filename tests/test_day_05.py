from src.day05 import CrateStack, MoveInstruction, generate_stacks_from_crate_diagram, parse_instruction_step


def test_cratestack():

    stack = CrateStack()

    stack.add("a")
    stack.add("b")
    stack.add("c")

    assert len(stack.crates) == 3
    assert stack.crates[0] == "a"
    assert stack.crates[1] == "b"
    assert stack.crates[2] == "c"

    assert stack.get_top_crate() == "c"


def test_cratemover_single_crates():


def test_generate_stacks_from_crate_diagram():

    test_diagram = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 "
    ]

    stacks = generate_stacks_from_crate_diagram(test_diagram)

    assert len(stacks) == 3
    assert stacks[1].crates == ["Z", "N"]
    assert stacks[2].crates == ["M", "C", "D"]
    assert stacks[3].crates == ["P"]


def test_parse_instruction_step():

    test_instruction = "move 101 from 12345 to 123456789"
    instruction = parse_instruction_step(test_instruction)
    assert instruction.num_crates_to_move == 101
    assert instruction.from_stack_index == 12345
    assert instruction.to_stack_index == 123456789
