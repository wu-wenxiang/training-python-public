""" topological sort of direct graph 
"""

from 图.Graph import *

from 栈的实现.SStack import SStack


# Generate the DFS sequence of rearchable vertices from v0
def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges))
            if visited[v] == 0: # unvisited node
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq

# Genarate span-forest of a graph, recursive definition
def DFS_span_tree(graph):
    vnum = graph.vertex_num()
    span_forest = [None]*(vnum)
    def dfs(graph, v):  # 递归遍历函数，在递归中记录经由边
        nonlocal span_forest  # 要操作 nonlocal 变量 span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest

if __name__ == '__main__':
    gmat1 = [[0,1,1,0,0,0,0,0],
             [1,0,0,1,1,0,0,0],
             [1,0,0,0,0,1,1,0],
             [0,1,0,0,0,0,0,1],
             [0,1,0,0,0,0,0,1],
             [0,0,1,0,0,0,0,0],
             [0,0,1,0,0,0,0,0],
             [0,0,0,1,1,0,0,0]]

    gmat2 = [[0,1,0,1,1,1,0],
             [0,0,1,0,0,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,0,0,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,0,0],
             [0,0,1,0,0,1,0]]

    g1 = GraphA(gmat1, 0)
    dfs1 = DFS_seq(g1, 0)
    print(dfs1)

    g2 = GraphA(gmat2, 0)
    dfs2 = DFS_seq(g2, 0)
    print(dfs2, "\n")
    
    dfs_tree = DFS_span_tree(g1)
    print(dfs_tree)
    dfs_tree = DFS_span_tree(g2)
    print(dfs_tree)
    


    
    
    

