from random import sample, randrange, choice

counter = 0
used_indexes = []


def generate_tree(height):
    if height == 0:
        return None

    global used_indexes

    max_nodes = 2 ** height
    min_nodes = 2 ** (height - 1)
    no_of_nodes = randrange(min_nodes, max_nodes)
    used_indexes += sample(range(no_of_nodes + 1), no_of_nodes + 1)
    ind = used_indexes[0]
    used_indexes.pop(0)
    subtree1 = generate_subtree(height - 1)
    subtree2 = generate_subtree(height - 1)

    if choice([True, False]):
        return [ind, subtree1, subtree2]
    return [ind, subtree2, subtree1]


def generate_subtree(height):
    if height == 0 or (len(used_indexes) == 0 and height == 1):
        return None
    ind = used_indexes[0]
    used_indexes.pop(0)
    return [ind, generate_subtree(height - 1), generate_subtree(height - 1)]


def dfs(tree):
    if tree == None:
        return
    yield tree[0]
    yield from dfs(tree[1])
    yield from dfs(tree[2])


def bfs(tree):
    if tree == None:
        return
    current_level = tree
    next_level = tree
    while len(next_level) > 0:
        next_level = []
        for element in current_level:
            if isinstance(element, list):
                for e in element:
                    next_level.append(e)
            elif element != None:
                yield element
        current_level = next_level


if __name__ == '__main__':
    some_tree = generate_tree(3)
    print(some_tree)
    print(list(dfs(some_tree)))
    print(list(bfs(some_tree)))
