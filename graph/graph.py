#
class Adjacency:
    def __init__(self, dest):
        self.dest = dest
        self.value = self.dest.value

# 
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

#
class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

#
class EdgeList:
    def __init__(self, edgeList):
        self.edgeList = edgeList

#
class Graph:
    # nodes: una lista de elementos de un tipo de dato cualquiera
    # [1,2,3] o [a,b,c] o [Doha, TuPrima]
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

    def _get_node(self, nodeValue):
        return self.nodes[nodeValue]

    def _lookup_node(self, nodeValue):
        return nodeValue in self.nodes