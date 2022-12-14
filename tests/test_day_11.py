from src.day11 import MonkeyFactory, _get_items_inspected

TEST_INPUT = [
    "Monkey 0:",
    "  Starting items: 79, 98",
    "  Operation: new = old * 19",
    "  Test: divisible by 23",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "  Starting items: 54, 65, 75, 74",
    "  Operation: new = old + 6",
    "  Test: divisible by 19",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "  Starting items: 79, 60, 97",
    "  Operation: new = old * old",
    "  Test: divisible by 13",
    "    If true: throw to monkey 1",
    "    If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "  Starting items: 74",
    "  Operation: new = old + 3",
    "  Test: divisible by 17",
    "    If true: throw to monkey 0",
    "    If false: throw to monkey 1",
]


def test_simulate_part_a():

    monkeys = MonkeyFactory.generate_monkey_barrel(TEST_INPUT)

    for _ in range(20):
        for i in range(len(monkeys)):
            monkeys[i].round(monkeys, decrease_worry_level=True)

    items_inspected = _get_items_inspected(monkeys)

    assert items_inspected == [101, 95, 7, 105]

    items_inspected.sort(reverse=True)
    monkey_business = items_inspected[0] * items_inspected[1]

    assert monkey_business == 10605


def test_simulate_part_b():

    monkeys = MonkeyFactory.generate_monkey_barrel(TEST_INPUT)

    for round in range(1, 10000 + 1):

        for i in range(len(monkeys)):
            monkeys[i].round(monkeys, decrease_worry_level=False)

        match round:
            case 1:
                assert _get_items_inspected(monkeys) == [2, 4, 3, 6]

            case 20:
                assert _get_items_inspected(monkeys) == [99, 97, 8, 103]

            case 1000:
                assert _get_items_inspected(monkeys) == [5204, 4792, 199, 5192]

    items_inspected = _get_items_inspected(monkeys)
    items_inspected.sort(reverse=True)
    monkey_business = items_inspected[0] * items_inspected[1]

    assert monkey_business == 2713310158
