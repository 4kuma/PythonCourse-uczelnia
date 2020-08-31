def qsort_list_comprehension(l):
    if len(l) < 2:
        return l
    pivot, rest = l[0], l[1:]
    return qsort_list_comprehension([i for i in rest if i < pivot]) + [pivot] + qsort_list_comprehension(
        [i for i in rest if i >= pivot])


def qsort_filter(l):
    if len(l) < 2:
        return l
    pivot, rest = l[0], l[1:]
    return qsort_list_comprehension(list(filter(lambda i: i < pivot, rest))) + [pivot] + qsort_list_comprehension(
        list(filter(lambda i: i >= pivot, rest)))


print(qsort_list_comprehension([3, 4, 1, 7]))
print(qsort_filter([3, 4, 1, 7]))
