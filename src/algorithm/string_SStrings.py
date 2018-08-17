# Naive string matching

# KMP 字符串匹配算法

def naive_matching(t, p):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i==m means a matching
        if t[j] == p[i]:  # ok! consider next char in p
            j, i = j + 1, i + 1
        else:  # no! consider next position in t
            j, i = j - i + 1, 0
    if i == m:  # find a matching, return its index
        return j - i
    return -1  # no matching, return special value


## KMP string matching
# 关键，预处理模式串，得到匹配数组
def gen_pnext0(p):
    """ Generate a list for the next checking index
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:  # generate pnext[i+1]
        while k >= 0 and p[i] != p[k]:
            k = pnext[k]
        i, k = i + 1, k + 1
        pnext[i] = k  # set a pnext entry
    return pnext


# 关键，预处理模式串，得到匹配数组
# 优化的写法
def gen_pnext(p):
    """ Generate a list for the next checking index,
    a little revised version.
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:  # generate pnext[i+1]
        while k >= 0 and p[i] != p[k]:
            k = pnext[k]
        i, k = i + 1, k + 1
        if p[i] == p[k]:  # 当两个字符相等时要跳过
            pnext[i] = pnext[k]
        else:
            pnext[i] = k
    return pnext


def KMPmatching(t, p, pnext):
    """ KMP string mateching, the main function."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i==m means a matching
        if i == -1 or t[j] == p[i]:  # consider next char in p
            j, i = j + 1, i + 1
        else:  # no! consider pnext char in p
            i = pnext[i]
    if i == m:  # find a matching, return its index
        return j - i
    return -1  # no matching, return special value


def KMPmatching1(t, p, pnext):
    """ KMP string matching, a little revised version."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i==m means a matching
        while i >= 0 and t[j] != p[i]:
            i = pnext[i]
        j, i = j + 1, i + 1
    if i == m:  # find a matching, return its index
        return j - i
    return -1  # no matching, return special value


def matching(t, p):
    return KMPmatching(t, p, gen_pnext0(p))


def matching1(t, p):
    return KMPmatching1(t, p, gen_pnext0(p))


t = "BBC ABCDAB ABCDABCDABDE"
p = "ABCDABD"

if __name__ == '__main__':
    print(matching1(t, p))
