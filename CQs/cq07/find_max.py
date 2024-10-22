"""list practice"""

__author__ = "730550999"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index: int = 0
    value: int = input[index]
    for value in range(0, len(input)):
        if value < input[index]:
            value = input[index]
            index += 1
        else:
            index += 1
    index = 0
    while index < len(input):
        if value == input[index]:
            input.pop(index)
            index += 1
        else:
            index += 1
    return value
