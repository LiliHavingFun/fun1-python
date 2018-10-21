import re


def count_words(string):
    if not string:
        return 0

    try:
        split_words = re.compile('[\s,;?!.]*').split(string)
    except:
        print("Could not split the string")
        return 0

    words_count = 0
    for word in split_words:
        words_count += 1

    return words_count


word_count = count_words("Hello over there, how are you doing? Indeed! You; are doing well. Hey.")
print(word_count)
