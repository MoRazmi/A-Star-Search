# A Star Search
 The A* Search graph 
Introduction
This software is designed to implement A* graph search algorithm for robotics motion 
planning. The software includes 5 python files that work together to create a graph 
and find the shortest path between two nodes in the graph.



https://user-images.githubusercontent.com/96496279/221480509-ed988f98-8614-419a-bdac-c91813ade5bf.mp4


File Descriptions
graphsearch_node.py - This file contains the Node class that represents a node in the graph. 
Each node has an x and y coordinate, a cost value, a parent node, and a list of its neighbors.

graphsearch_graph.py - This file contains the Graph class that represents the entire graph. 
It has functions to add nodes and edges to connect them. It also has a function to get a 
node by its x and y coordinates.

graphsearch_A_start_search.py - This file contains the A* search algorithm implementation.
 It takes the start and goal nodes and the graph as input and returns the shortest path 
between them.

graphsearch_csvReader.py - This file contains functions to read and write nodes and edges 
from and to csv files.

graphsearch_main.py - This file is the main file that runs the A* search algorithm. It 
creates a graph, adds nodes and edges to it, reads nodes and edges from csv files, and 
finds the shortest path between two nodes.
