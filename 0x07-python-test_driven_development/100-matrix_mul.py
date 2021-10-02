#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    x = []
    y = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if all(isinstance(n, (int, float)) for r in m_a for n in r) is False:
        raise TypeError("m_a should contain only integers or floats")
    if all(isinstance(n, (int, float)) for r in m_b for n in r) is False:
        raise TypeError("m_b should contain only integers or floats")
    if len(set([len(row) for row in m_a])) is not 1:
        raise TypeError("each row of m_a must should be of the same size")
    if len(set([len(row) for row in m_b])) is not 1:
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        """iterate through columns of Y"""
        for j in range(len(m_b[0])):
            """iterate through rows of Y"""
            sum = 0
            for k in range(len(m_b)):
                sum = sum + (m_a[i][k] * m_b[k][j])
            x.append(sum)
        y.append(x)
        x = []
    return y
