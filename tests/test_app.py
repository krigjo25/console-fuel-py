#   Importing responsories
import pytest
from app import convert



def test_Convert():

    #  Testing the convertion of the fraction to percentage
    assert convert("1/100") == "E"
    assert convert("50/100") == "50%"
    assert convert("99/100") == "F"


#   Raises an ZeroDivisionError when the denominator is 0
def test_raiseZeroDivisionError():
    with pytest.raises(ZeroDivisionError) as e:

        assert convert("1/0") == e


#   Raises an ValueError when the input is not a fraction
def test_raiseValueError():

    with pytest.raises(ValueError) as e:

        assert convert("a/b") == e

    with pytest.raises(Exception) as e:

        assert convert("2/1") == e
        assert convert("200/1") == e
