""" classes and functions for binary trees 
"""

from 队列的实现方式.PrioQueue import PrioQueue
from 图.Graph import *


# Kruskal 算法 最小生成树问题
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):  # put all edges into a list
        for v, w in graph.out_edges(vi):
            edges.append((w, (vi, v)))
    edges.sort()  # sort, O(n log n) time
    for w, e in edges:
        if reps[e[0]] != reps[e[1]]:
            mst.append((e, w))
            if len(mst) == vnum - 1: break
            rep, orep = reps[e[0]], reps[e[1]]
            for i in range(vnum):
                if reps[i] == orep: reps[i] = rep
    return mst


# Prim 算法 最小生成树问题
def Prim(graph):
    """ Assume that graph is a network, a connected undirect
graph. This function implements Prim algorithm to build its
minimal span tree. A list mst to store the resulting
span tree, where each element takes the form ((i, j), w).
A representing array reps is used to record the representive
vertics of each of the connective parts.
"""
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQueue([(0, 0, 0)])  # record cand-edges (w, vi, wj)
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, vmin = cands.dequeue()  # take minimal candidate edge
        if mst[vmin]: continue  # vmin is already in mst
        mst[vmin] = ((u, vmin), w)  # record new MST edge and vertex
        count += 1
        for v, w in graph.out_edges(vmin):  # for adjacents of vmin
            if not mst[v]:  # when v is not in mst yet
                cands.enqueue((w, vmin, v))
    return mst

# def Prim2(graph):
#     vnum = graph.vertex_num()
#     wv_seq = [[graph.get_edge(0, v), v, 0] for v in range(vnum)]
#     connects = DecPrioHeap(wv_seq) # 最近连接的顶点堆， |V| 个元素
#     mst = [None]*vnum
#     while not connects.is_empty():
#         w, mv, u = connects.getmin() # 取得最近顶点和连接边
#         if w == infinity: break # 最近顶点已不连通，说明该图没有生成树
#         mst[mv] = ((u, mv), w) # 这就是新的 MST 边
#         for v, w in graph.out_edges(mv): # 检查 mv 的邻接边
#             if not mst[v] and w < connects.weight(v):  # 如果更短就修改
#                 connects.dec_weight(v, w, mv)
#     return mst

inf = float("inf")

if __name__ == '__main__':
    gmat3 = [[0, 10, inf, inf, 19, 21],
             [10, 0, 5, 6, inf, 11],
             [inf, 5, 0, 6, inf, inf],
             [inf, 6, 6, 0, 18, 14],
             [19, inf, inf, 18, 0, 7],
             [21, 11, inf, 14, 7, 0]]

    gmat4 = [[0, 10, inf, inf, 19, 21],
             [10, 0, 5, 6, inf, 11],
             [inf, 5, 0, 6, inf, inf],
             [inf, 6, 6, 0, 18, 14],
             [19, inf, inf, 18, 0, 33],
             [21, 11, inf, 14, 33, 0]]

    g3 = GraphA(gmat3, inf)
    g4 = GraphA(gmat4, inf)

    spt1 = Kruskal(g3)
    print(spt1)

    spt2 = Prim(g3)
    print(spt2)

    spt3 = Kruskal(g4)
    print(spt3)

    spt4 = Prim(g4)
    print(spt4)
