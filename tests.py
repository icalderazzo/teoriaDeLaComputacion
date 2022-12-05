from graphutils.graph import *

g1 = Graph(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [
        Edge(0, 7),
        Edge(7, 1),
        Edge(1, 2),
        Edge(7, 6),
        Edge(1, 5),
        Edge(5, 4),
        Edge(2, 9),
        Edge(2, 4),
        Edge(4, 6),
        Edge(9, 4),
        Edge(4, 3),
        Edge(6, 8)
    ])

g2 = Graph(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [
        Edge(1, 6),
        Edge(6, 0),
        Edge(0, 2),
        Edge(2, 4),
        Edge(5, 3),
        Edge(5, 7),
        Edge(8, 9)
    ]
)

g3 = Graph(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [
        Edge(0,2),
        Edge(0,3),
        Edge(0,5),
        Edge(0,8),
        Edge(1,4),
        Edge(1,6),
        Edge(2,3),
        Edge(2,7),
        Edge(3,9),
        Edge(4,5),
        Edge(6,8),
        Edge(6,9)
    ]
)

# Funcionalid 1 (DFS)
def dfs_test(g=g1, n=2):
    print(f'\nDFS: Busqueda en profunidad del grafo\n{g.dfs(n)}\n')

# Funcionalidad 2 (BFS)
def bfs_test(g=g1, n=2):
    print(f'BFS: Busqueda en amplitud del grafo\n{g.bfs(n)}\n')

# Funcionalidad 3 (Componentes conexas)
def scc_test(g=g2):
    print(f'SCC: Componentes conexas del grafo\n{g.connected_components()}\n')

# Funcionalidad 4 (Cantidad componentes conexas)
def count_scc_test(g=g2):
    print(f'SCC: La cantidad de componentes conexas del grafo es: {g.count_connected_components()}\n')

# Funcionalidad 5 (Es conexo)
def is_connected_test(g=g2):
    print(f'SCC: El grafo es conexo?: {g.is_connected()}\n')

# Funcionalidad 6 (Camino mas corto entre 2 nodos)
def shortest_path_test(g=g3, a=4, b=3):
    print(f'SP: El camino más corto entre {a} y {b} es\n{g.shortest_path(a, b)}\n')

# Funcionalidad 7 (Largo del camino mas corto entre 2 nodos)
def shortest_path_length_test(g=g3, a=4, b=3):
    print(f'SP: El largo del camino más corto entre {a} y {b} es: {g.shortest_path_length(a, b)}\n')

# Funcionalidad 8 (Verificar si un camino dado es el mas corto entre 2 nodos)
def verify_shortest_path_test(g=g3, a=4, b=3, p=[4,5,0,3]):
    print(f'SP: Es {p} el camino mas corto entre {a} y {b}? {g.check_shortest_path(a, b, p)}\n')

def run_tests(g = None):
    if(g == None):
        dfs_test()
        bfs_test()
        scc_test()
        count_scc_test()
        is_connected_test()
        shortest_path_test()
        shortest_path_length_test()
        verify_shortest_path_test()
    else:
        dfs_test(g, 0)
        bfs_test(g, 0)
        scc_test(g)
        count_scc_test(g)
        is_connected_test(g)