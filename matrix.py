def subtract(matrix1, matrix2):
    final_matrix = []
    for i in range(len(matrix1)):
        final_matrix.append([matrix1[i][j] - matrix2[i][j] for j in range(len(matrix2))])
    return final_matrix

def determinant(matrix):
    n = len(matrix)
    label = False

    for j in range(n):
        if matrix[j][j] == 0:
            line = j
            for i in range(j + 1, n):
                if matrix[i][j] != 0:
                    line = i
                    break

            if line == j:
                label = True
                break
            else:
                for q in range(j, n):
                    tmp = matrix[j][q]
                    matrix[j][q] = matrix[line][q]
                    matrix[l][q] = tmp
        p = matrix[j][j]

        for i in range(j + 1, n):
            k = matrix[i][j] / p
            for q in range(j, n):
                matrix[i][q] -= k * matrix[j][q]

    det = 0
    if not label:
        det = 1
        for i in range(n):
            det *= matrix[i][i]
    return det