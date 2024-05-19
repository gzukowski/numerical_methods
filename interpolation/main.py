from utils.Matrix import Matrix
from methods import prepare_data, plot_data, interpolation

LAGRANGE = 1
SPLINES = 0
DATA_SOURCE = "2018_paths/WielkiKanionKolorado.csv"

if __name__ == "__main__":
      a = Matrix(5, 3)

      points = prepare_data(DATA_SOURCE)
      interpolated, nodes = interpolation(points, mode=SPLINES)

      plot_data(points, interpolated, nodes)