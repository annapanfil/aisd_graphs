from generator import *

def DFSlist(v, list, visited = []):
    for child in list[v]:         # odwiedź dzieci, jeśli nieodwiedzone
        if child not in visited:
            DFSlist(child, list, visited)
    visited.append(v)             # zaznacz się jako przetworzony
    return visited

def DFSmatrix(v, matrix, visited = []):
    for col in range(len(matrix)):         # odwiedź dzieci, jeśli nieodwiedzone
        if  matrix[v][col] == 1:
            if col not in visited:
                DFSmatrix(col, matrix, visited)
    visited.append(v)             # zaznacz się jako przetworzony
    return visited

if __name__ == '__main__':
    matrix, list, root = generateDAG(10, 60)
    printList(list)
    printMatrix(matrix)

    ordered1 = DFSlist(root, list)
    ordered2 = DFSmatrix(root, matrix)
    print(ordered1, "\n", ordered2) # w kolejności od najwcześniej przetworzonego
