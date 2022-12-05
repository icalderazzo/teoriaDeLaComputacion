# adjacencia
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
        if(self._lookup_adj(node) == None):
            self.adj_list.append(Adjacency(node))
    
    # Busqueda en profundidad
    def dfs(self, nodes):
        self.visited = True
        nodes.append(self.value)
        for adj in self.adj_list:
            if not adj.dest.visited:
                adj.dest.dfs(nodes)

    # Busqueda en amplitud
    def bfs(self, nodes):
        self.visited = True
        nodes.append(self.value)
        stack = []
        stack.insert(0,self)
        while (len(stack) > 0):
            x = stack.pop()
            for adj in x.adj_list:
                if not adj.dest.visited:
                    adj.dest.visited = True
                    nodes.append(adj.dest.value)
                    stack.insert(0, adj.dest)
                    
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

    # Busqueda en profundidad
    def dfs(self, node):
        nodes = []
        origin = self._get_node(node)
        if (origin != None):
            self._unvisit_all()
            origin.dfs(nodes)
            for n in self.nodes.values():
                if not n.visited:
                    n.dfs(nodes)
        return nodes

    # Busqueda en amplitud
    def bfs(self, node):
        nodes = []
        origin = self._get_node(node)
        if (origin != None):
            self._unvisit_all()
            origin.bfs(nodes)
        return nodes

    # Componentes conexos
    def connected_components(self):
        # 1: Resetear visitados
        # 2: Realizar busqueda en profundidad (DFS) en aquellos nodos que no fueron visitados
        # 3: Aumentar contador luego de cada DFS
        self._unvisit_all()
        # comenzar dfs desde el primer nodo
        self.dfs(self.nodes[self.nodes.keys[0]])
        cc = []
        for n in self.nodes:
            # Si el nodo no fue visitado, realizar DFS 
            if(not self.nodes[n].visited):
                self.dfs(self.nodes[n])
                cc.append()  
        return cc
    
    # Cantidad de componented conexos
    def count_connected_components(self):
        # 1: Resetear visitados
        # 2: Realizar busqueda en profundidad (DFS) en aquellos nodos que no fueron visitados
        # 3: Aumentar contador luego de cada DFS
        self._unvisit_all()
        # comenzar dfs desde el primer nodo
        self.dfs(self.nodes[self.nodes.keys[0]])
        count = 0
        for n in self.nodes:
            # Si el nodo no fue visitado, realizar DFS 
            if(not self.nodes[n].visited):
                self.dfs(self.nodes[n])
                count += 1 
        return count

    # Es conexto
    def is_connected(self):
        # 1: Se hace una busqueda en profunidad
        # 2: Se recorren todos los nodos y se pregunta si fueron visitados
        # 3: Si alguno no fue visitado, devuleve Falso, de lo contratio Verdadero
        self._unvisit_all()
        # self.dfs()
        for n in self.nodes:
            if(not self.nodes[n].visited):
                return False
        return True

    # Camino mas corto entre A y B
    def shortest_path(self, nodeA, nodeB):
        #1: Resetear visitados
        self._unvisit_all()

        #2: Si el nodo origen y destino es el mismo, retornar un camino consigo mismo
        if nodeA == nodeB:
            return [nodeA]
        
        #3: Inicializo una queue con el nodo representado por la etiqueta A
        queue = [[self._get_node(nodeA)]]

        while(queue):
            path = queue.pop(0)
            node = path[-1]

            #4: Si el nodo no fue visitado, reviso su lista de adyacencias
            if not node.visited:
                for neighbour in node.adj_list:
                    #5: Voy agregando las adyacencias al path
                    new_path = list(path)
                    new_path.append(neighbour.dest)
                    queue.append(new_path)

                    #6: Si uno de mis vecinos es el nodo destino, terminamos el camino
                    if neighbour.value == nodeB:
                        result = []
                        for node in new_path:
                            result.append(node.value)
                        return result
                node.visited = True

        return []

    # Largo del camino mas corto
    def shortest_path_length(self, nodeA, nodeB):
        return len((self.shortest_path(nodeA, nodeB)))

    # Reviso si el camino objetivo es el mismo que el camino mas corto
    def check_shortest_path(self, nodeA, nodeB, uncheckedPath):
        return self.shortest_path(nodeA, nodeB) == uncheckedPath

        

    def _get_node(self, nodeValue):
        return self.nodes[nodeValue]

    def _lookup_node(self, nodeValue):
        return nodeValue in self.nodes
    
    def _unvisit_all(self):
        for n in self.nodes:
            self.nodes[n].visited = False