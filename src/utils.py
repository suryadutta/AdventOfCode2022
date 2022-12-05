import os
from typing import List


def get_data() -> List[str]:

    day = int(os.environ["AOC_DAY"])
    year = int(os.environ["AOC_YEAR"])

    import aocd
    return aocd.get_data(day=day, year=year).splitlines()


def recursively_split_line_with_delimiters(line: str, delimiters: List[str]):
    def _recursively_split(arr, split_delims: List[str]):
        split_val = [val.split(split_delims[0]) for val in arr]

        if len(split_delims) == 1:
            return split_val

        return [_recursively_split(val, split_delims[1:]) for val in split_val]

    return _recursively_split([line], delimiters)[0]
