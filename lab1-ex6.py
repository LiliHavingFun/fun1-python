def convert_to_lowercase(text):
    if not text:
        return ""

    # Worrying about iterator invalidation and did not find a "replace" method that
    # accepts a lambda or a map...
    # So, we'll use a temporary
    returnedString = ""

    copy_from_pos = 0
    if text[0].isupper():
        returnedString = text[0].lower()
        copy_from_pos = 1

    start_pos = copy_from_pos
    for char in text[start_pos:]:
        if char.isupper():
            returnedString


    text[1:].replace()

print( convert_to_lowercase("UpperCamelCase") )