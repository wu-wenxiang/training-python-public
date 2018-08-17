from LNode import LNode


# 循环单链表
class LCList:  # class of Circular Linked List
    def __init__(self):
        self.rear = None   # 表对象只有一个 rear 域

    def isEmpty(self):
        return self.rear is None

    def prepend(self, elem):  # add element in the front end
        p = LNode(elem, None)
        if self.rear is None:
            p.next = p  # 表中第一个结点建立初始的循环链接
            self.rear = p
        else:
            p.next = self.rear.next  # 链在尾结点之后，就是新的首结点
            self.rear.next = p

    def append(self, elem):  # add element in the rear end
        self.prepend(elem)  # 直接调用前段加入操作
        self.rear = self.rear.next  # 修改 rear 使之指向新的尾结点

    def pop(self):  # pop out head element
        if self.rear is None:
            raise ValueError
        p = self.rear.next
        if self.rear is p:  # rear 等于其 next，说明表中只有一个结点
            self.rear = None  # 弹出唯一结点后 rear 置空
        else:
            self.rear.next = p.next  #一般情况，删去一个结点
        return p.elem

    # 简单输出所有元素的方法
    def printall(self):
        p = self.rear.next
        while True:
            print(p.elem)
            if p is self.rear:
                break
            p = p.next


if __name__ == '__main__':
    mlist = LCList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    # mlist1.printall()

    while not mlist.isEmpty():
        print(mlist.pop())
