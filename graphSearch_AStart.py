import numpy as np

import math
import graphSearch_csvReader
import graphSearch_node
import graphSearch_graph
import graphSearch_node

# Create a new Graph instance
g = graphSearch_graph.Graph()

# Add nodes to the graph
g.update_nodes()
g.update_edge()

# g.add_node(1)
# g.add_node(2)
g.add_parent(1,2 )


for node_id, node in g.nodes.items():
    print(f"Node {node_id}:")
    print(node.heuristic_cost)
    print(node.parent)
    for neighbor, weight in node.edges.items():
        print(f"  edge to node {neighbor} with weight {weight}")

