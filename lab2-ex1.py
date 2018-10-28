from math import sqrt

# Based on: http://mathworld.wolfram.com/FibonacciNumber.html
# The closed form(check point 5)
def fib(number):
    return ( (1 + sqrt(5))**number - (1 - sqrt(5))**number) / (2**number * sqrt(5) )

def fib_list(number):
    list = []
    for n in range(0, number):
        list.append(fib(n))

    return list

print(fib_list(10))
