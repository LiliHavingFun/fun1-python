from sys import argv, stderr
import os

if len(argv) != 2:
    print("The script receive a path from the command line", file=stderr)
    exit(1)

if not os.path.exists(argv[1]):
    print("The argument is not a path:", argv[1], file=stderr)
    exit(1)

path = os.path.abspath(argv[1])
if os.path.isfile(path):
    print(path[:4096])
elif os.path.isdir(path):
    for entry in os.scandir(path):
        print(entry.path)
else:
    print("The passed path is not a file nor a directory", file=stderr)
    exit(1)
