import pytest

def func(x):
    return x *2

def test_method1():
    assert func(2) == 4

def test_method2():
    assert func(3) == 6

def test_method3():
    assert func(4) == 7