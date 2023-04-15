"""
Trees:

First, import the collections module
Define a class Node to represent a node in the tree with an attribute for the node value and a list of child nodes
Define a class Tree with an attribute for the root node
Implement methods for adding nodes and searching the tree using recursion
Example code:
"""
import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
    
    def add_node(self, value, parent_value=None):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            parent_node = self.search_tree(parent_value)
            parent_node.children.append(node)
        
    def search_tree(self, value, node=None):
        if node is None:
            node = self.root
        if node.value == value:
            return node
        else:
            for child in node.children:
                found_node = self.search_tree(value, child)
                if found_node is not None:
                    return found_node
        return None
"""
Graphs:

First, import the collections module
Define a class Graph to represent the graph with a dictionary of vertices and a list of edges
Implement methods for adding vertices and edges, and searching the graph using recursion
Example code:
"""
import collections

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    
    def add_vertex(self, value):
        self.vertices[value] = []
        
    def add_edge(self, start_value, end_value):
        self.edges.append((start_value, end_value))
        self.vertices[start_value].append(end_value)
        
    def search_graph(self, start_value, end_value, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_value)
        if start_value == end_value:
            return True
        else:
            for neighbor in self.vertices[start_value]:
                if neighbor not in visited:
                    found = self.search_graph(neighbor, end_value, visited)
                    if found:
                        return True
        return False
"""
Sets:
Sets are built-in to Python and can be created using curly braces or the set() constructor
You can perform various set operations such as union, intersection, difference, and symmetric difference
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
