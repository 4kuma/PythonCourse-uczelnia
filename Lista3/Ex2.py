l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]


def flatten(input_list):
    for element in input_list:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element


print(list(flatten(l)))
