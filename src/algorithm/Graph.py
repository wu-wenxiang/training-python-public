""" topological sort of direct graph 
"""

infinity = float("inf")


class AdjGraphError(TypeError):
    pass


# 图的邻接矩阵实现
class Graph:  # basic graph class, using adjacent matrix
    def __init__(self, mat, unconn=0):
        vnum1 = len(mat)
        for x in mat:
            if len(x) != vnum1:  # Check square matrix
                raise ValueError("Argument for 'GraphA' is bad.")
        self.mat = [mat[i][:] for i in range(vnum1)]
        self.unconn = unconn
        self.vnum = vnum1

    def vertex_num(self):
        return self.vnum

    def add_edge(self, vi, vj, val=1):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        self.mat[vi][vj] = val

    def add_vertex(self):
        raise AdjGraphError(
            "Adj Matrix does not support 'add_vertex'")

    def get_edge(self, vi, vj):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        return self.mat[vi][vj]

    def out_edges(self, vi):
        assert 0 <= vi < self.vnum
        return self._out_edges(self.mat, vi, self.unconn)

    @staticmethod
    def _out_edges(mat, vi, unconn):
        edges = []
        row = mat[vi]
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + "\n".join(map(str, self.mat)) + "\n]" \
               + "\nUnconnected: " + str(infinity)


# 图的链接表实现
class GraphA(Graph):
    def __init__(self, mat, unconn=0):
        vnum1 = len(mat)
        for x in mat:
            if len(x) != vnum1:  # Check square matrix
                raise ValueError("Argument for 'GraphA' is bad.")
        self.mat = [Graph._out_edges(mat, i, unconn)
                    for i in range(vnum1)]
        self.vnum = vnum1
        self.unconn = unconn

    def add_vertex(self):  # For new vertex, return an index allocated
        self.mat.append([])
        self.vnum += 1
        return self.vnum

    def add_edge(self, vi, vj, val=1):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        row = self.mat[vi]
        for i in range(len(row)):
            if row[i][0] == vj:  # replace a value for mat[vi][vj]
                self.mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj: break
        else:
            i += 1  # adjust for the new entry at the end
        self.mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum
        for i, val in self.mat[vi]:
            if i == vj: return val
        return self.unconn

    def out_edges(self, vi):
        assert 0 <= vi < self.vnum
        return self.mat[vi]


if __name__ == '__main__':
    ##    g1 = Graph(10)
    ##    g2 = Graph(10, infinity)
    ##    print(str(g1))
    ##    print(str(g2))

    gmat = [[0, 0, 3, 4], [2, 0, 0, 0], [4, 1, 0, 0], [2, 0, 1, 0]]

    g3 = GraphA(gmat, 0)
    g3.add_edge(0, 3, 5)
    g3.add_edge(1, 3, 6)
    g3.add_edge(3, 1, 9)
    print(str(g3))
