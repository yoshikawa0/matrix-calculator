
import unittest
from calculator import MatrixCalculator

class TestMatrixCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = MatrixCalculator()

    def test_add_matrices(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        result = self.calculator.add_matrices(matrix_a, matrix_b)
        self.assertEqual(result, [[6, 8], [10, 12]])

    def test_multiply_matrices(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        result = self.calculator.multiply_matrices(matrix_a, matrix_b)
        self.assertEqual(result, [[19, 22], [43, 50]])

    def test_transpose_matrix(self):
        matrix_a = [[1, 2], [3, 4]]
        result = self.calculator.transpose_matrix(matrix_a)
        self.assertEqual(result, [[1, 3], [2, 4]])

if __name__ == "__main__":
    unittest.main()
