from pytest import approx
temperature = 20

def print_temperature():
    print(temperature)

def add(a, b):
    return a + b

def test_add():
    assert add(2.0, 3.0) == approx(5.0)
