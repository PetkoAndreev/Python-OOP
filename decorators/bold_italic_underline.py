import functools


def make_bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = f'<b>{func(*args, **kwargs)}</b>'
        return result

    return wrapper


def make_italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = f'<i>{func(*args, **kwargs)}</i>'
        return result

    return wrapper


def make_underline(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = f'<u>{func(*args, **kwargs)}</u>'
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

# <b><i><u>Hello, Peter</u></i></b>


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

# <b><i><u>Hello, Peter, George</u></i></b>
