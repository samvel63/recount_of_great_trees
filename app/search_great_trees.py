import itertools

'''capacity_great_trees = 2
graph = [[0, 1, 1],
        [0, 0, 1],
        [0, 1, 0]]
n = len(graph)
root = 0'''


def search_great_trees(n, root, graph, capacity_great_trees):
    transpose_graph = list(zip(*graph))
    null_list = [0 for i in range(n)]

    list_options = [[] for i in range(n)]

    for l, k in enumerate(transpose_graph):
        for q, w in enumerate(k):
            if w == 1:
                tmp_matrix = null_list[:]
                tmp_matrix[q] = 1
                list_options[l].append(tmp_matrix[:])
        if l == root:
            list_options[l].append(null_list[:])

    list_options = list(itertools.product(*list_options))
    list_options = [list(i) for i in list_options]
    list_options = [list(zip(*i)) for i in list_options]
    list_options = [[list(j) for j in i] for i in list_options]
    # print(list_options)


    list_of_great_trees = []

    for lst in list_options:
        if capacity_great_trees == len(list_of_great_trees):
            break
        g = lst[:]
        ex = set()  # множество посещенных вершин

        def dfs(node):  # start - начальная вершина
            ex.add(node)
            for i in range(len(g)):
                if g[node][i] == 1 and i not in ex:
                    dfs(i)

        dfs(root)
        # print(ex)
        if len(ex) == n:
            list_of_great_trees.append(lst)

    print(list_of_great_trees)
    return list_of_great_trees