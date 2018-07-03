import pytest
from tutoring import simple_exercises


def test_identity():
    assert 1 == simple_exercises.identity(1)
    assert True is simple_exercises.identity(True)


def test_sign():
    assert simple_exercises.sign(2) == "positive"
    assert simple_exercises.sign(-1) == "negative"
    assert simple_exercises.sign(0) == "zero"
    with pytest.raises(TypeError):
        simple_exercises.sign("Hello World")
