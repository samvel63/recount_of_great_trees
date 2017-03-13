def matrix_subtract(matrix1, matrix2):
    final_matrix = []
    for i in range(len(matrix1)):
        final_matrix.append([matrix1[i][j] - matrix2[i][j] for j in range(len(matrix2))])
    return final_matrix



graph = [[0, 1, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 0, 1],
         [0, 0, 0, 0]]

transpose_graph = list(zip(*graph))

for i, j in enumerate(transpose_graph):
    if sum(j) == 0:
        root_of_great_tree = i

count_of_occurrences = [sum(i) for i in transpose_graph]
matrix_of_occurrences = [[] for i in graph]


for i in range(len(graph)):
    for j in range(len(graph)):
        if i == j:
            matrix_of_occurrences[i].append(count_of_occurrences[i])
        else:
            matrix_of_occurrences[i].append(0)

print(matrix_subtract(matrix_of_occurrencesx, graph))
