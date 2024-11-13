
from typing import List


def matrix_add(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices.

    Parameters:
    ----------
    A : List[List[float]]
        The first matrix.
    B : List[List[float]]
        The second matrix.

    Returns:
    -------
    List[List[float]]
        The resulting matrix after addition.

    Raises:
    ------
    ValueError
        If the matrices have different dimensions.
    """
    if len(m1) != len(m2) or any(len(row1) != len(row2) for row1, row2 in zip(m1, m2)):
        raise ValueError("Matrices have different dimensions!")

    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(m1, m2)]


def matrix_mul(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.

    Parameters:
    ----------
    A : List[List[float]]
        The first matrix.
    B : List[List[float]]
        The second matrix.

    Returns:
    -------
    List[List[float]]
        The resulting matrix after multiplication.

    Raises:
    ------
    ValueError
        If the number of columns in the first matrix does not match the number of rows in the second matrix
    """
    # Check for empty matrices
    if not m1 or not m2:
        return []

    # Check if the number of columns in the first matrix matches the number of rows in the second matrix
    if len(m1[0]) != len(m2):
        raise ValueError(
            "The number of columns of the first matrix must match the number of rows of the second matrix."
        )

    # Multiply the matrices
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*m2)] for row in m1]


def matrix_trans(m: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Parameters:
    ----------
    A : List[List[float]]
        The matrix to be transposed.

    Returns:
    -------
    List[List[float]]
        The transposed matrix.
    """
    return list(map(list, zip(*m)))
    
