
# coding: utf-8

# In[19]:

# We use the NetworkX package 
import networkx as nx
import matplotlib.pyplot as plt


# In[54]:

# Setting up a demo graph according to Q1
G = nx.Graph()
committees = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(committees)

# edges_A = [('A', 'C'), ('A', 'E'), ('A', 'G'), ('A', 'D'), ('A', 'B')]

G.add_edges_from([('A','B'), ('A','C'), ('A','D'), ('A','E'), ('A','G')]) # adds edges of A
G.add_edges_from([('B','E')])
G.add_edges_from([('C','G')])
G.add_edges_from([('D','G')])
G.add_edges_from([('E','G')])
G.add_edges_from([('F','G'), ('F','H')])
G.add_edges_from([('G','H')])

color_map = ['blue', 'green', 'red', 'blue', 'blue', 'green', 'red', 'blue']
color_map_2 = ['blue', 'green', 'gold']
color_map_3 = {'A' : 'gold'}

# now we try to write a colouring algorithm

nx.draw(G, node_color = color_map, with_labels = True) # this draws the graph

nx.coloring.greedy_color(G)


# In[72]:

# default = []
# for i in range(len(G)):
#     default.append(0)

# colors = dict( zip(G.nodes(), default) )
# print(colors)

# Just iterates through the nodes in order and colours with first available color
def color_graph_1( graph ):
    # Initialize dictionary of nodes-colors
    zeroes = []
    for i in range(len(graph)):
        default.append(0)
    colors = dict( zip(G.nodes(), default) )
    
    # Begin coloring the graph, one vertex at a time
    for node in graph:
        # Pick the first color (nat) that does not conflict with the existing coloring of its neighbors
        adjacent_colors = set()
        for n in graph.neighbors(node):
            adjacent_colors.add( colors[n] )
        i = 1
        while i in adjacent_colors:
            i = i + 1
        colors[node] = i
        
    # Returns final coloring of graph
    return colors

coloring_1 = color_graph_1(G)
print coloring_1

chromatic_number_1 = max( coloring_1.values() )
print chromatic_number_1
        



# In[74]:

# Iterates through the nodes in order from largest to degree to smallest degree
def color_graph_2( graph ):
    # Make a dictionary of nodes-degrees
    degrees = dict()
    for node in graph:
        degrees[node] = graph.degree(node)
    print degrees # To debug
    
    # Initialize dictionary of nodes-colors
    zeroes = []
    for i in range(len(graph)):
        default.append(0)
    colors = dict( zip(G.nodes(), default) )
    
    # Iterates through nodes of graph in descending order according to degree
    for node in sorted(degrees, key = lambda node : degrees[node], reverse = True):
        print node # To debug
        
        # Pick the first color (nat) that does not conflict with the existing coloring of its neighbors
        adjacent_colors = set()
        for n in graph.neighbors(node):
            adjacent_colors.add( colors[n] )
        i = 1
        while i in adjacent_colors:
            i = i + 1
        colors[node] = i
        
    # Returns final coloring of graph
    return colors 

coloring_2 = color_graph_2(G)
print coloring_2

chromatic_number_2 = max( coloring_2.values() )
print chromatic_number_2



# In[75]:

# Random testing code

b = {'one': 1, 'two': 2, 'three': 3}

sorted(b, key = lambda e : e[0], reverse=True)


# In[ ]:



