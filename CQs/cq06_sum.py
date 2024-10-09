"""Summing the elements of a list using different loops"""

__author__ = "730550999"


def w_sum(vals: list[float]) -> float:
    index: float = 0
    solution: float = 0
    while index < len(vals):
        solution += float(vals[index])
        index += 1
    return solution


def f_sum(vals: list[float]) -> float:
    solution: float = 0
    for value in vals:
        solution += float(value)
    return solution


def f_range_sum(vals: list[float]) -> float:
    solution: float = 0
    for value in range(0, len(vals)):
        solution += float(vals[value])
    return solution
