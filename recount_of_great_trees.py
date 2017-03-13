import matrix
import sys

graph = [i.rstrip('\n') for i in sys.stdin.readlines()]
graph = [i.split() for i in graph]
graph = [[int(j) for j in i] for i in graph]

#graph = [[0, 1, 0, 1],
 #        [0, 0, 1, 1],
 #        [0, 1, 0, 1],
   #      [0, 0, 1, 0]]

transpose_graph = list(zip(*graph))
count_of_occurrences = [sum(i) for i in transpose_graph]

for i, j in enumerate(transpose_graph):
    if sum(j) == 0:
        root_of_great_tree = i


matrix_of_occurrences = [[] for i in graph]


for i in range(len(graph)):
    for j in range(len(graph)):
        if i == j:
            matrix_of_occurrences[i].append(count_of_occurrences[i])
        else:
            matrix_of_occurrences[i].append(0)

matrix_difference = matrix.subtract(matrix_of_occurrences, graph)

matrix_difference.pop(root_of_great_tree)
minor_root = list(zip(*matrix_difference))
minor_root.pop(root_of_great_tree)
minor_root = list(zip(*minor_root))
minor_root = [[j for j in i] for i in minor_root]

print(minor_root)


print("Det = ", matrix.determinant(minor_root))