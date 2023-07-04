#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    return np.matmul(m_a, m_b)
