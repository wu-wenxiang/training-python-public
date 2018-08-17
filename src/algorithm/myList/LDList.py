from LNode import LNode
from LList1 import LList1


# 定义一个新结点类
class LDNode(LNode):  # class of Double Linked Nodes
    def __init__(self, prev, elem, nxt):
        LNode.__init__(self, elem, nxt)
        self.prev = prev  # 扩充了一个前一结点指针


# 双链表
class LDList(LList1):  # class of Double Linked List
    def __init__(self):
        LList1.__init__(self)  # 基于带尾结点引用的单链表派生一个双链表类

    # 加入元素的一对操作
    def prepend(self, elem):
        p = LDNode(None, elem, self.head)
        self.head = p
        if self.rear is None:  # insert in empty list
            self.rear = p
        else:  # otherwise, create the prev reference
            p.next.prev = p

    # 加入元素的一对操作
    def append(self, elem):  # 与 prepend 对称
        p = LDNode(self.rear, elem, None)
        self.rear = p
        if self.head is None:  # insert in empty list
            self.head = p
        else:  # otherwise, create the next reference
            p.prev.next = p

    # 弹出（删除）元素
    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next  # 删除当前首结点
        if self.head is None:
            self.rear = None  # 如果删除后表空，把 rear 也置空
        else:
            self.head.prev = None  # 首结点的 prev 链接置空
        return e

    # 与 pop 对称
    def poplast(self):
        if self.head is None:
            raise ValueError
        e = self.rear.elem
        self.rear = self.rear.prev
        if self.rear is None:
            self.head = None  # 删除后表空，把 head 也置空
        else:
            self.rear.next = None
        return e


if __name__ == '__main__':
    mlist = LDList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    # mlist1.printall()

    while not mlist.isEmpty():
        print(mlist.pop())
        if not mlist.isEmpty():
            print(mlist.poplast())
