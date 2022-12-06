import pytest

from src.day06 import (
    get_first_marker
)

@pytest.mark.parametrize("data, marker_length, expected", [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26)
])
def test_get_first_marker(data, marker_length, expected):
    assert get_first_marker(data, marker_length) == expected
