from math import *
from matrix import Matrix
from typing import List
import time
import matplotlib.pyplot as plt


INDEX = 193184
N = 984

E = 1
F = 3
A1A = 5 + E
A2A = -1
A3A = -1

A1C = 3
A2C = -1
A3C = -1

MAX_RES_NORM = 1e-9
MAX_ITERATIONS = 1000


def exerciseA() -> tuple:
    matrix = Matrix(N)
    matrix.fill_matrix(A1A, A2A, A3A)

    b = [sin(element*(F+1)) for element in range(N)]
    x = [1 for element in range(N)]

    return matrix, b, x

def exerciseB(A : Matrix, b : List[float], x: List[float]):

    start_jac = time.time()
    x_new_jac, iterations_jac, res_jac, converged_jac = jacobi_method(A, b, x)
    end_jac = time.time()

    start_gaus = time.time()
    x_new_gaus, iterations_gaus, res_gaus, converged_gaus = gauss_seidel_method(A, b, x)
    end_gaus = time.time()
    
    return (x_new_jac, iterations_jac, res_jac, end_jac - start_jac, converged_jac), \
        (x_new_gaus,iterations_gaus, res_gaus, end_gaus - start_gaus, converged_gaus)

def exerciseC():
    matrix = Matrix(N)
    matrix.fill_matrix(A1C, A2C, A3C)

    b = [sin(element*(F+1)) for element in range(N)]
    x = [1 for element in range(N)]


    start_jac = time.time()
    x_new_jac, iterations_jac, res_jac, converged_jac = jacobi_method(matrix, b, x)
    end_jac = time.time()

    start_gaus = time.time()
    x_new_gaus, iterations_gaus, res_gaus, converged_gaus = gauss_seidel_method(matrix, b, x)
    end_gaus = time.time()
    
    return (x_new_jac, iterations_jac, res_jac, end_jac - start_jac, converged_jac), \
        (x_new_gaus,iterations_gaus, res_gaus, end_gaus - start_gaus, converged_gaus)

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
    
    was_calculated = True

    try:
        for element in v:
            n += element ** 2

    except OverflowError:
        was_calculated = False



    return sqrt(n), was_calculated

def jacobi_method(A : Matrix, b : list, x : list) -> tuple:
    n = len(b)
    x_new = x[:]
    iterations = 0
    res = []
    norm_array = []
    converged = False

    while iterations < MAX_ITERATIONS:
        x_old = x_new[:]
        
        for i in range(n):
            sigma = 0.0
            for j in range(n):
                if j != i:
                    sigma += A.matrix[i][j] * x_old[j]
            
            x_new[i] = (b[i] - sigma) / A.matrix[i][i]
        
        iterations += 1
        
        res = residual(A, b, x_new)

        norm, was_calculated = euclidean_norm(res)

        if not was_calculated:
            break

        norm_array.append(norm)
        if norm < MAX_RES_NORM:
            converged = True
            break
    

    iterations = [i for i in range(iterations)]
    return x_new, iterations, norm_array, converged   



def gauss_seidel_method(A : Matrix, b : list, x : list) -> tuple:
    n = len(b)
    x_new = x[:]
    iterations = 0
    res = []
    norm_array = []

    converged = False

    while iterations < MAX_ITERATIONS:
        x_old = x_new[:]

        for i in range(n):
            sigma = 0.0


            for j in range(n):
                if j != i:
                    sigma += A.matrix[i][j] * x_new[j]

            x_new[i] = (b[i] - sigma) / A.matrix[i][i]
        
        iterations += 1

        res = residual(A, b, x_new)

        norm, was_calculated = euclidean_norm(res)

        if not was_calculated:
            iterations -= 1
            break

        norm_array.append(norm)
        if norm < MAX_RES_NORM:
            converged = True
            break

    iterations = [i for i in range(iterations)]
    return x_new, iterations, norm_array, converged


def plot_jacobi_gaus(jacobi : tuple , gaus : tuple):

    iterations_jac, residual_norm_jac = jacobi
    iterations_gaus, residual_norm_gaus = gaus


    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)  
    plt.plot(iterations_jac, residual_norm_jac)
    plt.yscale('log')
    plt.title('Jacobi 1: Zmiana normy residuum w kolejnych iteracjach')
    plt.xlabel('Iteracje')
    plt.ylabel('Norma residuum (log)')

    plt.subplot(2, 1, 2)  
    plt.plot(iterations_gaus, residual_norm_gaus)
    plt.yscale('log')
    plt.title('Gaus Seidel 2: Zmiana normy residuum w kolejnych iteracjach')
    plt.xlabel('Iteracje')
    plt.ylabel('Norma residuum (log)')

    #plt.legend()
    plt.tight_layout()
    plt.show()


def show_results(info):
    result, iterations, residual_norm, time, converged, name = info

    iterations = len(iterations)
    result = result[-1]
    residual_norm = residual_norm[-1]

    print("Results for {}: ".format(name))
    print("Result: {}".format(result))
    print("Iterations: {}".format(iterations))
    print("Residual Norm: {}".format(residual_norm))
    print("Time Taken: {} seconds".format(time))
    print("Converged: {}".format(converged))






