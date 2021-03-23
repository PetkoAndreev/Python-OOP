import functools


def logged(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'you called {func.__name__}{args}\nit returned {result}'

        return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

'''
you called func(4, 4, 4)
it returned 6
you called sum_func(1, 4)
it returned 5
'''

# test zero
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

if __name__ == '__main__':
    unittest.main()
