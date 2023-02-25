from enum import Enum

class node_position:
     """The 2D position represent the position of a node in a 2-dimnesional space."""
     def __init__(self,x, y):
      self.x = x
      self.y = y

INFINITY = 10000

class searchCondition(Enum):
     """Enum defintion for Open and close nodes"""
     CLOSE = True
     OPEN = False

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.parent = 0
        self.heuristic_cost = 0
        self.past_cost = INFINITY
        self.position = {}
        
    def add_heu_cost(self, heuristic_cost):
        """Add heuritic cost to the node, i.e. the best guess
        to reach the goal"""
        self.heuristic_cost = heuristic_cost

    def add_position(self, x, y):
        """Add x y position of the node"""
        self.position[0] = x
        self.position[1] = y

    def add_edge(self, neighbor, weight =0):
        """Add edge to the node"""
        self.edges[neighbor] = weight

    def add_parent(self, parent):
        """Add the parent to the node"""
        self.parent = parent