import numpy as np
from enum import Enum
import math
import csv

def read_csv_file(file_path, data):
     """Read csv file and ignore the comment line"""
     with open(file_path) as csv_file:
          csv_reader = csv.reader(csv_file)
          for row in csv_reader:
               if not row or row[0].startswith('#'):
                    continue
               data.append(row)
     return data

node_data = []
node_data = read_csv_file('nodes.csv', node_data)
edge_data = []
edge_data = read_csv_file('edges.csv', edge_data)

#print(edge_data)

class searchCondition(Enum):
     """Enum defintion for Open and close nodes"""
     CLOSE = True
     OPEN = False

class node_position:
     """The 2D position represent the position of a node in a 2-dimnesional space."""
     def __init__(self,x, y):
      self.x = x
      self.y = y

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.heuristic_cost = 0
        self.position = {}
        
    def add_heu_cost(self, heuristic_cost):
        self.heuristic_cost = heuristic_cost

    def add_position(self, x, y):
        self.position[0] = x
        self.position[1] = y

    def add_edge(self, neighbor, weight =0):
        self.edges[neighbor] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        """Add a node new node to the graph with three new parameters: ID, Position, and heurusitic cost"""
        self.nodes[id] = Node(id)
    
    def add_position(self, node1 , x, y):
        self.nodes[node1].add_position(x, y)
    
    def add_heuristic_cost(self, node1 ,heuristic_cost):
        self.nodes[node1].add_heu_cost(heuristic_cost)
        
    def add_edge(self, node1, node2, weight = 0):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_edge(node2, weight)
        self.nodes[node2].add_edge(node1, weight)

# Create a new Graph instance
g = Graph()

# Add nodes to the graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_position(1, 1, 2)
g.add_heuristic_cost(1, 0.2)

# Add edges to the graph
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 3)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 4)
 
for node_id, node in g.nodes.items():
    print(f"Node {node_id}:")
    print(node.heuristic_cost)
    for neighbor, weight in node.edges.items():
        print(f"  edge to node {neighbor} with weight {weight}")

def node_extraxor(data):
    """Extract nodes after read csv file"""
    for row in range(len(data)):
        id = int(data[row][0])
        graph.add_node(id)
        position = node_position(float(data[row][1]), float(data[row][2]))
        graph.add_node(id)
        heuristic_cost = float(data[row][3])
        node = Node(id, position, heuristic_cost)
        graph.add_node(node)

def edge_extractor(data):
    """Extract edges after read csv file"""
    print(len(data))
    for row in range(len(data)):
        node_print = list(graph.nodes.values())[int(data[row][0])*3-3]
        print(node_print)

