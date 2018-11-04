def get_sets(list_a, list_b):
    """
    Returns a tuple of A^B, A | B, A - B, B - A
    """
    set_a = set(list_a)
    set_b = set(list_b)
    return (
        set_a.intersection(set_b),
        set_a.union(set_b),
        set_a.difference(set_b),
        set_b.difference(set_a)
    )


print(get_sets([1, 2, 3], [2, 3, 4]))
