from math import *
from matrix import Matrix
from typing import List
import time
import matplotlib.pyplot as plt
import copy
import numpy as np
import scipy.linalg as la


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
    x = [0 for element in range(N)]

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

    
    matrix = Matrix(N)
    matrix.fill_matrix(A1C, A2C, A3C)

    b = [sin(element*(F+1)) for element in range(N)]
    x = [1 for element in range(N)]


    start = time.time()
    result, norm = LU_decomposition(matrix, b, x)

    end = time.time()

    return result, norm, end - start


def exerciseE():

    jacobi_times = []
    gaus_times = []
    lu_times = []
    variables_count = [50, 100, 1000, 2000, 3000]

    for var in variables_count:

        matrix = Matrix(var)
        matrix.fill_matrix(A1A, A2A, A3A)

        b = [sin(element*(F+1)) for element in range(var)]
        x = [1 for element in range(var)]

        start = time.time()
        jacobi_method(matrix, b, x)
        end = time.time()
        jacobi_times.append(end - start)

        start = time.time()
        gauss_seidel_method(matrix, b, x)
        end = time.time()
        gaus_times.append(end - start)


        start = time.time()
        LU_decomposition(matrix, b, x)
        end = time.time()
        lu_times.append(end - start)

        print(jacobi_times[-1], gaus_times[-1], lu_times[-1])


    return jacobi_times, gaus_times, lu_times


    
    

def residual(A: Matrix, b: List[float], x: List[float]) -> List[float]:
    r = A * x

    for i in range(len(b)):
        r[i] -= b[i]

    return r

def euclidean_norm(v: List[float]) -> float:
    sigma = 0
    
    was_calculated = True

    try:
        for element in v:
            sigma += element ** 2

    except OverflowError:
        was_calculated = False



    return sqrt(sigma), was_calculated


def LU_decomposition(A : Matrix, b : list, x : list):
    U = copy.deepcopy(A)
    L = Matrix(A.size)
    L.fill_identity()
    n = U.size
    x_new = x[:]
    
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

        y[i] = (b[i] - sigma) / L.matrix[i][i]

    for i in range(n - 1, -1, -1):
        sigma = 0
        
        for j in range(i + 1, n):
            sigma += U.matrix[i][j] * x_new[j]

        x_new[i] = (y[i] - sigma) / U.matrix[i][i]

    res = residual(A, b, x_new)

    norm, was_calculated = euclidean_norm(res)

    x_new = [round(x, 10) for x in x_new]

    return x_new, norm


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

def plot_times(jacobi, gaus, lu):
    pass


def show_results(info):

    if info[-1] == "LU":
        residual_norm, time, name = info
        print("Results for {}: ".format(name))
        print("Residual Norm: {}".format(residual_norm))
        print("Time Taken: {} seconds".format(time))
        return
    


    iterations, residual_norm, time, converged, name = info

    iterations = len(iterations)
    result = result[-1]
    residual_norm = residual_norm[-1]

    print("Results for {}: ".format(name))
    print("Iterations: {}".format(iterations))
    print("Residual Norm: {}".format(residual_norm))
    print("Time Taken: {} seconds".format(time))
    print("Converged: {}".format(converged))






