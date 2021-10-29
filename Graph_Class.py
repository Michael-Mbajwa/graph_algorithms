import copy
import numpy as np
import itertools


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

    def add_edge(self, u, v):
        """
        Adds an edge between vertices u and v
        :param u: Must be provided. If u doesn't exist, it will be created
        :param v: Must be provided. If v doesn't exist, it will be created
        :param name: Refers to the name of the edge. Default value is None.
        """
        if u not in self.nodes:
            self.nodes[u] = {}
        if v not in self.nodes:
            self.nodes[v] = {}

        # create the edge
        self.nodes[u][v] = str(u) + str(v)
        self.nodes[v][u] = str(v) + str(u)

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


# To test the graph class, we can create a simple graph
if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'd')
    g.add_edge('c', 'b')
    print(len(g))
    print(g.number_of_vertices())
    print(g.vertices())
    print(g.edges())
    print(g.deg('b'))
    print(g.is_edge('b', 'a'))
    print(g.nodes)
    print(g['a']['b'])


# QUESTION 2
# Puzzle
def rotate_square(z, i, j):
    """
    A function for rotating squares in a 2d array with 8 checkers. Since we are dealing with a 2D array, the function
    takes as arguments the two indexes from the row and column that make a square. For example:
    [[1 2 3 4]
    [5 6 7 8]] for a 2D array with this configuration, providing i=0 and j=1, would mean you are interested in the index
    0 and index 1 from both the row and column. In this case, it would mean: [[1 2], [5 6]].
    :param z: The 8 checkers matrix with which we rotate a square.
    :param i: index of a checker
    :param j: index of second checker
    :return: Returns the 8 checkers matrix with one square rotated.
    """
    y = copy.deepcopy(z)  # Creates a deep copy of the provided vertex.
    arr = np.array([y[0][i], y[0][j], y[1][i], y[1][j]]).reshape(2, 2)  # This code picks out the square of four
    # numbers to be rotated
    rot_arr = np.rot90(arr, 3, (0, 1))  # The code uses the numpy rotate method to rotate the square
    # Adjust the matrix y
    y[0][i] = rot_arr[0][0]
    y[0][j] = rot_arr[0][1]
    y[1][i] = rot_arr[1][0]
    y[1][j] = rot_arr[1][1]

    return y


def create_edges(graph):
    """
    This function creates edges between two vertices if and only if one is obtained from the other by a single rotation.
    The function selects three squares from each vertex and rotates it.
    :param graph: The graph on which we will create edges.
    """
    vertices = np.array([np.array(vtx).reshape(2, 4) for vtx in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8])])
    # The vertices represent all the possible combinations of numbers from 1-8.
    for vertex in vertices:
        # We loop through each vertex
        rotations = [(0, 1), (1, 2), (2, 3)]
        for i, j in rotations:
            # Three different squares in each vertex are rotated and an edge is created between the new vertex gotten
            # from the rotation and the original vertex that was rotated.
            rotated_vertex = rotate_square(vertex, i, j)
            graph.add_edge(str(vertex), str(rotated_vertex))


def binary_search(a_list, item):
    # A customized binary search algorithm for 2D Numpy arrays. Super fast.
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if np.array_equal(a_list[midpoint], item):
            found = True
            return midpoint
        else:
            if item[0][0] < a_list[midpoint][0][0]:
                last = midpoint - 1
            elif item[0][0] == a_list[midpoint][0][0]:
                rng = len(a_list) // 6
                for i in range(-rng, rng):
                    if np.array_equal(a_list[midpoint + i], item):
                        return midpoint+i
            else:
                first = midpoint + 1


if __name__ == '__main__':
    puzzle_graph = Graph()
    create_edges(puzzle_graph)
    print(puzzle_graph.number_of_vertices())