from generator import *
from data_export import *
from topological_sort import *
import numpy as np
from mst import *

def main_mst():
    filenames = ["data/mst_list70.txt","data/mst_matrix70.txt"]
    saturation = 60
    probes = 3
    for n in range(100, 420, 20):
        timel = 0
        timem = 0
        for a in range(probes):
            matrix, list = generateUWG(n,70,1000)
            timel += measure_time(mst_prim_list, list)
            timem += measure_time(mst_prim_mtrx, matrix)
        export_data_to_file(filenames[0], timel/probes)
        export_data_to_file(filenames[1], timem/probes)
        print(n)
    return 0

def main_ts():
    filenames = ["data/ts_matrix.txt", "data/ts_list.txt"]
    saturation = 60
    probes = 3
    for n in range(100, 1000, 20):
        timel = 0
        timem = 0
        for a in range(probes):
            matrix, list = generateDAG(n, saturation)
            timem += measure_time(DFSmatrix, matrix, 0)
            timel += measure_time(DFSlist, list, 0)
        export_data_to_file(filenames[0], timem/probes)
        export_data_to_file(filenames[1], timel/probes)
    return 0

def read_from_file(filename):
    file = open(filename, "r")

    size = int(file.readline())
    content = file.readlines()
    matrix = [row.split() for row in content]

    file.close()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


def main_show():
    print("\nSORTOWANIE TOPOLOGICZNE\n------------------------\n\nDane:")
    matrix = read_from_file("data/topol.txt")
    print(np.array(matrix))

    root = find_root(matrix)
    order = DFSmatrix(root, matrix, [])

    print("\nPorządek topologiczny: ")
    for i in reversed(order):
        print(i+1, end = " ")
    print("\n")

    print("\nMINIMALNE DRZEWO ROZPINAJĄCE\n-----------------------------\n\nDane:")
    matrix = read_from_file("data/mst.txt")
    print(np.array(matrix))

    edges = mst_prim_mtrx(matrix)
    print("\nKrawędzie MST: ")
    [print(edge, end=" ") for edge in edges]
    print("\nSuma wag na krawędziach: ")
    # TODO: suma wag


if __name__ == '__main__':
    main_show()
