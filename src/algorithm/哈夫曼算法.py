""" classes and functions for binary trees 
"""

from 队列的实现方式.PrioQueue import PrioQueue
from 树.BiTree1 import BiTNode, print_BiTNodes

class HTNode(BiTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self): return self.num

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w, None, None))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()

if __name__ == '__main__':

##    t = BiTNode(1, BiTNode(2, None, None), BiTNode(3, None, None))
##    print_BiTNodes(t)
##    print("\n")

    h = HuffmanTree([2, 3, 7, 10, 4, 2, 5])
    print_BiTNodes(h)

    pass

