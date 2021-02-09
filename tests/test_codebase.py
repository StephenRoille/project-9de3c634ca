import hypothesis.strategies as st
import pytest
import src
from hypothesis import given

# load hypothesis configuration
import config  # noqa:F401


def all_types():
    """All built-in types hypothesis knows."""
    return st.from_type(type).flatmap(st.from_type)


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_add(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.add(a, b)
    else:
        c = src.codebase.add(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_subtract(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.subtract(a, b)
    else:
        c = src.codebase.subtract(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_multiply(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.multiply(a, b)
    else:
        c = src.codebase.multiply(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_divide(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.divide(a, b)
    # b=0 should raise a ZeroDivisionError
    elif b == 0:
        with pytest.raises(ZeroDivisionError):
            src.codebase.divide(a, b)
    else:
        c = src.codebase.divide(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        else:
            assert type(c).__name__ == "float"
