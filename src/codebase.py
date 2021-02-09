"""A set of dummy functions to test a continous integration pipeline."""


VALID_TYPES = (complex, float, int, str)


def addition(a: complex, b: complex) -> complex:
    """Add two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result adding `a` and `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"'a' must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a + b


def subtract(a: complex, b: complex) -> complex:
    """Subtract two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result subtracting `b` from `a`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a - b


def multiply(a: complex, b: complex) -> complex:
    """Multiply two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result multiplying `a` and `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a * b


def divide(a: complex, b: complex) -> complex:
    """Divide two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result diving `a` by `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    ZeroDivisionError
        if `b` is `0`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a / b
