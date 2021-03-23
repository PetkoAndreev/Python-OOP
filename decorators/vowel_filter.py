def vowel_filter(func):
    vowels = set('aeiuo' + 'aeiuo'.upper())

    def wrapper():
        result = func()
        return [ch for ch in result if ch in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
