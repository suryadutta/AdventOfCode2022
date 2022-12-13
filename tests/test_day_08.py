import numpy as np
from src.day08 import (
    get_visible_trees,
    get_directional_scenic_score,
    get_scenic_score_for_tree,
    get_max_scenic_score_for_tree,
)

TEST_MATRIX = np.array(
    [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
)


def test_get_visible_trees():

    visible_trees = get_visible_trees(TEST_MATRIX)

    assert len(visible_trees) == 21

    n_rows, n_columns = np.shape(TEST_MATRIX)

    for i in range(n_rows):
        assert (i, 0) in visible_trees

    for i in range(n_columns):
        assert (0, i) in visible_trees

    assert (1, 1) in visible_trees
    assert (1, 2) in visible_trees
    assert (2, 1) in visible_trees
    assert (2, 3) in visible_trees
    assert (3, 2) in visible_trees


def test_get_directional_scenic_score():
    assert get_directional_scenic_score(tree_height=5, view=np.array([4, 3, 2, 1])) == 4
    assert get_directional_scenic_score(tree_height=5, view=np.array([4, 3, 2, 5])) == 4
    assert get_directional_scenic_score(tree_height=5, view=np.array([4, 3, 5, 4])) == 3
    assert get_directional_scenic_score(tree_height=5, view=np.array([6, 3, 5, 4])) == 1


def test_get_scenic_score_for_tree():
    assert get_scenic_score_for_tree(TEST_MATRIX, row_index=1, col_index=2) == 4
    assert get_scenic_score_for_tree(TEST_MATRIX, row_index=3, col_index=2) == 8


def test_get_max_scenic_score_for_tree():
    assert get_max_scenic_score_for_tree(TEST_MATRIX) == 8
