

import pytest

# Test cases go here.


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    # s.split should throw when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)


def test_yeet():
    assert yeet() == 50


def test_addition():
    assert addition(5, 10) == 15


pytest.main()

# Rest goes here.


def yeet():
    return 50


def addition(a, b):
    return a + b


print("Test cases completed!")
