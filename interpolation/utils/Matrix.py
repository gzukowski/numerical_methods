from typing import List
from math import *
import copy

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
      
      def fill_identity(self):
            N = self.rows
            for i in range(N):
                  self.matrix[i][i] = 1




def residual(A: Matrix, b: List[float], x: List[float]) -> List[float]:
      r = A * x

      for i in range(b.rows):
            r.matrix[i][0] -= b.matrix[i][0]

      return r

def euclidean_norm(v: List[float]) -> float:
      sigma = 0
      
      was_calculated = True

      try:
            for element in v.matrix:
                  sigma += element[0] ** 2

      except OverflowError:
            was_calculated = False



      return sqrt(sigma), was_calculated


def LU_decomposition(A : Matrix, b : Matrix, x : Matrix):
      U = copy.deepcopy(A)
      L = Matrix(A.rows, A.rows)
      L.fill_identity()
      n = U.rows
      x_new = copy.deepcopy(x)
      
      for i in range(2, n+1):
            for j in range(1,i):
                  L.matrix[i-1][j-1] = U.matrix[i-1][j-1] / U.matrix[j-1][j-1]
                  
                  for l in range(n):
                        U.matrix[i-1][l] = U.matrix[i-1][l] - L.matrix[i-1][j-1] * U.matrix[j-1][l]


      y = [0 for element in range(n)]


      for i in range(n):
            sigma = 0
            
            for j in range(i):
                  sigma += L.matrix[i][j] * y[j]

            y[i] = (b.matrix[i][0] - sigma) / L.matrix[i][i]

      for i in range(n - 1, -1, -1):
            sigma = 0
            
            for j in range(i + 1, n):
                  sigma += U.matrix[i][j] * x_new.matrix[j][0]

            x_new.matrix[i][0] = (y[i] - sigma) / U.matrix[i][i]

      res = residual(A, b, x_new)

      norm, was_calculated = euclidean_norm(res)

      x_new = [round(x[0], 10) for x in x_new.matrix]

      return x_new, norm


