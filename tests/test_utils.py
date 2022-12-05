from src.utils import recursively_split_line_with_delimiters


def test_recursively_split_line_with_delimiters():

    test_line_to_split = "a,b:c,d,e"
    test_delimiters = [":", ","]

    test_split = recursively_split_line_with_delimiters(
        line=test_line_to_split, delimiters=test_delimiters
    )

    assert len(test_split) == 2
    assert len(test_split[0]) == 2
    assert len(test_split[1]) == 3

    assert test_split[0][0] == "a"
    assert test_split[0][1] == "b"
    assert test_split[1][0] == "c"
    assert test_split[1][1] == "d"
    assert test_split[1][2] == "e"
