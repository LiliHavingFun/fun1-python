import re


def occurence(search_this_string, in_this_string):
    return in_this_string.count(search_this_string)


print(occurence("hello", "hello hellohelloworld")) # 3
