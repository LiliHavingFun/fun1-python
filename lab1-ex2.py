def is_vowel(char):
    char = char.lower()
    if (   char == 'a'
        or char == 'e'
        or char == 'i'
        or char == 'o'
        or char == 'u'):
        return True
    else:
        return False


def count_vowels(string):
    vowels = 0

    # should move the .map
    for i in string:
        if is_vowel(i):
            vowels += 1

    return vowels


print(count_vowels("There you go"))
