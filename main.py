from generator import *
from data_export import *
from topological_sort import *

def main():
    filenames = ["data/ts_matrix.txt", "data/ts_list.txt"]
    saturation = 60
    probes = 3

    for n in range(100, 1000, 20):
        timel = 0
        timem = 0
        for a in range(probes):
            matrix, list, v = generateDAG(n, saturation)
            timel += measure_time(DFSlist, list, v)
            timem += measure_time(DFSlist, matrix, v)
        export_data_to_file(filenames[0], timel/probes)
        export_data_to_file(filenames[1], timem/probes)
    return 0

if __name__ == '__main__':
    main()
