"""practice creating functions based around lists"""

__author__ = "730550999"


def only_evens(input: list[int]) -> list[int]:
    index: int = 0
    output: list[int] = []
    while index < len(input):
        if input[index] % 2 == 0:
            output.append(input[index])
            index += 1
        else:
            index += 1
    return output


def sub(input: list[int], start: int, end: int) -> list[int]:
    index: int = 0
    output: list[int] = []
    while index < len(input):
        if index < start:
            index += 1
        elif index == end:
            index += 1
        else:
            output.append(input[index])
            index += 1
    return output


def add_at_index(input: list[int], num1: int, num2: int) -> None:
    if num2 < 0:
        raise IndexError("Index is out of bounds for the input list")
    elif num2 > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    for value in range(len(input) - 1, num2, -1):
        input[value] = input[value - 1]
    input[num2] = num1
