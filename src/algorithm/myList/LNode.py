# 自定义单链节点
class LNode:
    def __init__(self, elm, nxt):
        self.elem = elm
        self.next = nxt


if __name__ == '__main__':
    llist1 = LNode(1, None)
    pnode = llist1

    # 构造一个链表
    for i in range(2, 11):
        pnode.next = LNode(i, None)
        pnode = pnode.next

    # 输出一个链表
    pnode = llist1
    while pnode != None:
        print(pnode.elem)
        pnode = pnode.next
