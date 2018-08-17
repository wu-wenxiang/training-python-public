from LNode import LNode


# 单链表,翻转和排序功能
class LList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e

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
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    # 表元素翻转
    def rev(self):
        p = None
        while self.head is not None:
            q = self.head
            self.head = q.next  # 摘先原来的首结点
            q.next = p
            p = q  # 将刚摘下的结点加入 p 引用的结点序列
        self.head = p  # 反转后的结点序列已经做好，重置表头链接

    # 基于移动元素的单链表排序
    def sortm(self):
        if self.head is None:
            return
        crt = self.head.next  # 从首结点之后开始处理
        while crt is not None:
            x, p = crt.elem, self.head
            while p is not crt and p.elem <= x:   # 跳过小元素
                p = p.next
            while p is not crt:   # 倒换大元素，完成元素插入的工作
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x  # 最后的回填
            crt = crt.next

    # 通过调整链接关系完成排序
    def sort(self):
        if self.head is None:
            return
        last = self.head  # 初始，排序段只有一个结点
        crt = last.next
        while crt is not None:  # 循环，一次处理一个结点
            p = self.head
            q = None  # 设置扫描指针初值
            while p is not crt and p.elem <= crt.elem:
                q = p
                p = p.next  # 顺序更新两个扫描指针
            if p is crt:  # p 是 crt 时不用修改链接，设置 last 到下一结点 crt
                last = crt
            else:
                last.next = crt.next  # 取下当前结点
                crt.next = p # 接好后链接
                if q is None:
                    self.head = crt   # 作为新的首结点
                else:
                    q.next = crt  # 或者接在表中间
            crt = last.next  # 无论什么情况， crt 总是 last 的下一结点
        # end of class LList


# list元素排序
def listSort(lst):
    for i in range(1, len(lst)):  # seg [0:0] is sorted
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:  # moving one by one
            lst[j] = lst[j - 1]  # in reversed-order
            j -= 1
        lst[j] = x


if __name__ == '__main__':
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()
    for i in range(5):
        print(mlist1.pop())
        print(mlist1.poplast())

    print('remained:')
    mlist1.printall()
    mlist1.rev()
    print('\nreversed:')
    mlist1.printall()

    mlist1.sort()
    print('\nsorted:')
    mlist1.printall()

##    list1 = [random.randint(1, 50) for i in range(20)]
##    print(list1, '\n')
##    listSort(list1)
##    print(list1)
