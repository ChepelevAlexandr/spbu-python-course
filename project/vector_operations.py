import math
from typing import List


def scalar(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the scalar product of two vectors.

    Parameters:
    ----------
    v1 : List[float]
        The first input vector.
    v2 : List[float]
        The second input vector.

    Returns:
    -------
    float
        The scalar product of the vectors.

    Raises:
    ------
    ValueError
        If the lengths of the vectors are not equal.
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the vectors must match.")

    return sum(x * y for x, y in zip(v1, v2))


def length(v: List[float]) -> float:
    """
    Calculate the length (magnitude) of a vector.

    Parameters:
    ----------
    v : List[float]
        The vector.

    Returns:
    -------
    float
        The length of the vector.

    Raises:
    ------
    Exceptions:
    ValueError: If the vector is empty.
    """
    if not v:
        raise ValueError("The vector must not be empty.")

    return math.sqrt(scalar(v, v))


def angle(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the angle between two vectors.

    Parameters:
    ----------
    v1 : List[float]
        The first vector.
    v2 : List[float]
        The second vector.

    Returns:
    -------
    float
        The angle between the vectors in radians.

    Raises:
    ------
    ValueError: If the length of either vector is zero.

    """
    length_v1 = length(v1)
    length_v2 = length(v2)

    if length_v1 == 0 or length_v2 == 0:
        raise ValueError(
            "The length of one of the vectors is zero, the angle cannot be determined."
        )

    # Scalar multiply
    dot_product = scalar(v1, v2)
    cos_angle = dot_product / (length_v1 * length_v2)
    cos_angle = max(-1.0, min(1.0, cos_angle))

    return math.acos(cos_angle)
