from sys import argv, stderr

if len(argv) != 3:
    print("The script should be called with 2 parameters(numbers)", file=stderr)
    exit(1)

try:
    a = float(argv[1])
    b = float(argv[2])

    print("a - b: {}".format(a - b))
    print("a + b: {}".format(a + b))
    print("a / b: {}".format(a / b))
    print("a * b: {}".format(a * b))
except ValueError as err:
    print("Please make sure the arguments are numbers:", err, file=stderr)
    raise
except OverflowError as err:
    print("One of the operations(-,+,/,*) overflowed:", err, file=stderr)
    raise
except ZeroDivisionError as err:
    print("Please make sure the second argument is not zero:", err, file=stderr)
    raise
except ArithmeticError as err:
    print(err, file=stderr)
    raise
except Exception as err:
    print("Unexpected error:", err, file=stderr)
    raise
