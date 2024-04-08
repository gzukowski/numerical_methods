from typing import List

class Matrix:
    def __init__(self, n : int) -> None:
        self.size= n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def fill_matrix(self, a1 : int, a2 : int, a3 : int):
        N = self.size
        for i in range(N):
            for j in range(N):
                if j == i:
                    self.matrix[i][j] = a1
                elif j == i - 1 or j == i + 1:
                    self.matrix[i][j] = a2
                elif j == i - 2 or j == i + 2:
                    self.matrix[i][j] = a3

    def __mul__(self, v : List[float]) -> List[float]:
        if len(v) != self.size:
            raise ValueError("Vector size must match matrix size")
        
        result = [0] * self.size

        for i in range(self.size):
            col_sum = 0
            for j in range(self.size):
                col_sum += self.matrix[i][j] * v[j]
            result[i] = col_sum

        return result
    
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str


        
