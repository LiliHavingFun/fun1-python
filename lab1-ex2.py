def isVowel(char):
    char = char.lower()
    if (   char == 'a'
        or char == 'e'
        or char == 'i'
        or char == 'o'
        or char == 'u'):
        return True
    else:
        return False

def countVowels(string):
    vowels = 0

    # should move the .map
    for i in string:
        if isVowel(i):
            vowels += 1

    return vowels

print(countVowels("There you go"))
