import copy
import numpy as np
import itertools
import random


# the graph class to be used to solve the puzzle
class Graph:
    """
    A class created for an undirected graph.
    The graph class uses a dict-of-dict data structure.
    A graph stores vertices and edges. Edges are undirected but can be named.
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

    def add_edge(self, u, v, name=None):
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
        if name:
            self.nodes[u][v] = name
            self.nodes[v][u] = name
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

    # To find the shortest path to the solution of the puzzle, we will first implement a breadth first search algorithm
    def breadth_first_search(self, start, dest, pred, dist):
        """
        param start: start vertex
        param dest: destination vertex
        param dist: a dictionary containing all vertices. Stores each vertex as a key and stores the distance to
        the start vertex as a value.
        param pred: a dictionary containing all vertices. Stores each vertex as a key and stores the preceding
        vertex to the key as the value.
        """
        # A queue to maintain a list of vertices from the dictionary to be scanned.
        queue = []

        # Visited is a set that stores a vertex if it has been visited at least once in the Breadth first search.
        visited = set()  # Initially all vertices are unvisited so the set visited starts empty

        # Since no path is yet constructed dist[vertex] for all vertices is set to None
        # And all predecessors are stored as None
        for vertex in self.vertices():
            dist[vertex] = None
            pred[vertex] = None

        # We first begin by visiting the start vertex. Logically, distance from start to itself should be 0
        visited.add(start)
        dist[start] = 0
        queue.append(start)

        # The standard BFS algorithm
        while len(queue) != 0:  # while queue is not empty
            u = queue.pop(0)
            for key in self.nodes[u].keys():  # Iterate through each vertex connected to u.

                if key not in visited:  # Only inspect vertices that have not already been visited.
                    visited.add(key)  # Vertex is now added to the visited set
                    dist[key] = dist[u] + 1  # distance from vertex(key) to start vertex is updated
                    pred[key] = u  # vertex(u) is updated as the predecessor of vertex(key)
                    queue.append(key)  # vertex key is added to the queue so it can be visited

                    # We stop BFS when we find destination.
                    if key == dest:
                        return True

        return False

    def shortest_path(self, start, dest):
        """
        Function uses the breadth first search algorithm to return the shortest path from start to destination
        :param start: The start vertex
        :param dest: The destination vertex
        :return: Returns the length of the shortest path as an integer and a list that shows the walk from start to
        destination using the shortest path
        """

        dist = {}  # A dictionary that stores all vertices in the graph as keys. It stores the distance from each
        # vertex to the destination  as the value.
        pred = {}  # This dictionary helps in determining the shortest path walk. It stores the proceeding vertex to
        # each vertex while taking the shortest path.

        if self.breadth_first_search(start, dest, pred, dist) is False:
            return "Start and destination not connected"

        length_shortest_path = dist[dest]

        path = [dest]
        walk = dest

        while pred[walk] is not None:
            # pred[walk] is None if that vertex was not visited during the breadth first search.
            path.append(pred[walk])
            walk = pred[walk]

        shortest_path = path[::-1]

        print("The shortest path: ", shortest_path)
        print("Length of shortest path: ", length_shortest_path)

    # To find the connected components of G
    def connected_group(self, vertex, visited):
        """
        :param vertex: Current vertex we are walking from.
        :param visited: A set that contains vertices we have already visited.
        :return: returns a list called result. Result contains all elements in a connected group.
        """
        result = []  # This list stores the connected components of each connected group
        vertices = {vertex}  # This contains the vertices we will visit in the while loop
        while vertices:  # while the vertices set is not empty, the loop continues.
            node = vertices.pop()
            visited.add(node)  # add the vertex to visited so we do not visit it again.
            vertices.update(
                n for n in self.nodes[node].keys() if n not in visited)  # if we haven't already encountered a
            # vertex, we store it in the vertices set so we can look at it's connected component
            result.append(node)
        return result

    def connected_components(self):
        """This function returns all the connected components of a graph.
        :return: the connected components of the graph as a nested list. Each sublist in the nested list is a connected
        component. If the function returns a nested list with only one sublist, it means the entire graph is connected.
        """
        # Visited is a set that stores a vertex if it has been visited at least once in the search.
        visited = set()  # Initially all vertices are unvisited so the set visited starts empty
        c_c = []  # This is a nested list that contains sublists of the connected components of the graph.
        for vertex in self.nodes.keys():
            # Iterate through each vertex in the graph and apply a depth first search to it if it has not been visited
            if vertex not in visited:
                result = self.connected_group(vertex, visited)
                c_c.append(result)
        return c_c


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


if __name__ == '__main__':
    G = Graph()
    # We can now use the shortest_path method to solve the puzzle.
    # THE CODE TAKES ABOUT 14 SECONDS TO RUN
    create_edges(G)

    # This creates a random configuration of numbers 1 to 8
    x = random.sample(range(1, 9), 8)
    random_start = np.array(x).reshape(2, 4)
    print("We are starting from: ", random_start)
    print("")

    # The destination is the [[1, 2, 3, 4], [5, 6, 7, 8]]
    destination = np.arange(1, 9).reshape(2, 4)
    print("Destination is:", destination)
    print("")

    G.shortest_path(start=str(random_start), dest=str(destination))

    # Because our graph is a very large one with over 40000 vertices, I can instead just find out how many sublist our
    # connected components have. The result determines if our graph is strongly connected or not.
    print(len(G.connected_components()))