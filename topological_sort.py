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

def find_root(matrix):
    # szuka wierzchołka od którego zacznie – v_in = 0
    sumout=1
    root=-1
    while(sumout !=0):
        root+=1
        sumout = 0
        for i in range(len(matrix)):
            sumout += matrix[i][root]

    return root

if __name__ == '__main__':
    matrix, list = generateDAG(5, 60)
    printList(list)
    printMatrix(matrix)

    find_root(matrix)
    ordered1 = DFSlist(root, list, [])
    print(ordered1)
    ordered2 = DFSmatrix(root, matrix, [])
    print(ordered2)
