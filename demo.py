from graph import Node, Graph
from pagerank import pagerank
import os

# Uncomment the memory_usage_psutil call and its call to see the memory usage after installing the psutil package 'pip install psutil'

# calculate how memory much memory is used
# def memory_usage_psutil():
#     # return the memory usage in MB
#     import psutil
#     process = psutil.Process(os.getpid())
#     mem = process.memory_info()[0] / float(2 ** 20)
#     print('MEMORY USED:', mem, 'MB')
#     return mem

# import text file, first column is the node name and the second column is the node name that it is connected to
def import_file(file_name):
    nodes = {}
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            node_name, connected_node = line.split()
            if node_name not in nodes:
                nodes[node_name] = Node()
            if connected_node not in nodes:
                nodes[connected_node] = Node()
            nodes[node_name].add_outbound_edge(nodes[connected_node])
    return nodes

# create a graph from the nodes
def create_graph(nodes):
    graph = Graph()
    for node_name, node in nodes.items():
        graph.add_node(node_name, node)
    return graph


g = create_graph(import_file('dataset.txt'))

ranks = pagerank(g)

# sort the ranks by their score and print them out
sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)

while True:
    try:
        number_of_nodes_to_print = int(
            input('How many nodes would you like to print? '))
        break
    except:
        print('Please enter a number')

i = 0
for node, rank in sorted_ranks:
    # print only top 10 nodes
    if i < number_of_nodes_to_print:
        print('node name:', node.name, 'score:', rank, 'rank:', i + 1)
        i += 1
    if i == number_of_nodes_to_print:
        break

# memory_usage_psutil()
