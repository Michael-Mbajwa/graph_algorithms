# graph_algorithms
I created my own graph class. It is a dictionary of dictionaries G, an instance variable which stores the graph structure. 
More precisely, G[v1][v2] is a string which represents the label of the edge v1v2 of the graph.
The class graph has the following methods :
— vertices() returns the set of vertices of the graph ; 
— edges() returns the set of edges of the graph ;
— deg(v) returns the degree of the vertex v ;
— is_edge(u, v) returns True iff uv is an edge.
