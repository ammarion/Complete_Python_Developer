"""test."""


def do_stuff(num=0):
    """test."""
    try:
        if num:
            return int(num) + 100
        else:
            return "Please enter  a number"
    except ValueError as e:
        return e
