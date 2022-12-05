from graph.graph import *

def main():
    g = Graph(
        [0,1,2,3,4,5,6,7,8,9], 
        [
            Edge(0,7), 
            Edge(7,1), 
            Edge(1,2), 
            Edge(7,6), 
            Edge(1,5), 
            Edge(5,4), 
            Edge(2,9),
            Edge(2,4),
            Edge(4,6), 
            Edge(9,4), 
            Edge(4,3), 
            Edge(6,8)
        ])

    print(g.shortest_path(Node(9),Node(0)))
    print(g.shortest_path_length(Node(9),Node(0)))
    print(g.check_shortest_path(Node(9),Node(0), [9, 2, 1, 7, 0]))


if __name__ == "__main__":
    main() 