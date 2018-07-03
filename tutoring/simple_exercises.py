import numbers


def identity(x):
    return x


def sign(number: numbers.Real) -> str:
    """Determine the sign of a number

    Args:
        number: any real number

    Returns:
        A string describing the sign of the number
    """
    if number < 0:
        message = "negative"
    elif number == 0:
        message = "zero"
    elif number > 0:
        message = "positive"
    else:
        raise TypeError("number must be a number. got: {}".format(number))
    return message
