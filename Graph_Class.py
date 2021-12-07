class Graph:
    """
    A class created for an undirected graph.
    The graph class uses a dict-of-dict data structure.
    A graph stores vertices and edges. Edges are undirected but can be weighted.
    This graph supports parallel edges.

    The outer dict (vertices_dict) holds information keyed by vertex.
    The inner dict holds edge data keyed by each neighbor.

    """

    def __init__(self, data=None):
        """
        :param data: The graph class can be created with a value for the vertex. data must be hashable.
        """
        self.nodes = {}
        try:
            if data is not None:
                self.nodes[data] = {}
        except TypeError:
            print('Please provide an number or a string instead.')

    def __getitem__(self, item1, item2=None):
        if item2:
            return self.nodes[item1][item2]
        else:
            return self.nodes[item1]

    def __contains__(self, item):
        """Returns True if item is a node on the graph"""
        try:
            return item in self.nodes
        except TypeError:
            return False

    def __len__(self):
        """Returns the length of the number of vertices in the graph."""
        return len(self.nodes)

    def add_vertex(self, item):
        """
        :param item: Because we are using a dictionary structure, item has to be hashable. That means it can be any
        data structure except None. Our node can be an integer, float, string etc.
        """
        try:
            if item not in self.nodes:
                self.nodes[item] = {}
            else:
                pass
        except TypeError:
            print('Please provide an number or a string instead.')

    def number_of_vertices(self):
        """
        :return: the number of nodes in the graph.
        """
        return len(self.nodes)

    def add_edge(self, u, v, label=None):
        """
        Adds an edge between vertices u and v
        :param u: Must be provided. If u doesn't exist, it will be created
        :param v: Must be provided. If v doesn't exist, it will be created
        :param label: Refers to the name of the edge. Default value is None.
        """
        if u not in self.nodes:
            self.nodes[u] = {}
        if v not in self.nodes:
            self.nodes[v] = {}

        # create the edge
        if label:
            self.nodes[u][v] = label
            self.nodes[v][u] = label
        else:
            self.nodes[u][v] = str(u) + str(v)
            self.nodes[v][u] = str(u) + str(v)

    def vertices(self):
        """
        :return: A set of vertices in the graph
        """
        data = set()
        for key in self.nodes.keys():
            data.add(key)
        return data

    def edges(self):
        """
        Returns the set of edges of the graph.
        :return:
        """
        edges = []

        for vertex in self.nodes.keys():
            for adj in self.nodes[vertex].keys():
                edge_list = sorted([vertex, adj])
                if edge_list not in edges:
                    edges.append(edge_list)
                else:
                    pass

        return edges

    def is_edge(self, u, v):
        """
        Checks if an edge exists
        :param u: first vertex
        :param v: second vertex
        :return: True if the edge exists else return a statement saying it doesnt exist.
        """
        if sorted([u, v]) in self.edges():
            return True
        else:
            return 'This edge does not exist'

    def deg(self, v):
        """
        Degree is the number of edges adjacent to a vertex.
        :param v: the vertex we are interested in getting the degree
        :return:
        """
        # first check if the vertex exists
        if v not in self.nodes:
            return 'This vertex does not exist. Use the add_vertex method to add a vetex.'
        else:
            degree = len(self.nodes[v].values())
            return degree

