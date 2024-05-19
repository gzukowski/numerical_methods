from utils.Matrix import Matrix
from methods import prepare_data, plot_data, interpolation

LAGRANGE = 1
SPLINES = 0
#FILE = "MountEverest.csv"
FILE = "tczew_starogard.txt"
DIR_PATH = "2018_paths/"



if __name__ == "__main__":
      a = Matrix(5, 3)

      points = prepare_data(DIR_PATH + FILE)
      interpolated, nodes = interpolation(points)

      plot_data(points, interpolated, nodes, FILE)