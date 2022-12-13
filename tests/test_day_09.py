from src.day09 import (
    Direction,
    Location,
    RopeElement,
    parse_instructions,
    get_tail_locations_from_instructions,
)


def test_location_touching():
    assert Location(0, 0).is_touching(Location(0, 0))
    assert Location(0, 0).is_touching(Location(0, 1))
    assert Location(0, 0).is_touching(Location(1, 0))
    assert Location(0, 0).is_touching(Location(1, 1))
    assert not Location(0, 0).is_touching(Location(1, 2))


def test_move_rope_element():
    test_rope_element = RopeElement(location=Location(x=1, y=2))

    test_rope_element.move_direction(direction=Direction.RIGHT)
    assert test_rope_element.location == Location(x=2, y=2)

    test_rope_element.move_direction(direction=Direction.UP)
    assert test_rope_element.location == Location(x=2, y=3)

    test_rope_element.move_direction(direction=Direction.LEFT)
    assert test_rope_element.location == Location(x=1, y=3)

    test_rope_element.move_direction(direction=Direction.DOWN)
    assert test_rope_element.location == Location(x=1, y=2)


def test_get_tail_locations_from_instructions_length_two():

    test_lines = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    test_instructions = (parse_instructions(line) for line in test_lines)

    tail_locations = get_tail_locations_from_instructions(
        test_instructions, rope=[RopeElement() for _ in range(2)]
    )

    expected_tail_locations = {
        Location(*raw_location)
        for raw_location in [
            (0, 0),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (2, 4),
            (3, 0),
            (3, 2),
            (3, 3),
            (3, 4),
            (4, 1),
            (4, 2),
            (4, 3),
        ]
    }

    assert tail_locations == expected_tail_locations


def test_get_tail_locations_from_instructions_length_ten():

    test_lines = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
    test_instructions = (parse_instructions(line) for line in test_lines)

    test_rope = [RopeElement() for _ in range(10)]
    tail_locations = get_tail_locations_from_instructions(
        test_instructions, rope=test_rope
    )

    expected_tail_locations = {
        Location(*raw_location)
        for raw_location in [
            (0, 0),
            (1, 1),
            (2, 2),
            (1, 3),
            (2, 4),
            (3, 5),
            (4, 5),
            (5, 5),
            (6, 4),
            (7, 3),
            (8, 2),
            (9, 1),
            (10, 0),
            (9, -1),
            (8, -2),
            (7, -3),
            (6, -4),
            (5, -5),
            (4, -5),
            (3, -5),
            (2, -5),
            (1, -5),
            (0, -5),
            (-1, -5),
            (-2, -5),
            (-3, -4),
            (-4, -3),
            (-5, -2),
            (-6, -1),
            (-7, 0),
            (-8, 1),
            (-9, 2),
            (-10, 3),
            (-11, 4),
            (-11, 5),
            (-11, 6),
        ]
    }

    assert tail_locations == expected_tail_locations
