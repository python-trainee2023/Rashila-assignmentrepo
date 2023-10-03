import pytest

def func(x):
    return x+3

def test_method1():
    assert func(3)==6

@pytest.mark.xfail
def test_method2():
    assert func(2)==7

@pytest.mark.skip
def test_method3():
    assert func(4) == 5

@pytest.mark.custom
def test_method4():
    assert func(5) == 8