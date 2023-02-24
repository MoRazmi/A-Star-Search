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

class searchCondiition(Enum):
     """Enum defintion for Open and close nodes"""
     CLOSE = True
     OPEN = False

class node_position:
     """The 2D position represent the position of a node in a 2-dimnesional space."""
     def __init__(self,x, y):
      self.x = x
      self.y = y

class Node:
    def __init__(self, id,node_position, heuristic_cost):
        self.id = id
        self.node_position = node_position
        self.heuristic_cost = heuristic_cost
        self.edges = {}

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        """Add a node new node to the graph with three new parameters: ID, Position, and heurusitic cost"""
        self.nodes[node.id] = node.id
        self.nodes[node.node_position] = node.node_position
        self.nodes[node.heuristic_cost] = node.heuristic_cost


    def add_edge(self, node1, node2, weight=0):
        """Add a edge between two nodes with specified weight associated to it"""
        if node1.id not in self.nodes:
            self.add_node(node1)
        if node2.id not in self.nodes:
            self.add_node(node2)
        node1.add_edge(node2, weight)
        node2.add_edge(node1, weight)

graph = Graph()

def node_extraxor(data):
    """Extract nodes after read csv file"""
    for row in range(len(data)):
        id = int(data[row][0])
        position = node_position(float(data[row][1]), float(data[row][2]))
        heuristic_cost = float(data[row][3])
        node = Node(id, position, heuristic_cost)
        graph.add_node(node)


def edge_extractor(data):
    """Extract edges after read csv file"""
    print(len(data))
    for row in range(len(data)):
        node_print = list(graph.nodes.values())[int(data[row][0])*3-3]
        print(node_print)

node_extraxor(node_data)
edge_extractor(edge_data)