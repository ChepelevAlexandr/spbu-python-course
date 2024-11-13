
import pytest
import math

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from project.vector_operations import scalar, length, angle


def test_scalar():
    # The normal case
    assert scalar([2, 3, 4], [5, 6, 7]) == 56

    # Scalar product with a zero vector
    assert scalar([0, 0, 0], [2, 3, 4]) == 0

    # Scalar product with negative numbers
    assert scalar([-2, -3, -4], [5, 6, 7]) == -56

    # Boundary case: empty vectors
    assert scalar([], []) == 0

    # Exception: size mismatch
    with pytest.raises(ValueError):
        scalar([2], [2, 3])


def test_length():
    # The normal case
    assert length([6, 8]) == 10

    # The length of the zero vector
    assert length([0, 0]) == 0

    # The length of a vector with negative numbers
    assert length([-6, -8]) == 10

    # Boundary case: empty vector
    with pytest.raises(ValueError):
        length([])


def test_angle():
    # The normal case
    assert pytest.approx(angle([1, 1], [-1, -1])) == math.pi

    # The angle between the opposite vectors (must be π)
    assert pytest.approx(angle([2, 0], [-2, 0])) == math.pi

    # The angle between the zero vectors (undefined)
    with pytest.raises(ValueError):
        angle([0, 0], [1, 1])

    # The angle between the vector and the zero vector (undefined)
    with pytest.raises(ValueError):
        angle([2, 3], [0, 0])