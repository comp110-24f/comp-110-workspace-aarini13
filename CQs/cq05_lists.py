"""Mutating functions."""

__author__ = "730550999"


def manual_append(lister: list[int], num: int) -> None:
    lister.append(num)


def double(listy: list[int]) -> None:
    indexing: int = 0
    while indexing < len(listy):
        listy[indexing] *= 2
        indexing += 1


list1: list[int] = [1, 2, 3]
list2: list[int] = list1
double(listy=list2)
print(list1)
print(list2)
