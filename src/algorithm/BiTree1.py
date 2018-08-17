""" classes and functions for binary trees 
"""


class BiTNodeError(ValueError):
    pass


class BiTNode:
    def __init__(self, dat, left, right):
        self.data = dat
        self.left = left
        self.right = right


def count_BiTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BiTNodes(t.left) + count_BiTNode(t.right)


def sum_BiTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BiTNodes(t.left) + sum_BiTNodes(t.right)


def preorder(t, proc):
    if t is None: return
    assert (isinstence(t, BiTNode))
    proc(t.data)
    preorder(t.left)
    preorder(t.right)


def inorder(t, proc):
    if t is None: return
    inorder(t.left)
    proc(t.data)
    inorder(t.right)


def postorder(t, proc):
    if t is None: return
    postorder(t.left)
    postorder(t.right)
    proc(t.data)


from 队列的实现方式.SQueue import *


def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        n = q.dequeue()
        if t is None: continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.data)


from 栈的实现.SStack import *


def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # go down along left chain
            s.push(t.right)  # push right branch into stack
            proc(t.data)
            t = t.left
        t = s.pop()  # left chain ends, backtrack


def preorder_iter(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


def inorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


# 非递归的后根序遍历算法
def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # iterate until top has no child
            s.push(t)
            t = t.left if t.left is not None else t.right
            # if we can go left, go, otherwise, go right
        t = s.pop()  # get the node to be access
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right  # end of left visit, turn right
        else:
            t = None  # end of right visit, force to backtrack


def print_BiTNodes(t):
    if t is None:
        print("^", end="")
        return
    print("(" + str(t.data), end="")
    print_BiTNodes(t.left)
    print_BiTNodes(t.right)
    print(")", end="")


class BiTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def preorder_iter(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == '__main__':
    pass
