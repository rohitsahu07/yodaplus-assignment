import pytest
from src.range_expander import expand_range

def test_basic_range_expansion():
    assert expand_range("1-3") == [1, 2, 3]
    assert expand_range("5") == [5]
    assert expand_range("1-2,4") == [1, 2, 4]