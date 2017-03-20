import numpy as np
from math import sqrt

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

def recount(lin_matrix):

    n = int(sqrt(len(lin_matrix)))
    g = [[0 for j in range(n)] for i in range(n)] 
    g = [lin_matrix[i:i+n] for i in range(0, len(lin_matrix), n)] #One-dimensional list in two-dimensional

    transpose_graph = list(zip(*g))
    count_of_occurrences = [sum(i) for i in transpose_graph]

    root_of_great_tree = [i for i, j in enumerate(transpose_graph) if sum(j) == 0]

    matrix_of_occurrences = [[] for i in g]
    matrix_of_occurrences = np.ndarray.tolist(np.diag(count_of_occurrences))

    matrix_difference = matrix_subtraction(matrix_of_occurrences, g)

    minor_root = find_minor(matrix_difference, root_of_great_tree[0])

    return int(np.linalg.det(minor_root))

#print("Number Of Great Trees = ", int(matrix.determinant(minor_root)))