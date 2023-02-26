import graphSearch_graph
import graphSearch_A_star_Search 

# Create a new Graph instance
g = graphSearch_graph.Graph()

# Add nodes to the graph
g.update_nodes()
g.update_edge()

# g.add_node(1)
# g.add_node(2)
# g.add_parent(1,2)
# g.close_node(1)

a = graphSearch_A_star_Search.A_Star(g)
node_goal = len(g.nodes)
a.run_algorithm(node_goal)

for node_id, node in g.nodes.items():
    print(node_id)
    print(node.heuristic_cost)
    for neighbor, weight in node.edges.items():
        print(f"  edge to node {neighbor} with weight {weight}")


""" 
print(g.nodes[3].edges.keys())
keys_list = list(g.nodes[3].edges.keys())
print(keys_list[0])

for node_id, node in g.nodes.items():
    print(node_id)
    print(node.heuristic_cost)
    print(node.parent)
    print(node.searchConditionClosed)
    for neighbor, weight in node.edges.items():
        print(f"  edge to node {neighbor} with weight {weight}")

"""
