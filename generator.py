import random

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

def matrixToList(matrix):
    # tworzy listę incydencji na podstawie macierzy sąsiedztwa
    v = len(matrix)
    list = [[]for i in range(v)]

    for vout in range(v):
        for vin in range(v):
            if matrix[vout][vin]==1:
                list[vout].append(vin)
    return list

def generateUWG(v: int, saturation: int, weight = 9):
    # generowanie nieskierowanego ważonego grafu spójnego w postaci macierzy sąsiedztwa i listy incydencji
    # v – liczba wierzchołków, saturation – nasycenie w %, weight – maksymalne wagi krawędzi

    e = round(v*(v-1)/2 * saturation/100)
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
    while(e>0):
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
                break
            i+=1
    # IDEA: dla optymalizacji można dodać zbiór wierzchołków, do których nie da się już dodać krawędzi
    return (matrix, list)

def generateDAG(v: int, saturation: int):
    # generowanie skierowanego acyklicznego grafu spójnego w postaci macierzy sąsiedztwa i listy incydencji
    # v – liczba wierzchołków, saturation – nasycenie w %

    if round(v*(v-1)/2 * saturation/100)<(v-1):
        print("Unable to generate connected graph")
        return -1

    e = v*v-round(v*(v-1)/2 * saturation/100)          # ilośc krawędzi do usunięcia (na początku mamy v^2 krawędzi)

    matrix = [[1 for i in range(v)]for i in range(v)]   # wygenerowanie grafu pełnego

    list = [[]for i in range(v)]


    # drzewo jest grafem acyklicznym – opieramy się na drzewie
    for i in range(v):
        matrix[i][i] = 0               # usuwa pętle własne
    e-=v

    root = random.randrange(v)         # losuje korzeń
    for i in range(v):                 # do korzenia nie może nic wchodzić
        matrix[root][i] = 0
    e-=v-1    # pętla własna już była usunięta

    leaf = root
    while root==leaf:
        leaf = random.randrange(v)         # losuje liść
    for i in range(v):                     # z liścia nie może nic wychodzić
        if matrix[i][leaf] == 1:
            matrix[i][leaf] = 0
            e-=1

    for i in range(v-1):                    # zamienia krawędzie dwustronne na jednostronne
        for j in range(i+1, v):
            if (matrix[i][j]*matrix[j][i]==1):
                if(random.randrange(2)==0):     # losuje, którą krawędź usunąć
                    matrix[i][j]=0
                else:
                    matrix[j][i]=0
                e-=1

    while(e>0):                                 # usuwa losowe krawędzie
        vout = random.randrange(v)              # losuje wierzchołek początkowy...
        i = 0
        while (i<=v):
            vin = random.randrange(v)           # ... i wierzchołek koncowy tak długo aż coś znajdzie
            if (matrix[vout][vin] == 1):
                matrix[vout][vin] = 0
                e-=1
                break
            i+=1

    list = matrixToList(matrix)
    return matrix, list


if __name__ == '__main__':
    matrix, list = generateDAG(5, 60)
    printMatrix(matrix)
    printList(list)
