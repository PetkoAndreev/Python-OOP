class store_results:
    log_file_path = './results.txt '

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # args_str = ', '.join(args)
        # kwargs_str = ', '.join(f'{key}={value}' for (key, value) in kwargs.items())
        result = self.func(*args, **kwargs)
        with open(self.log_file_path, 'a') as file:
            file.write(f'Function {self.func.__name__} was called. Result: {result}\n')
            # Function {func_name} was add called. Result: {func_result}"
        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

# Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24
