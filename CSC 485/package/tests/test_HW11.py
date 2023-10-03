from package.projects.HW11 import get_formal_name
import pytest

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_apple():
    assert get_formal_name('apple') == ('Malus domestica')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_banana():
    assert get_formal_name('banana') == ('Musa acuminata')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_orange():
    assert get_formal_name('orange') == ('Citrus × sinensis')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_strawberry():
    assert get_formal_name('strawberry') == ('Fragaria × ananassa')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_grape():
    assert get_formal_name('grape') == ('Vitis vinifera')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_pineapple():
    assert get_formal_name('pineapple') == ('Ananas comosus')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_mango():
    assert get_formal_name('mango') == ('Mangifera indica')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_blueberry():
    assert get_formal_name('blueberry') == ('Vaccinium corymbosum')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_peach():
    assert get_formal_name('peach') == ('Prunus persica')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_watermelon():
    assert get_formal_name('watermelon') == ('Citrullus lanatus')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_cherry():
    assert get_formal_name('cherry') == ('Prunus avium')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_pear():
    assert get_formal_name('pear') == ('Pyrus')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_plum():
    assert get_formal_name('plum') == ('Prunus domestica')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_raspberry():
    assert get_formal_name('raspberry') == ('Rubus idaeus')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_kiwi():
    assert get_formal_name('kiwi') == ('Actinidia deliciosa')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_lemon():
    assert get_formal_name('lemon') == ('Citrus limon')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_avocado():
    assert get_formal_name('avocado') == ('Persea americana')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_pomegranate():
    assert get_formal_name('pomegranate') == ('Punica granatum')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_cranberry():
    assert get_formal_name('cranberry') == ('Vaccinium macrocarpon')

"""Test to ensure that the correct key returns the correct value"""
def test_fruit_key_grapefruit():
    assert get_formal_name('grapefruit') == ('Citrus × paradisi')

"""Test that if more than one positional arguements are given it will result in a TypeError"""
def test_multiple_arguments():
    with pytest.raises(Exception) as e:
        get_formal_name(('apple') == ('Malus domestica'), ('banana') == ('Musa acuminata'))
    assert e.type == TypeError

"""Test that a positional argument(key) being given that is not in the dictionary will return a KeyError"""
def test_key_error():
    with pytest.raises(Exception) as e:
        get_formal_name('blackberry') == ('Rubus fruticosus')
    assert e.type == KeyError

"""Test that a positional argument(key) will only return it's assigned value and not another value in the dictionary"""
def test_key_does_not_equal():
    assert get_formal_name('apple') != ('Musa acuminata')
