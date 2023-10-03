from csc485.csc485.projects.hw10.HW10 import is_it_a_fruit
import pytest

"""test_fruit_is_apple tests to see if 'apple' is in is_it_a_fruit"""
def test_fruit_is_apple():
    assert is_it_a_fruit('apple') == True

"""test_fruit_is_pear tests to see if 'pear' is in is_it_a_fruit"""
def test_fruit_is_pear():
    assert is_it_a_fruit('pear') == True

"""test_fruit_is_bananna tests to see if 'bananna' is in is_it_a_fruit"""
def test_fruit_is_bananna():
    assert is_it_a_fruit('bananna') == True

"""test_fruit_is_grape tests to see if 'grape' is in is_it_a_fruit"""
def test_fruit_is_grape():
    assert is_it_a_fruit('grape') == True

"""test_integer tests to make sure that there are no integers in is_it_a_fruit"""
def test_integer():
    assert is_it_a_fruit(5) == False

"""test_banana_spelling tests to make sure the correct spelling of banana will not return True"""
def test_banana_spelling():
    assert is_it_a_fruit('banana') == False

"""test_random_string tests to make sure a random input as a string will not return True"""
def test_random_string():
    assert is_it_a_fruit('wrench') == False

"""test_multiple_inputs tests to make sure that multiple inputs as strings will return with a TypeError"""
def test_multiple_inputs():
    with pytest.raises(Exception) as e:
        is_it_a_fruit('apple', 'pear')
    assert e.type == TypeError
