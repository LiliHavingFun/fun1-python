import re

def contains_special_characters(string):
    if not string:
        return False

    found = re.findall('[\r\t\n\a\b\f\v]+', string)

    if not found:
        return False
    else:
        return True


print(contains_special_characters("Hello\tWorld"))
