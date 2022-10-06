from graph import Node, Graph
from pagerank import pagerank
import os


# calculate how memory much memory is used
def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    print('MEMORY USED:', mem, 'MB')
    return mem


a = Node()
b = Node()
c = Node()
d = Node()

g = Graph()

g.add_node('a', a)
g.add_node('b', b)
g.add_node('c', c)
g.add_node('d', d)

g.add_edge('b', 'c')
g.add_edge('b', 'a')
g.add_edge('c', 'a')
g.add_edge('d', 'a')
g.add_edge('d', 'b')
g.add_edge('d', 'c')

ranks = pagerank(g)

for node, value in ranks.items():
    print(node.name, value)

memory_usage_psutil()
