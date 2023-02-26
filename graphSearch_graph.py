import graphSearch_node
import graphSearch_csvReader

class Graph:
    def __init__(self):
        self.nodes = {}


    def add_node(self, id):
        """Add a node new node to the graph with three new parameters: ID, Position, and heurusitic cost"""
        self.nodes[id] = graphSearch_node.Node(id)
        if (id == 1):
             self.nodes[id].save_pastCost(0)

    
    def add_position(self, node1 , x, y):
        """Add a position x and y coordinates"""
        self.nodes[node1].add_position(x, y)
    
    def add_heuristic_cost(self, node1 ,heuristic_cost):
        """Add a guess for the optimal path for a node to reach the destination"""
        self.nodes[node1].add_heu_cost(heuristic_cost)
        
    def add_edge(self, node1, node2, weight = 0):
        """Add edge in the graph connecting first node to second node with weight connecting them"""
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_edge(node2, weight)
        self.nodes[node2].add_edge(node1, weight)

    def add_parent(self,node1, node2):
        """Add parent for the node in the graph"""
        self.nodes[node1].add_parent(node2)

    def update_nodes(self):
        """Update graph with csv nodes including node id and position"""
        graphSearch_csvReader.node_extraxor(self)
    
    def update_edge(self):
        """Update graph with csv edges including two nodes and weights connecting them."""
        graphSearch_csvReader.edge_extractor(self)

    def close_node(self, node):
        """Close the node after A* search completed!"""
        self.nodes[node].close_node()

