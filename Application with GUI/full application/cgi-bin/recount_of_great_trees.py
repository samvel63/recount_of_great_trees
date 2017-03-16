import matrix
def recount(g, n):

    transpose_graph = list(zip(*g))
    count_of_occurrences = [sum(i) for i in transpose_graph]

    for i, j in enumerate(transpose_graph):
        if sum(j) == 0:
            root_of_great_tree = i


    matrix_of_occurrences = [[] for i in g]

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_of_occurrences[i].append(count_of_occurrences[i])
            else:
                matrix_of_occurrences[i].append(0)

    matrix_difference = matrix.subtract(matrix_of_occurrences, g)

    minor_root = matrix.find_minor(matrix_difference, root_of_great_tree)

    return int(matrix.determinant(minor_root))

#print("Number Of Great Trees = ", int(matrix.determinant(minor_root)))