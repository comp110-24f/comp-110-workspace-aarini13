from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest

"""practice testing functions in edge and use cases"""

__author__ = "730550999"


def test_only_evens_use1() -> None:
    b: list[int] = [1, 2, 3]
    assert only_evens(b) == [2]


def test_only_evens_use2() -> None:
    b: list[int] = [1, 2, 3]
    only_evens(b)
    assert b == [1, 2, 3]


def test_only_evens_edge() -> None:
    b: list[int] = [1, 5, 3]
    assert only_evens(b) == []


def test_sub_use1() -> None:
    b: list[int] = [10, 20, 30, 40]
    assert sub(b, 1, 3) == [20, 30]


def test_sub_use2() -> None:
    b: list[int] = [10, 20, 30, 40]
    sub(b, 1, 3)
    assert b == [10, 20, 30, 40]


def test_sub_edge() -> None:
    b: list[int] = []
    assert sub(b, 1, 3) == []


def test_add_at_index_use1() -> None:
    b: list[int] = [1, 2, 3, 5]
    add_at_index(b, 4, 3)
    assert b == [1, 2, 3, 4, 5]


def test_add_at_index_use2() -> None:
    b: list[int] = [1]
    add_at_index(b, 2, 1)
    assert b == [1, 2]


def test_add_to_index_edge() -> None:
    b: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(b, 1, 1)
