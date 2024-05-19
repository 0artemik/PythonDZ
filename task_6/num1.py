import math
import pytest



def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)
def test_average_num_with_integers():
    assert average_num([1, 2, 3, 4, 5]) == 3

def test_average_num_with_floats():
    assert average_num([1.0, 2.5, 3.0, 4.5]) == 2.75

def test_average_num_with_mixed_numbers():
    assert average_num([1, 2.5, '3', 4.0]) == 2.62

def test_average_num_with_non_convertible_string():
    assert average_num([1, 2, 'abc']) == "Bad request"

def test_average_num_with_empty_list():
    assert average_num([]) == "Bad request"

def test_average_num_with_single_element():
    assert average_num([5]) == 5

def test_average_num_with_large_numbers():
    assert average_num([1000000, 2000000, 3000000]) == 2000000

def test_average_num_with_boolean():
    assert average_num([1, True, 3]) == "Bad request"
