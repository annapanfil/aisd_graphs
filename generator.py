import random

def generateUWG(v: int, saturation: int, weight = 9):
    # generowanie nieskierowanego ważonego grafu spójnego w postaci macierzy sąsiedztwa i listy incydencji
    # v – liczba wierzchołków, saturation – nasycenie w %, weight – maksymalne wagi krawędzi

    e = v*(v-1)/2 * saturation/100
    matrix = [[0 for i in range(v)]for i in range(v)]
    list = [[]for i in range(v)]

    if e<(v-1):
        print("Unable to generate connected graph")
        return -1

    vertexes = [i for i in range(v)]

    # żeby był spójny zaczynamy od ścieżki
    vout = vertexes.pop(0)
    for i in range (v-1):
        # losuje wierzchołek końcowy i wagę, dodaje krawędź do macierzy i listy
        vin = vertexes.pop(random.randrange(len(vertexes)))
        w = random.randrange(weight)+1
        matrix[vout][vin] = w
        matrix[vin][vout] = w
        list[vout].append((vin, w))
        list[vin].append((vout, w))
        vout = vin

    e-=v-1                                      # dodaje pozostałe krawędzie
    while(e!=0):
        vout = random.randrange(v)              # losuje wierzchołek początkowy...
        i = 0
        while (i<v):
            vin = random.randrange(v)           # ... i wierzchołek koncowy tak długo aż coś znajdzie
            if (vin == vout): continue          # bez pętli własnych
            if (matrix[vout][vin] == 0):
                w = random.randrange(weight)+1  # dodaje krawędź
                matrix[vout][vin] = w
                matrix[vin][vout] = w
                list[vout].append((vin, w))
                list[vin].append((vout, w))
                e-=1
            i+=1
    # IDEA: dla optymalizacji można dodać zbiór wierzchołków, do których nie da się już dodać krawędzi
    return (matrix, list)

def generateDAG():
    return 0


def printMatrix(matrix):
    print("\nMATRIX\n    ", end="")
    for i in range(len(matrix)):
        print(i, end=" ")
    print()

    for row in range(len(matrix)):
        print(row, ".", end=" ")
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()

def printList(list):
    print("\nLIST")
    for row in range(len(list)):
        print(row, ".", end=" ")
        for col in range(len(list[row])):
            print(list[row][col], end=" ")
        print()

if __name__ == '__main__':
    matrix, list = generateUWG(5, 60)
    printMatrix(matrix)
    printList(list)
