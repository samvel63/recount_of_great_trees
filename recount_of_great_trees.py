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

transpose_graph.pop(0)
#g = list(zip(*transpose_graph)).pop(0)
#print(matrix_of_occurrences)
#print(root_of_great_tree)