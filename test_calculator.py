from calculator import add, substract ,divide

import pytest

def test_add():
    assert add(2,3) == 5


def test_substract():
    assert substract(5,3) == 2



def test_divide():
    assert divide(10,2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)
    
    
    
