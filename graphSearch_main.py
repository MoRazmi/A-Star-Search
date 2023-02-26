import graphSearch_graph
import graphSearch_A_star_Search 

# Create a new Graph instance
g = graphSearch_graph.Graph()

# Add nodes to the graph
g.update_nodes()
g.update_edge()

a = graphSearch_A_star_Search.A_Star(g)
node_goal = len(g.nodes)
a.run_algorithm(node_goal)
