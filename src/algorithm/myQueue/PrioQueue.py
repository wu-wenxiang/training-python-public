# This file contains two
# implementations of priority queues:
# 1, as sorted list
# 2, as heap stored in a list
# and in addition,
# an implementation of heap sort function

class PrioQueueError(ValueError):
    pass


class PrioQue(object):
    """ Implementing binary trees as sorted list
    """

    def __init__(self, elist=[]):
        self.elems = list(elist)
        self.elems.sort()
    
    def is_empty(self):
        return self.elems == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self.elems[len(self.elems) - 1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self.elems.pop()

    def enqueue(self, e):
        i = len(self.elems) - 1
        while i >= 0:
            if self.elems[i] <= e:
                i -= 1
            else:
                break
        self.elems.insert(i + 1, e)


class PrioQueue(object):
    """ Implementing binary trees as heaps
    """

    def __init__(self, elist=[]):
        self.elems = list(elist)
        if elist != []:
            self.buildheap()
    
    def __repr__(self):
        return '; '.join(str(i) for i in self.elems)


    def is_empty(self):
        return self.elems == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self.elems[0]

    def enqueue(self, e):
        self.elems.append(None)  # add a dummy element
        self.siftup(e, len(self.elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self.elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        elems = self.elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self.elems, begin, begin * 2 + 1
        while j < end:  # invariant: j == 2*i+1
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1  # elems[j] <= its brother
            if e < elems[j]:  # e is the smallest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self.elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self.elems[i], i, end)


def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:  # invariant: j == 2*i+1
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1  # elems[j] <= its brother
            if e < elems[j]:  # e is the smallest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2 * j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)


from random import randint

def test1():
    print("Test class PrioQue:")
    pq = PrioQue()
    for i in range(12):
        pq.enqueue(randint(0, 30))
    while not pq.is_empty():
        print(pq.dequeue())

def test2():
    print("Test class PrioQueue:")
    pq = PrioQueue()
    for i in range(12):
        pq.enqueue(randint(0, 30))
    while not pq.is_empty():
        print(pq.dequeue())

def test3():
    print("Test function heap_sort:")
    lst = [randint(1, 30) for i in range(15)]
    print(lst)
    heap_sort(lst)
    print(lst)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    pass
