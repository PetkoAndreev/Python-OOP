import functools


def cache(func):
    # internal_cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args[0] # args + tuple(kwargs.values())
        # if cache_key not in internal_cache:
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func(*args) # func(*args, **kwargs)
            # internal_cache[cache_key] = func(*args,  **kwargs)
        return wrapper.log[cache_key]
        # return   internal_cache[cache_key]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
# {1: 1, 0: 0, 2: 1, 3: 2}

fibonacci(4)
print(fibonacci.log)
# {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}

# test first zero
import unittest


class CacheTests(unittest.TestCase):
    def test_zero_first(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        fibonacci(3)
        self.assertEqual(fibonacci.log, {1: 1, 0: 0, 2: 1, 3: 2})


if __name__ == '__main__':
    unittest.main()
