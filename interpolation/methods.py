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


def splines_y(points: list[Pair], x : float, nodes : list, abcd : tuple):
    a, b, c, d = abcd

    index = NODES_NUM - 1
    for i in range(len(nodes) - 1):
        if points[nodes[i]].x <= x < points[nodes[i+ 1]].x:
            index = i
            break

    h = x-points[nodes[index]].x
    return a[index] + b[index] * h + c[index] * h**2 + d[index] * h ** 3

def splines(points : list[Pair], nodes : list):
    a = [points[node].y for node in nodes]
    b = [0 for _ in range(N-1)]
    d = [0 for _ in range(N-1)]
    h = [points[nodes[i+1]].x - points[nodes[i]].x for i in range(N-1)]

    A = Matrix(NODES_NUM, NODES_NUM)
    vec = Matrix(NODES_NUM, 1)
    for i in range(1, NODES_NUM-1):
        A.matrix[i][i] = 2 * (h[i-1] + h[i])
        A.matrix[i][i-1] = h[i-1]
        A.matrix[i][i+1] = h[i]
        vec.matrix[i][0] = 3 * ((points[nodes[i+1]].y - points[nodes[i]].y)/h[i] - (points[nodes[i]].y - points[nodes[i-1]].y)/h[i-1])
    A.matrix[0][0] = 1
    A.matrix[NODES_NUM-1][NODES_NUM-1] = 1

    x = Matrix(NODES_NUM, 1)
    c, dummy = LU_decomposition(A, vec, x)
    for i in range(NODES_NUM-1):
        d[i] = ((c[i+1] - c[i])/(3 * h[i]))
        b[i] = ((points[nodes[i+1]].y - points[nodes[i]].y)/h[i] - h[i]/3 * (2 * c[i] + c[i+1]))

    b += [0]
    d += [0]

    X = linspace(points[0].x, points[-1].x, INTERPOLATING_NUM)
    results = [Pair(x, splines_y(points, x, nodes, (a,b,c,d))) for x in X]

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

def linspace(start, end, n):
    if n == 1:
        return
    value = (end - start) / (n - 1)
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = start + value * i
    
    return result

def generate_chebysev(n):
    results = [0 for _ in range(n)]

    for k in range(n):
        results[k] = int(((math.cos((k*PI) / (n - 1)) + 1) / 2) * (N-1))

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
