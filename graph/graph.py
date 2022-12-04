# Adyacencia
class Adjacency:
    def __init__(self, dest):
        self.dest = dest
        self.value = self.dest.value

# Nodo o vertice
class Node:
    def __init__(self, value, visited = False):
        self.value = value
        self.adj_list = []
        self.visited = visited
    
    def add_adj(self, node):
        if(self._lookup_adj(node) != None):
            self.add_adj.append(Adjacency(node))

    def _lookup_adj(self, node):
        for a in self.adj_list:
            if(a.value == node.value):
                return a
        return None             

# Arista
class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

#
class EdgeList:
    def __init__(self, edgeList):
        self.edgeList = edgeList

# Grafo (no dirigido)
class Graph:
    def __init__(self, nodes, edges = []):
        self.nodes = {}
        [self.add_node(Node(n)) for n in nodes]
        [self.add_edge(e) for e in edges]

    def add_node(self, node):
        if(not self._lookup_node(node.value)):
            self.nodes[node.value] = node

    def add_edge(self, edge):
        if(self._lookup_node(edge.origin) and self._lookup_node(edge.destination)):
            node1 = self._get_node(edge.origin)
            node2 = self._get_node(edge.destination)
            # agrega ambas referencias
            node1.add_adj(node2)
            node2.add_adj(node1)

    # Componentes conexos
    def connected_components(self):
        # 1: Resetear visitados
        # 2: Realizar busqueda en profundidad (DFS) en aquellos nodos que no fueron visitados
        # 3: Aumentar contador luego de cada DFS
        self._reset_visited()
        cc = []
        for n in self.nodes:
            # Si el nodo no fue visitado, realizar DFS 
            if(not self.nodes[n].visited):
                ## call dfs(n) and append the list
                cc.append()  
        return cc
    
    # Cantidad de componented conexos
    def count_connected_components(self):
        # 1: Resetear visitados
        # 2: Realizar busqueda en profundidad (DFS) en aquellos nodos que no fueron visitados
        # 3: Aumentar contador luego de cada DFS
        self._reset_visited()
        count = 0
        for n in self.nodes:
            # Si el nodo no fue visitado, realizar DFS 
            if(not self.nodes[n].visited):
                ## call dfs(n) and append the list
                count += 1 
        return count

    # Es conexto
    def is_connected(self):
        # 1: Se hace una busqueda en profunidad
        # 2: Se recorren todos los nodos y se pregunta si fueron visitados
        # 3: Si alguno no fue visitado, devuleve Falso, de lo contratio Verdadero
        self._reset_visited()
        # self.dfs()
        for n in self.nodes:
            if(not self.nodes[n].visited):
                return False
        return True

    def _get_node(self, nodeValue):
        return self.nodes[nodeValue]

    def _lookup_node(self, nodeValue):
        return nodeValue in self.nodes
    
    def _reset_visited(self):
        for n in self.nodes:
            self.nodes[n].visited = False