from matrix import Matrix
from methods import prepare_data, plot_data, interpolation


DATA_SOURCE = "2018_paths/przyk3.txt"

if __name__ == "__main__":
      a = Matrix(5, 3)

      points = prepare_data(DATA_SOURCE)
      interpolated = interpolation(points)

      print(interpolated)

      plot_data(points, interpolated)