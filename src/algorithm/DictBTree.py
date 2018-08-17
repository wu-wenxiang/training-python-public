""" Dictionary and searching 
"""

from 树.BiTree1 import BiTNode
from 栈的实现.SStack import *
from Assoc import Assoc

def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else: return entry.value
    return None

class DictBTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def preorder(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None: 
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()

    def inorder(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield(t.data)
            t = t.right

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else: return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt == None:
            self._root = BiTNode(Assoc(key,value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left == None:
                    bt.left = BiTNode(Assoc(key,value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right == None:
                    bt.right = BiTNode(Assoc(key,value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
    
    def delete(self, key):
        p, q = None, self._root # keep p the parent of q
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key: q = q.left
            else: q = q.right
        if q == None: return # key is not in the tree
        # Now q refers to key node, p is its parent or _root
        if q.left == None: # q has no left child
            if p == None: self._root = q.right # q == self._root
            elif q == p.left: p.left = q.right 
            else: p.right = q.right # here q == p.right
            return
        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right
        if p == None: self._root = q.left # q == self._root
        elif p.left == q: p.left = q.left
        else: p.right = q.left

    def print(self):
        for entry in self.inorder():
            print(entry.key, entry.value)
# END class

def build_dictBT(entries):
    dic = DictBTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic

if __name__ == '__main__':

    data = [(x, 1) for x in
            [36, 65, 18, 7, 60, 89, 43, 57, 101, 52, 74]]
    dic1 = build_dictBT(data)

    for entry in dic1.inorder():
        print(entry.key, entry.value)

    pass
        
    

