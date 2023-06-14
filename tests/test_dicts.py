from utils import dicts
import pytest

def test_get_val():
    assert dicts.get_val({1: 'green', 2: 'black', 3: 'pink'}, 2) == 'black'
    assert dicts.get_val({}, 2) == 'git'
    assert dicts.get_val({1: 'green', 2: 'black', 3: 'pink'}, 4) == 'git'
