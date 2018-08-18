""" a queue class implemented using Python list
"""

class QueueUnderflow(ValueError):
    pass

class SQueue(object):
    def __init__(self, init_len=8):
        self.len = init_len  # length of mem-block
        self.elems = [0] * init_len
        self.head = 0  # index of head element
        self.elnum = 0  # number of elements

    def is_empty(self):
        return self.elnum == 0

    def first(self):
        if self.elnum == 0:
            raise QueueUnderflow
        return self.elems[self.head]

    # 出队
    def dequeue(self):
        if self.elnum == 0:
            raise QueueUnderflow
        e = self.elems[self.head]
        self.head = (self.head + 1) % self.len
        self.elnum -= 1
        return e

    # 入队
    def enqueue(self, elem):
        if self.elnum == self.len:
            self.__extend()
        self.elems[(self.head + self.elnum) % self.len] = elem
        self.elnum += 1

    # 扩张存储区
    def __extend(self):
        old_len = self.len
        self.len *= 2
        new_elems = [0] * (self.len)
        for i in range(old_len):
            new_elems[i] = self.elems[(self.head + i) % old_len]
        self.elems, self.head = new_elems, 0


if __name__ == '__main__':
    q = SQueue()
    for i in range(10):
        q.enqueue(i * 3)
    print(q.dequeue())
    q.enqueue(100)
    while not q.is_empty():
        print(q.dequeue())
