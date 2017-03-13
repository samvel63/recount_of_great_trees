import matrix

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input().split()))
graph = [[int(i) for i in j] for j in graph]

transpose_graph = list(zip(*graph))
count_of_occurrences = [sum(i) for i in transpose_graph]

for i, j in enumerate(transpose_graph):
    if sum(j) == 0:
        root_of_great_tree = i


matrix_of_occurrences = [[] for i in graph]


for i in range(n):
    for j in range(n):
        if i == j:
            matrix_of_occurrences[i].append(count_of_occurrences[i])
        else:
            matrix_of_occurrences[i].append(0)

matrix_difference = matrix.subtract(matrix_of_occurrences, graph)

minor_root = matrix.find_minor(matrix_difference, root_of_great_tree)

print("Number Of Great Trees = ", int(matrix.determinant(minor_root)))