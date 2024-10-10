"""implementing algorithims and understand behaviours of common functions"""

__author__ = "730550999"


def all(listy: list[int], num: int) -> bool:
    index: int = 0
    value: int = 0  # makes easier to write the situation
    if len(listy) == 0:
        return False
    while index < len(listy):
        if num == listy[index]:
            value += 1
            index += 1
        else:
            index += 1
    if value == len(listy):
        return True
    else:
        return False


def max(listy2: list[int]) -> int:
    if len(listy2) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # put as very first line otherwise error doesn't show up
    index: int = 0  # after error line to ensure error comes out
    value: int = listy2[index]
    while index < len(listy2):
        if value < listy2[index]:
            value = listy2[index]
            index += 1
        else:
            index += 1
    return value


def is_equal(listy3: list[int], listy4: list[int]) -> bool:
    if len(listy3) != len(listy4):
        return False
    index: int = 0
    value: int = 0
    """assuming lists are equal, deep equality"""
    while index < len(listy3):
        if listy3[index] == listy4[index]:
            value += 1
            index += 1
        else:
            index += 1
    if value == len(listy3):
        return True
    else:
        return False


def extend(listy5: list[int], listy6: list[int]) -> None:
    index: int = 0
    while index < len(
        listy6
    ):  # use a while loop to do it individually because a list can't be appeneded
        listy5.append(listy6[index])
        index += 1
