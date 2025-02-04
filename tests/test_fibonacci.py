## This is the test file where we testify about how our tests went! :)

from app.fibonacci import *
import pytest

#meep = "Meep"

def test_fib():
    assert fib(0) == 0

def test_fib_type_error():
    with pytest.raises(TypeError):
        fib(1.5)

#def meeptime():
#    assert meep == "Meep"

def test_fib_value_error():
    with pytest.raises(ValueError):
        fib(-1)