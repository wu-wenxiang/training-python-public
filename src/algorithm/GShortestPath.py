""" classes and functions for binary trees 
"""

from 队列的实现方式.PrioQueue import PrioQueue
from 图.Graph import *

inf = float("inf") # infinity

# Find nearest pathes from a single vertex to other reachable
# vertices using Dijkstra algorithm, with priority queue.
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    pathes = [None]*vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])  # 初始队列
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()  # 取路径最短顶点
        if pathes[vmin]: continue  # 如果其最短路径已知则继续
        pathes[vmin] = (u, plen)  # 记录新确定的最短路径
        for v, w in graph.out_edges(vmin):  # 考察经由新 U 顶点的路径
            if not pathes[v]:  # 是到尚未知最短路径的顶点的路径，记录它
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return pathes

# Find all nearset pathes using Floyd-Warshall algorithm
def all_shortest_paths(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)]
         for i in range(vnum)] # create a copy the adjacent matrix
    nvertex = [[-1 if a[i][j] == infinity else j
                for j in range(vnum)]
               for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return (a, nvertex)

def test_dijkstra():
    pathes0 = dijkstra_shortest_paths(g1, 0)
    pathes1 = dijkstra_shortest_paths(g1, 1)
    pathes2 = dijkstra_shortest_paths(g1, 2)
    pathes3 = dijkstra_shortest_paths(g1, 3)
    pathes4 = dijkstra_shortest_paths(g1, 4)
    pathes5 = dijkstra_shortest_paths(g1, 5)

    if (pathes0 != [(0, 0), (3, 41), (0, 10), (2, 25), (0, 45), None] or
        pathes1 != [(2, 35), (1, 0), (1, 15), (2, 30), (1, 5), None] or
        pathes2 != [(2, 20), (3, 31), (2, 0), (2, 15), (1, 36), None] or
        pathes3 != [(2, 51), (3, 16), (1, 31), (3, 0), (1, 21), None] or
        pathes4 != [(2, 81), (3, 46), (1, 61), (4, 30), (4, 0), None] or
        pathes5 != [(2, 54), (3, 19), (1, 34), (5, 3), (1, 24), (5, 0)]):
        print("Some result are not correct.")

    print("start v0:", pathes0)
    print("start v1:", pathes1)
    print("start v2:", pathes2)
    print("start v3:", pathes3)
    print("start v4:", pathes4)
    print("start v5:", pathes5)
# end test_dijkstra()

def test_floyd():
    pathes = all_shortest_paths(g1)
    print("")
    print(pathes[0])
    print(pathes[1])

if __name__ == '__main__':
    gmat4 = [[  0, 50, 10,inf, 45,inf],
             [inf,  0, 15,inf,  5,inf],
             [ 20,inf,  0, 15,inf,inf],
             [inf, 16,inf,  0, 35,inf],
             [inf,inf,inf, 30,  0,inf],
             [inf,inf,inf,  3,inf,  0]]

    g1 = GraphA(gmat4, inf)

    test_dijkstra()
    test_floyd()

