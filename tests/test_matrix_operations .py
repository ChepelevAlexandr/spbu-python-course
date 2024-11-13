
import pytest

import math

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from project.matrix_operations import matrix_add, matrix_mul, matrix_trans


def test_matrix_add():
    # The normal case
    assert matrix_add([[2, 3], [4, 5]], [[6, 7], [8, 9]]) == [[8, 10], [12, 14]]

    # Addition with a zero matrix
    assert matrix_add([[2, 3], [4, 5]], [[0, 0], [0, 0]]) == [[2, 3], [4, 5]]

    # Addition with negative nums
    assert matrix_add([[-2, -3], [-4, -5]], [[6, 7], [8, 9]]) == [[4, 4], [4, 4]]

    # Boundary case: empty matrices
    assert matrix_add([], []) == []

    # Exception: size mismatch
    with pytest.raises(ValueError):
        matrix_add([[2]], [[2, 3]])


def test_matrix_mul():
    # The normal case (square matrices)
    assert matrix_mul([[2, 3], [4, 5]], [[6, 7], [8, 9]]) == [[36, 41], [64, 73]]

    # Multiplication by a single matrix (identity)
    assert matrix_mul([[2, 3], [4, 5]], [[1, 0], [0, 1]]) == [[2, 3], [4, 5]]

    # Multiplication with a zero matrix
    assert matrix_mul([[2, 3]], [[0], [0]]) == [[0]]

     # Test with non-square matrices (2x3 and 3x2)
    assert matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [
        [58, 64],
        [139, 154],
    ]

    # Test with non-square matrices (3x2 and 2x3)
    assert matrix_mul([[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10]]) == [
        [25, 28],
        [57, 64],
        [89, 100],
    ]

    # Boundary case: empty matrices
    assert matrix_mul([], []) == []

    # Exception: size mismatch
    with pytest.raises(ValueError):
        matrix_mul([[2]], [[3], [4]])


def test_matrix_trans():
    # The normal case
    assert matrix_trans([[2, 3, 4], [5, 6, 7]]) == [[2, 5], [3, 6], [4, 7]]

    # Transposing a square matrix
    assert matrix_trans([[2, 3], [4, 5]]) == [[2, 4], [3, 5]]

    # Transposing a matrix with a single row
    assert matrix_trans([[2, 3]]) == [[2], [3]]

    # Transposing a matrix with one column
    assert matrix_trans([[2], [3]]) == [[2, 3]]

    # Boundary case: an empty matrix
    assert matrix_trans([]) == []