import re

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
    def __repr__(self):
        ret = '(%s<-%s->%s)' % (self.lchild, self.elem, self.rchild)
        ret = ret.replace('None<-', '')
        ret = ret.replace('->None', '')
        ret = re.sub(r'\((\d+)\)', r'\1', ret)
        return ret

def buildTree(preOrder, inOrder):
    if not preOrder:
        return
    root = preOrder[0]
    index = inOrder.index(root)
    ltreeInOrder = inOrder[:index]
    ltreePreOrder = preOrder[1:index+1]
    rtreeInOrder = []
    rtreePreOrder = []
    if index+1 < len(inOrder):
        rtreeInOrder = inOrder[index+1:]
        rtreePreOrder = preOrder[index+1:]
#     print(root, ltreeInOrder, rtreeInOrder)
#     print(root, ltreePreOrder, rtreePreOrder)
    ltree = buildTree(ltreePreOrder, ltreeInOrder)
    rtree = buildTree(rtreePreOrder, rtreeInOrder)
    return Node(root, ltree, rtree)

def later_rec(root):
    if root == None:
        return
    later_rec(root.lchild)
    later_rec(root.rchild)
    postOrderList.append(root.elem)

class MyStack(list):
    def push(self, x):
        self.append(x)
    def pull(self):
        return self.pop()

def _searchList(root, a):
    if not root:
        return False
    if root.elem == a:
        return True
    return _searchList(root.lchild, a) or _searchList(root.rchild, a)

def searchList(root, a, b):
    return _searchList(root, a) and _searchList(root, b)

def findNearestPreNode(root, a, b):
    node = root
    while node:
        if searchList(node.lchild, a, b):
            node = node.lchild
        elif searchList(node.rchild, a, b):
            node = node.rchild
        else:
            return node.elem

if __name__ == '__main__':
    preOrder = open('preOrder.txt').read().split(',')
    preOrder = list(map(int, preOrder))
    inOrder = open('inOrder.txt').read().split(',')
    inOrder = list(map(int, inOrder))
#     print(preOrder, inOrder)
    root = buildTree(preOrder, inOrder)
    print(root)
    postOrderList = []
    later_rec(root)
    postOrder = ','.join(map(str, postOrderList))
    print(postOrder)
    
#     print(_searchList(root, 6))
    print(findNearestPreNode(root, 6, 8))
    