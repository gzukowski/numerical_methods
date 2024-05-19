from utils.Pair import Pair
import os
import matplotlib.pyplot as plt


LAGRANGE = 1
SPLINES = 0
N = 512

NODES_NUM = 3

def lagrange_polynomial(points : list[Pair], x : float):
    n = len(points)
    elevation = 0

    for i in range(n):
        a = 1
        for j in range(n):
            if i != j:
                a *= (x - points[j].x) / (points[i].x - points[j].x)
        elevation += a * points[i].y

    return Pair(x, elevation)

def prepare_data(path : str):
    pairs = [0 for _ in range(N)]
    file = open(path, "r")
    index = 0
    for line in file:
        point = line.strip().split()

        x = float(point[0])
        y = float(point[1])
        pairs[index] = Pair(x, y)
        index += 1

    return pairs


def plot_data(data : list, interpolated : list):
    # Extract x and y coordinates from pairs
    x_coords = [pair.x for pair in data]
    y_coords = [pair.y for pair in data]

    interpolated_x_coords = [pair.x for pair in interpolated]
    interpolated_y_coords = [pair.y for pair in interpolated]

    plt.figure(figsize=(10, 6))

    plt.plot(x_coords, y_coords, '-', label='Data Points')
    print(y_coords)

    plt.plot(interpolated_x_coords, interpolated_y_coords, '-', label='Interpolated Points', c='g')
    plt.scatter(interpolated_x_coords, interpolated_y_coords, c='g')
    # Create the plot
    
      # 'o-' plots points with lines connecting them
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Function Plot from Points')
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

def splines(points : list[Pair], distance):
    pass

def interpolation(points, mode=LAGRANGE):    
    results = []
    nodes = linspace(points[0].x, points[-1].x, NODES_NUM)

    for node in nodes:
        result = lagrange_polynomial(points, node)
        results.append(result)

    return results
