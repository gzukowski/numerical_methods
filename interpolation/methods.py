import csv
from utils.Matrix import *
from utils.Pair import Pair
import os
import math
import matplotlib.pyplot as plt

INTERPOLATING_NUM = 1000

NODES_NUM = 30

LAGRANGE = 1
SPLINES = 0
N = 512
PI = 3.14



def lagrange_polynomial(points : list[Pair], x : float, nodes : list):
    nodes = [int(node) for node in nodes]
    result = 0

    for i in nodes:
        a = 1
        for j in nodes:
            if i != j:
                a *= (x - points[j].x) / (points[i].x - points[j].x)
        result += a * points[i].y

    return Pair(x, result)


def splines(points : list[Pair], nodes : list):
    n = len(nodes)
    a = [points[ix].y for ix in nodes]
    b = []
    d = []
    h = [points[nodes[i+1]].x - points[nodes[i]].x for i in range(n-1)]

    A = Matrix(n, n)
    vec = Matrix(n, 1)


    for i in range(1, n-1):
        A.matrix[i][i] = 2 * (h[i-1] + h[i])
        A.matrix[i][i-1] = h[i-1]
        A.matrix[i][i+1] = h[i]
        vec.matrix[i][0] = 3 * ((points[nodes[i+1]].y - points[nodes[i]].y)/h[i] - (points[nodes[i]].y - points[nodes[i-1]].y)/h[i-1])

    A.matrix[0][0] = 1
    A.matrix[n-1][n-1] = 1

    x = Matrix(n, 1)

    c, _ = LU_decomposition(A, vec, x)


    for i in range(n-1):
        d.append((c[i+1] - c[i])/(3 * h[i]))
        b.append((points[nodes[i+1]].y - points[nodes[i]].y)/h[i] - h[i]/3 * (2 * c[i] + c[i+1]))

    b.append(0)
    d.append(0)


    def F(x):
        ix = n-1
        for ix_num in range(len(nodes) - 1):
            if points[nodes[ix_num]].x <= x < points[nodes[ix_num + 1]].x:
                ix = ix_num
                break

        h = x-points[nodes[ix]].x
        return a[ix] + b[ix] * h + c[ix] * h**2 + d[ix] * h ** 3

    interpolated_X = list(linspace(points[0].x, points[-1].x, INTERPOLATING_NUM))


    results = [Pair(x, F(x)) for x in interpolated_X]

    return results

def interpolation(points : list[Pair], mode=LAGRANGE):    
    results = []

    nodes = linspace(0, N-1, NODES_NUM)
    nodes = [int(node) for node in nodes]

    #nodes = generate_chebysev(NODES_NUM)


    if mode == LAGRANGE:
        results = [lagrange_polynomial(points, element, nodes) for element in linspace(points[0].x, points[-1].x - 1, INTERPOLATING_NUM)]

    if mode == SPLINES:
        results = splines(points, nodes)


    return results, nodes 


def plot_data(data : list, interpolated : list, nodes : list, title : str):
    x_coords = [pair.x for pair in data]
    y_coords = [pair.y for pair in data]

    interpolated_x_coords = [pair.x for pair in interpolated]
    interpolated_y_coords = [pair.y for pair in interpolated]

    nodes_X = [data[index].x for index in nodes]
    nodes_Y = [data[index].y for index in nodes]

    plt.figure(figsize=(10, 6))

    plt.plot(x_coords, y_coords, '-', label='Data Points')
    plt.plot(interpolated_x_coords, interpolated_y_coords, '-', label='Interpolated Points', c='g')
    plt.scatter(nodes_X, nodes_Y, c='g')

    plt.xlabel('distance(m)')
    plt.ylabel('height(m)')
    plt.title(f"{title}\nNodes: {NODES_NUM}")
    plt.legend()
    plt.grid(True)
    plt.show()

def linspace(start, stop, n):
    if n == 1:
        return
    h = (stop - start) / (n - 1)
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = start + h * i
    
    return result

def generate_chebysev(n):

    def fu(k):
        return ((math.cos((k*PI) / (n - 1)) + 1) / 2) * (N-1)
    
    results = [int(fu(k)) for k in range(n)]
    results = results[::-1]
    
    return  results


def prepare_data(path : str):

    pairs = [0 for _ in range(N)]
    if ".txt" in path:
        file = open(path, "r")
        index = 0
        for line in file:
            point = line.strip().split(" ")
            try:
                x = float(point[0])
                y = float(point[1])
                pairs[index] = Pair(x, y)
                index += 1
            except ValueError:
                continue


    if ".csv" in path:
        with open(path, "r") as file:
            reader = csv.reader(file)
            index = 0
            for row in reader:
                try:
                    x = float(row[0])
                    y = float(row[1])
                    pairs[index] = Pair(x, y)
                    index += 1
                except ValueError:
                    continue

    return pairs
