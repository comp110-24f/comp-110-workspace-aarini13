from CQs.cq07.find_max import find_and_remove_max

"""understanding unit list functions"""
__author__ = "730550999"


def test_find_and_remove_max_use_case() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(b) == 10


def test_find_and_remove_max_list_use_case() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(b)
    assert b == [9, 8, 7]


def test_find_and_remove_max_edge_case() -> None:
    b: list[int] = []
    assert find_and_remove_max(b) == -1
