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

if __name__ == '__main__':
    main_ts()
