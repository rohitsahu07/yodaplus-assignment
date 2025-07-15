import pytest
from src.range_expander import expand_range

def test_basic_range_expansion():
    assert expand_range("1-3") == [1, 2, 3]
    assert expand_range("5") == [5]
    assert expand_range("1-2,4") == [1, 2, 4]

def test_whitespace_and_empty():
    assert expand_range(" , 1-3 , ,5 ") == [1, 2, 3, 5]
    assert expand_range("1, ,3-4,,") == [1, 3, 4]

def test_custom_delimiters():
    assert expand_range("1..3") == [1, 2, 3]
    assert expand_range("4~6") == [4, 5, 6]
    assert expand_range("10 to 12") == [10, 11, 12]
    assert expand_range("1-2,3..5,7~9") == [1, 2, 3, 4, 5, 7, 8, 9]

def test_reversed_and_single_point_ranges():
    assert expand_range("5-3") == [5, 4, 3]
    assert expand_range("3-3") == [3]
    assert expand_range("10..8,3 to 3") == [10, 9, 8, 3]

def test_invalid_input():
    with pytest.raises(ValueError):
        expand_range("3-a")
    with pytest.raises(ValueError):
        expand_range("1-2,a-5")