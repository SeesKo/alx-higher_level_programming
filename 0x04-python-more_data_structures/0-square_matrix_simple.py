#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""

    # Creating new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in range(len(row))] for row in matrix]

    # Iterating thru each element in the matrix and computing its square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
