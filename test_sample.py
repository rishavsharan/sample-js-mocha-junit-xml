# content of test_sample.py
def func(x):
    return x + 1

def test_01():
    assert func(3) == 4

def test_02():
    assert func(4) == 5

def test_03():
    assert func(3) == 6

def test_04():
    assert func(3) == 7

def test_05():
    assert func(3) == 8