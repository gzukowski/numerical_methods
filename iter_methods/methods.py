from math import *
from matrix import Matrix
from typing import List
import time

INDEX = 193184
N = 984

E = 1
F = 3
A1 = 5 + E
A2 = -1
A3 = -1

MAX_RES_NORM = 1e-9


def exerciseA() -> tuple:
    matrix = Matrix(N)
    matrix.fill_matrix(A1, A2, A3)

    b = [sin(element*(F+1)) for element in range(N)]
    x = [1 for element in range(N)]

    return matrix, b, x

def exerciseB(A : Matrix, b : List[float], x: List[float]):
    start = time.time()
    x_new, iterations, res = jacobi_method(A, b, x)
    end = time.time()
    
    return x_new, iterations, res, end - start

def exerciseC():
    pass

def exerciseD():
    pass

def exerciseE():
    pass

def residual(A: Matrix, b: List[float], x: List[float]) -> List[float]:
    r = A * x

    for i in range(len(b)):
        r[i] -= b[i]

    return r

def euclidean_norm(v: List[float]) -> float:
    n = 0
    
    for element in v:
        n += element ** 2

    return sqrt(n)

def jacobi_method(A : Matrix, b : list, x : list) -> tuple:
    n = len(b)
    x_new = x[:]
    iterations = 0
    res = 0

    while True:
        x_old = x_new[:]
        
        for i in range(n):
            sigma = 0.0
            for j in range(n):
                if j != i:
                    sigma += A.matrix[i][j] * x_old[j]
            
            x_new[i] = (b[i] - sigma) / A.matrix[i][i]
        
        iterations += 1

        res = residual(A, b, x_new)
        if euclidean_norm(res) < MAX_RES_NORM:
            break

    return x_new, iterations, res 



