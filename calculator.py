
class MatrixCalculator:
    @staticmethod
    def add_matrices(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
        return result

    @staticmethod
    def transpose_matrix(matrix):
        return [list(row) for row in zip(*matrix)]


# Приклад використання
if __name__ == "__main__":
    calculator = MatrixCalculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    print("Addition:", calculator.add_matrices(matrix_a, matrix_b))
    print("Multiplication:", calculator.multiply_matrices(matrix_a, matrix_b))
    print("Transpose:", calculator.transpose_matrix(matrix_a))
