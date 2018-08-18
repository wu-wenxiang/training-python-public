from LCList import LCList
'''
问题：设有 n 个人围坐一圈，现在从第 k 个人开始报数，
报到第 m 的人退出。然后继续报数，直至所有人退出。
输出出列人顺序编号
'''


# Josephus问题：数组算法
def JosephusA(n, k, m):
    people = list(range(1, n + 1))
    num, i = 0, k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    return

# Josephus问题：连续表算法
def JosephusL(n, k, m):
    people = list(range(1, n + 1))
    if k < 1 or k > n:
        raise ValueError

    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end="")
        if num > 1:
            print(", ", end="")
        else:
            print("")
    return


# Josephus问题：循环链表算法
class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while not self.isEmpty():
            self.turn(m - 1)
            print(self.pop(), end="")
            if not self.isEmpty():
                print(", ", end="")
            else:
                print("")


# end class Josephus

if __name__ == '__main__':
    s = input("Josephus parameters (n k m): ")
    n, k, m = map(int, s.split())
    JosephusA(n, k, m)
    JosephusL(n, k, m)
    Josephus(n, k, m)
