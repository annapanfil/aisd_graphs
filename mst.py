# minimum spanning tree prim algorithm
def mst_prim_mtrx(adj_mtrx):
    max_value = 1e20 #np.max(adj_mtrx)+1
    visited = [0]
    edges = []
    for _ in range(len(adj_mtrx)-1):
        #Szukaj najlżejszej krawędzi
        minimum = max_value
        for vertex in visited:
            for neighbor in range(len(adj_mtrx[vertex])):
                if neighbor not in visited and 0 < adj_mtrx[vertex][neighbor] < minimum :
                    minimum = adj_mtrx[vertex][neighbor]
                    edge = (vertex,neighbor)
        visited.append(edge[1])
        edges.append(edge)
    return edges
    #[print(edge) for edge in edges]

def mst_prim_list(adj_list):
    max_value = 1e20
    visited = [0]
    edges = []
    for _ in range(len(adj_list)-1):
        #Szukaj najlżejszej krawędzi
        minimum = max_value
        for start in visited:
            for end in range(len(adj_list[start])):
                if adj_list[start][end][0] not in visited and adj_list[start][end][1] < minimum :
                    minimum = adj_list[start][end][1]
                    edge = (start,adj_list[start][end][0])
        visited.append(edge[1])
        edges.append(edge)
    return edges
    # [print(edge) for edge in edges]



if __name__ == '__main__':

    mst_prim_list([[(1,8),(2,9),(5,10)],[(0,8),(2,15),(5,20)],[(0,9),(1,15),(4,10)],[(4,7),(5,20)],[(2,10),(3,7)],[(0,10),(1,20),(3,20)]])
    print("matrix")
    mst_prim_mtrx([[0,8,9,0,0,10],[8,0,15,0,0,20],[9,15,0,0,10,0],[0,0,0,0,7,20],[0,0,10,7,0,0],[10,20,0,20,0,0]])

