from random import randrange, sample, choice

used_indexes = []


class Node(object):
    children = []
    visited = False

    def __init__(self, index, children):
        self.index = index
        self.children = children

    def __str__(self):
        if len(self.children) > 0:
            return f'{self.index}{[str(c) for c in self.children]}'
        else:
            return f'{self.index}'


def generate_tree(height):
    if height == 0:
        return None
    if height == 1:
        return Node(1, [])

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
        return Node(ind, [subtree1, subtree2])
    return Node(ind, [subtree2, subtree1])


def generate_subtree(height):
    if (len(used_indexes) > 0):
        ind = used_indexes[0]
        used_indexes.pop(0)
        if height == 1:
            return Node(ind, [])
        subtree1 = generate_subtree(height - 1)
        subtree2 = generate_subtree(height - 1)
        return Node(ind, [subtree1, subtree2])
    else:
        return


def bfs(root):
    cur_level = [root]
    while len(cur_level) > 0:
        next_level = []
        for node in cur_level:
            if node is not None:
                yield node.index
                if len(node.children) > 0:
                    next_level += node.children
        cur_level = next_level


def dfs(root):
    if root is None:
        return
    yield root.index
    for c in root.children:
        yield from dfs(c)


if __name__ == '__main__':
    some_tree = generate_tree(3)
    print(some_tree)
    print(list(dfs(some_tree)))
    print(list(bfs(some_tree)))
