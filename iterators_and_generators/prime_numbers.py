def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(ll: list):
    for num in ll:
        if is_prime(num):
            yield num


'''
Create a generator function called get_primes() which should receive a list of integer numbers and 
return a list containing only the prime numbers from the initial list. You can learn more about prime numbers from here:
'''
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
