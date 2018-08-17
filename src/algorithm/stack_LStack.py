from myList.LNode import LNode


class StackUnderflow(ValueError):
    pass


# 借用LNode类实现链接栈
class LStack():  # stack implemented as a linked node list
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def top(self):
        if self.top is None:
            raise StackUnderflow
        return self.top.elem

    def push(self, elem):
        self.top = LNode(elem, self.top)

    def pop(self):
        if self.top is None:
            raise StackUnderflow
        e = self.top.elem
        self.top = self.top.next
        return e


if __name__ == '__main__':
    pass
