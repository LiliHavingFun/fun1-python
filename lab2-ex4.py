def a_and_b(list_a, list_b):
    intersection = []

    for a in list_a:
        for b in list_b:
            if a == b:
                # Looks extremely inefficient
                if a not in intersection:
                    intersection.append(a)

    return intersection


def a_or_b(list_a, list_b):
    for b in list_b:
        # Again, inefficient, need better data structures
        if b not in list_a:
            list_a.append(b)

    return list_a


def a_minus_b(list_a, list_b):
    for b in list_b:
        if b in list_a:
            list_a.remove(b)

    return list_a


def b_minus_a(list_a, list_b):
    return a_minus_b(list_b, list_a)


print(   a_and_b([1, 2, 3], [2, 3, 4]) )
print(    a_or_b([1, 2, 3], [2, 3, 4]) )
print( a_minus_b([1, 2, 3], [2, 3, 4]) )
print( b_minus_a([1, 2, 3], [2, 3, 4]) )
