import graphSearch_graph

class A_Star:
    def __init__(self, graph):
        self.graph = graph
        self.sorted_nodes = []

    def check_all_Closed(self):
        all_closed = False
        for node_id, node in self.graph.nodes.items():
                all_closed = all_closed or node.searchConditionClosed
        return all_closed
    
    def update_sorted_list(self, node):
         if node in self.sortedList:
              self.sorted_nodes.remove(node)
         self.sorted_nodes.append(node)
         self.sorted_nodes.sort(key = lambda n: n.self.node[node].estTotCost)

    def get_neighbours_node(self, node_number):
         key_list = list(self.graph.nodes[node_number].edges.keys())
         return(key_list)

    
    def run_algorithm(self, node_goal):
        all_closed = False
        self.graph.nodes[1].close_node()
        self.graph.nodes[1].save_pastCost(0)
        while not all_closed:
             for node in self.graph.nodes.values():
                  if not node.searchConditionClosed:
                       self.graph.nodes[node.id].close_node()
                       if self.graph.nodes[node.id].id == node_goal:
                            return True
                       for neighbor in self.get_neighbours_node(node.id):
                            if self.graph.nodes[neighbor].searchConditionClosed == False:
                                 tenative_past_cost = self.graph.nodes[node.id].past_cost + float(self.graph.nodes[node.id].edges[neighbor])
                                 if tenative_past_cost < self.graph.nodes[node.id].past_cost:
                                         self.node[node].past_cost = tenative_past_cost
                                         self.node[neighbor].add_parent(node)
                                         self.update_sorted_list(self.node[node].id , self.node[node].estTotCost)
        all_closed = self.check_all_Closed(self)
        return False
    
    def print_sorted_nodes(self):
         print(self.sorted_nodes)

