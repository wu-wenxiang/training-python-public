from LNode import LNode


# 单链表
class LList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # 前加
    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e

    # 后加
    def append(self, elem):
        if self.head is None:
            self.head = LNode(elem, None)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None)

    def poplast(self):
        if self.head is None:  # empty list
            raise ValueError
        p = self.head
        if p.next is None:  # list with only one element
            e = p.elem;
            self.head = None
            return e
        while p.next.next is not None:  # till p.next be last node
            p = p.next
        e = p.next.elem;
        p.next = None
        return e

    def find(self, pred):
        p = self.head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
        return None

    def printall(self):
        p = self.head
        while p is not None:
            print(p.elem)
            p = p.next


if __name__ == '__main__':
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()
