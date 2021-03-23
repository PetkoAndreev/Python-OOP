import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data_check = [num for num in args if type(num) == int and num % 2 == 0]
        if len(data_check) == len(args):
            return func(*args, **kwargs)
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

'''
6
Please use only even numbers!
'''
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
'''
384
Please use only even numbers!
'''
