from typing import List

class Matrix:
      def __init__(self, rows : int, cols : int) -> None:
            self.rows = rows
            self.cols = cols
            self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
                  
     
      def __str__(self):
            matrix_str = ""
            for row in self.matrix:
                  matrix_str += " ".join(map(str, row)) + "\n"
            return matrix_str
      

      def __mul__(self, other: 'Matrix') -> 'Matrix':
            if self.cols != other.rows:
                  raise ValueError("You cant multiply these matrices.")

            result: Matrix = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                  for j in range(other.cols):
                        for k in range(self.cols):
                              result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
      
      def __add__(self, other: 'Matrix') -> 'Matrix':
            if self.rows != other.rows or self.cols != other.cols:
                  raise ValueError("Matrices must have the same dimensions for addition.")

            result: Matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                  for j in range(self.cols):
                        result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result

      def __sub__(self, other: 'Matrix') -> 'Matrix':
            if self.rows != other.rows or self.cols != other.cols:
                  raise ValueError("Matrices must have the same dimensions for subtraction.")

            result: Matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                  for j in range(self.cols):
                        result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result


