def matrix_transpozition(matrix):
    return [' '.join([i.split(' ')[matrix[0].split(' ').index(element)] for i in matrix])
            for element in matrix[
                0].split(' ')]


print(matrix_transpozition(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))
