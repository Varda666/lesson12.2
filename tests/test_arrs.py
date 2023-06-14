from utils import arrs
import pytest


@pytest.fixture
def array():
    return [1, 2, 3, 4]

def test_get(array):
    assert arrs.get(array, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"

def test_get_index_error(array):
    with pytest.raises(IndexError):
        arrs.get(array, 4)


def test_slice(array):
    assert arrs.my_slice(array, 1, 3) == [2, 3]
    assert arrs.my_slice(array, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(array, -4) == [1, 2, 3, 4]
    assert arrs.my_slice(array, -2) == [3, 4]
