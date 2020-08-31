def subsets_comprehension(l):
    if len(l) == 0:
        return [[]]
    else:
        head, tail = l[0], l[1:]
        return subsets_comprehension(tail) + [[head, *i] for i in subsets_comprehension(tail)]


def subsets_map(l):
    if len(l) == 0:
        return [[]]
    else:
        head, tail = l[0], l[1:]
        return subsets_map(tail) + list(map(lambda i: [head, *i], subsets_map(tail)))

print(subsets_comprehension([1,2,3]))
