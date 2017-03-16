import numpy as np

def find_minor(mat, k): # delete k-th column and row
    mat.pop(k)
    minor_root = list(zip(*mat))
    minor_root.pop(k)
    minor_root = list(zip(*minor_root))
    return [[j for j in i] for i in minor_root]

def matrix_subtraction(matrix1, matrix2):
    A, B = np.matrix(matrix1), np.matrix(matrix2)
    C = A - B
    return C.tolist()

def recount(g, n):

    transpose_graph = list(zip(*g))
    count_of_occurrences = [sum(i) for i in transpose_graph]

    root_of_great_tree = [i for i, j in enumerate(transpose_graph) if sum(j) == 0]

    matrix_of_occurrences = [[] for i in g]
    matrix_of_occurrences = np.ndarray.tolist(np.diag(count_of_occurrences))

    matrix_difference = matrix_subtraction(matrix_of_occurrences, g)

    minor_root = find_minor(matrix_difference, root_of_great_tree[0])

    return int(np.linalg.det(minor_root))

#print("Number Of Great Trees = ", int(matrix.determinant(minor_root)))