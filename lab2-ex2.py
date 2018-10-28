from math import sqrt

def is_prime(number):
    if (number < 2):
        return False

    for i in range( 2, int(sqrt(number)) + 1 ):
        if number % i == 0:
            return False

    return True

def get_prime_numbers(list):
    returned_list = []

    for number in list:
        if is_prime(number):
            returned_list.append(number)

    return returned_list

print( get_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) )
