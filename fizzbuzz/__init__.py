def fizzbuzz_convert(number):
    if number % 3 and 5 == 0:
        return 'Fizzbuzz'

    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return str(number)
assert fizzbuzz_convert(3) == 'Fizz'
