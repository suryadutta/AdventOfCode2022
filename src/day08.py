from src.utils import get_data
import numpy as np
from typing import List


def parse_matrix(data: List[str]):
    return np.array([list(line) for line in data]).astype(int)


def get_visible_trees(matrix: np.typing.NDArray):

    visible_tree_indices = set()

    n_rows, n_columns = np.shape(matrix)

    def _get_visible_tree_coords(arr: np.typing.NDArray):
        visible_indices = []
        max_height_found = -1
        for i in range(arr.shape[0]):
            if arr[i] > max_height_found:
                max_height_found = arr[i]
                visible_indices.append(i)

        return visible_indices

    for column_index in range(n_columns):

        column_to_analyze = matrix[:, column_index]

        # iterate over columns top_down
        for visible_row_index in _get_visible_tree_coords(arr=column_to_analyze):
            visible_tree_indices.add((visible_row_index, column_index))

        # iterate over columns top_down
        for visible_row_index in _get_visible_tree_coords(
            arr=np.flip(column_to_analyze)
        ):
            visible_tree_indices.add((n_rows - 1 - visible_row_index, column_index))

    for row_index in range(n_rows):

        row_to_analyze = matrix[row_index, :]

        # iterate over row left-right
        for visible_column_index in _get_visible_tree_coords(arr=row_to_analyze):
            visible_tree_indices.add((row_index, visible_column_index))

        # iterate over columns top_down
        for visible_column_index in _get_visible_tree_coords(
            arr=np.flip(row_to_analyze)
        ):
            visible_tree_indices.add((row_index, n_columns - 1 - visible_column_index))

    return visible_tree_indices


def get_directional_scenic_score(tree_height: int, view: np.typing.NDArray):
    score = np.argwhere(view >= tree_height)
    if len(score) == 0:
        return len(view)
    return score[0][0] + 1


def get_scenic_score_for_tree(
    matrix: np.typing.NDArray, row_index: int, col_index: int
) -> int:
    n_rows, n_columns = np.shape(matrix)
    tree_height = matrix[row_index, col_index]

    up_scenic_score: int
    if row_index == 0:
        up_scenic_score = 0
    else:
        up_scenic_score = get_directional_scenic_score(
            tree_height=tree_height, view=np.flip(matrix[:row_index, col_index])
        )

    down_scenic_score: int
    if row_index == n_rows - 1:
        down_scenic_score = 0
    else:
        down_scenic_score = get_directional_scenic_score(
            tree_height=tree_height, view=matrix[row_index + 1 :, col_index]
        )

    left_scenic_score: int
    if col_index == 0:
        left_scenic_score = 0
    else:
        left_scenic_score = get_directional_scenic_score(
            tree_height=tree_height, view=np.flip(matrix[row_index, :col_index])
        )

    right_scenic_score: int
    if col_index == n_columns - 1:
        right_scenic_score = 0
    else:
        right_scenic_score = get_directional_scenic_score(
            tree_height=tree_height, view=matrix[row_index, col_index + 1 :]
        )

    total_scenic_score = np.prod(
        [up_scenic_score, down_scenic_score, left_scenic_score, right_scenic_score]
    )
    return int(total_scenic_score)


def get_max_scenic_score_for_tree(matrix: np.typing.NDArray) -> int:

    max_scenic_score = 0
    n_rows, n_columns = np.shape(matrix)
    for row_index in range(n_rows):
        for col_index in range(n_columns):
            total_scenic_score = get_scenic_score_for_tree(matrix, row_index, col_index)
            if total_scenic_score > max_scenic_score:
                max_scenic_score = total_scenic_score

    return max_scenic_score


def run_part_a() -> str:
    forest = parse_matrix(get_data())
    return str(len(get_visible_trees(forest)))


def run_part_b() -> str:
    forest = parse_matrix(get_data())
    return str(get_max_scenic_score_for_tree(forest))
