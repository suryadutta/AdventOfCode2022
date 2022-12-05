from src.day05 import CrateStack


def test_split_equal_string():

    test_string = "abcdef"
    test_split = split_equal_string(test_string)

    assert len(test_split) == 2
    assert test_split[0] == "abc"
    assert test_split[1] == "def"
