""" topological sort of direct graph 
"""

from 图.Graph import *

inf = float("inf")  # infinity


# We suppose that A[i][i] = unconn value
# AOV 网，拓扑排序
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq, zerov = [0] * vnum, [], -1
    for vi in range(vnum):
        for v, w in graph.out_edges(vi): indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov;
            zerov = vi
    for n in range(vnum):
        if zerov == -1: return False  # Thereis no topo-seq
        toposeq.append(zerov)
        vi = zerov;
        zerov = indegree[zerov]
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov;
                zerov = v
    return toposeq


""" generate critical path of AOE 
"""

# AOE 网，关键路径
# graph 里无边用 infinity 表示
def criticalPath(graph):
    toposeq = toposort(graph)
    if toposeq == False:
        return False  # no topo-sequence, cannot continue
    vnum = graph.vertex_num()
    ee, le = [0] * vnum, [infinity] * vnum
    crtPath = []
    setEventE(vnum, graph, toposeq, ee)
    setEventL(vnum, graph, toposeq, ee[vnum - 1], le)
    for i in range(vnum):
        for j, w in graph.out_edges(i):
            if ee[i] == le[j] - w:  # a critical action
                crtPath.append([i, j, ee[i]])
    return crtPath  # return the critical actions


def setEventE(vnum, graph, toposeq, ee):
    for k in range(vnum - 1):  # 最后一个顶点不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if ee[i] + w > ee[j]:  # 事件 j 还更晚结束?
                ee[j] = ee[i] + w


def setEventL(vnum, graph, toposeq, eelast, le):
    for i in range(vnum): le[i] = eelast
    for k in range(vnum - 2, -1, -1):  # 逆拓扑顺序, 两端顶点都不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if le[j] - w < le[i]:  # 事件 i 应更早开始?
                le[i] = le[j] - w


if __name__ == '__main__':
    gmat6 = [[0, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1, 0, 0]]

    g6 = GraphA(gmat6)

    gmat7 = [[inf, 6, 4, 5, inf, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, inf, 2, inf, inf, inf],
             [inf, inf, inf, inf, inf, inf, 9, 7, inf],
             [inf, inf, inf, inf, inf, inf, inf, 4, inf],
             [inf, inf, inf, inf, inf, inf, inf, inf, 2],
             [inf, inf, inf, inf, inf, inf, inf, inf, 4],
             [inf, inf, inf, inf, inf, inf, inf, inf, inf]]

    g7 = GraphA(gmat7, inf)

    ##    toposeq = toposort(g6)
    ##    print(toposeq)

    cp = criticalPath(g7)
    print(cp)
    pass
