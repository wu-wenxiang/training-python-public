# Algorithm

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 第 1 天 | 上午 | [lab-01 基础模型](#lab-01-基础模型) | |
| | | [lab-02 排序](#lab-02-排序) | |
| | 下午 | [lab-03 查找](#lab-03-查找) | |
| 第 2 天 | 上午 | [lab-04 图](#lab-04-图) | |
| | 下午 | [lab-05 字符串](#lab-05-字符串) | |
| | | [lab-06 递归](#lab-06-递归) | |
| 第 3 天 | 上午 | [lab-07 回溯](#lab-07-回溯) | |
| | 下午 | [lab-08 动态规划](#lab-08-动态规划) | |
| | | [lab-09 贪心算法](#lab-09-贪心算法) | |
| 第 4 天 | 上午 | [lab-10 广度优先](#lab-10-广度优先) | |
| | | [lab-11 流量与切割](#lab-11-流量与切割) | |
| | 下午 | [lab-12 NP困难](#lab-12-np困难) | |

## lab-00 Reference

- [LeetCode题目](https://leetcode-cn.com/problemset/algorithms/)
    - [部分答案](https://github.com/wu-wenxiang/Training-Python-Public/tree/master/src/leetcode)
    - 参考：[https://github.com/qiyuangong/leetcode](https://github.com/qiyuangong/leetcode)
- [timeit](https://docs.python.org/3.7/library/timeit.html)

    ```python
    def test():
        """Stupid test function"""
        L = [i for i in range(100)]

    if __name__ == '__main__':
        import timeit
        print(timeit.timeit("test()", setup="from __main__ import test"))
    ```

    ```python
    def f(x):
        return x**2
    def g(x):
        return x**4
    def h(x):
        return x**8

    import timeit
    print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
    ```

- [cProfile](https://docs.python.org/3/library/profile.html)

    ```python
    import cProfile
    import re
    cProfile.run('re.compile("foo|bar")')
    ```

## lab-01 基础模型

### lab-01-01 数组

- list vs [array](https://docs.python.org/3/library/array.html)

    ```python
    from array import array

    array('l')
    array('u', 'hello \u2641')
    array('l', [1, 2, 3, 4, 5])
    array('d', [1.0, 2.0, 3.14])
    array('d', [1.0, 2.0, 3.14]).tolist()
    ```

- [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html)
- Demo: [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

    ```python
    class Solution:
        def generate(self, numRows):
            triangle = [[1] * i for i in range(1, 3)]
            for i in range(3, numRows+1):
                old_row = triangle[i-2]
                new_row = [1] * i
                new_row[1:-1] = [i+j for i,j in zip(old_row[:-1], old_row[1:])]
                triangle.append(new_row)
            return triangle[:numRows]


    if __name__ == '__main__':
        solution = Solution()
        print(solution.generate(5))
    ```

### lab-01-02 链表

- Demo：[2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

### lab-01-03 栈

- Demo：变化，逆序转顺序
- Demo：[844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/)

    ```python
    class Solution:
        def backspaceCompare(self, S: str, T: str) -> bool:
            return self.process(S) == self.process(T)

        def process(self, aStr):
            stack = []
            for i in aStr:
                if i == '#' and stack:
                    stack.pop()
                elif i != '#':
                    stack.append(i)
            return ''.join(stack)
    ```

### lab-01-03 标准库的实现

- namedtuple：返回 tuple 的子类

    ```python
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(1, 2)
    >>> p.x
    1

    类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
    # namedtuple('名称', [属性list]):
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    ```

- deque：实现了高效插入和删除操作的双向列表（list按索引访问元素很快，但是插入和删除元素就很慢，因为list是线性存储，数据量大的时候，插入和删除效率很低）

    ```python
    >>> from collections import deque
    >>> q = deque(['a', 'b', 'c'])
    >>> q.append('x')
    >>> q.appendleft('y')
    >>> q
    deque(['y', 'a', 'b', 'c', 'x'])
    ```

    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()。栈和队列。

- defaultdict：key不存在时，返回一个默认值

    ```python
    >>> from collections import defaultdict
    >>> dd = defaultdict(lambda: 'N/A')
    >>> dd['key1'] = 'abc'
    >>> dd['key1'] # key1存在
    'abc'
    >>> dd['key2'] # key2不存在，返回默认值
    'N/A'
    ```

- Counter：计数器

    ```python
    >>> from collections import Counter
    >>> c = Counter()
    >>> for ch in 'programming':
    ...     c[ch] = c[ch] + 1
    ...
    >>> c
    Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
    >>> Counter('programming')
    Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
    >>> c['tt']
    0
    ```

## lab-02 排序

### lab-02-01 选择排序

```python
def findSmallest(a):
    s = 0
    for i, j in enumerate(a):
        if j < a[s]:
            s = i
    return s


def selectionSort(a):
    for i in range(len(a) - 1):
        s = findSmallest(a[(i + 1):]) + i + 1
        if a[i] > a[s]:
            a[i], a[s] = a[s], a[i]
    return a


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(selectionSort(myList))
```

### lab-02-02 注入比较逻辑

```python
def findSmallest(a, key=lambda x: x):
    s = 0
    for i, j in enumerate(a):
        if key(j) < key(a[s]):
            s = i
    return s


def selectionSort(a, key=lambda x: x):
    for i in range(len(a) - 1):
        s = findSmallest(a[(i + 1):], key) + i + 1
        if key(a[i]) > key(a[s]):
            a[i], a[s] = a[s], a[i]
    return a


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList, key=lambda x: str(x)))
    print(selectionSort(myList, key=lambda x: str(x)))
```

### lab-02-03 快速排序

```python
def quickSort(a):
    if len(a) < 2:
        return a
    left = quickSort([i for i in a[1:] if i <= a[0]])
    right = quickSort([i for i in a[1:] if i > a[0]])
    return left + [a[0]] + right


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(quickSort(myList))
```

### lab-02-04 归并排序

```python
def merge(l, r):
    if not l or not r:
        return l + r
    if l < r:
        return [l[0]] + merge(l[1:], r)
    else:
        return [r[0]] + merge(l, r[1:])


def mergeSort(a):
    # print(a)
    if len(a) < 2:
        return a
    m = len(a) // 2
    return merge(mergeSort(a[:m]), mergeSort(a[m:]))


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(mergeSort(myList))
```

### 堆

## lab-03 查找

### lab-03-01 二分查找

```python
import bisect


def bisearch(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return None


def bisearch2(a, x):
    left = bisect.bisect_left(a, x)
    right = bisect.bisect_right(a, x)
    if left == right:
        return None
    return left


if __name__ == '__main__':
    myList = [1, 3, 5, 7, 9, 11]
    print(bisearch(myList, 3))  # 1
    print(bisearch2(myList, 3))  # 1
    print(bisearch(myList, -1))  # None
    print(bisearch2(myList, -1))  # None
```

- Demo：[327. 区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum/)

    ```python
    from bisect import bisect_left, bisect_right, insort_right


    class Solution:
        def countRangeSum(self, nums, lower, upper):
            p = [0]
            for a in nums:
                p.append(p[-1] + a)
            walked = []
            ans = 0
            for a in p[::-1]:
                l, r = a + lower, a + upper
                i, j = bisect_left(walked, l), bisect_right(walked, r)
                ans += j - i
                insort_right(walked, a)
            return ans
    ```

### lab-03-02 二分排序

```python
import bisect


def bisort(a):
    ret = []
    for i in a:
        bisect.insort(ret, i)
    return ret


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(bisort(myList))
```

### lab-03-03 散列表：哈希查找

- Demo: [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)
    - 暴力解法：`O(n**2)`
    - 结合二分查找：`O(n*logN)`
    - 数组映射：`O(n)`
    - 字典映射：[leetcode-0001.py](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/src/leetcode/leetcode-0001.py)
    - 多个版本
- Demo: [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
    - 暴力解法：`O(n**3)`
    - 优化：`O(n**2)`
    - 滑动窗口：[leetcode-0003.py](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/src/leetcode/leetcode-0003.py)，`O(n)`
- 二叉查找树
- 平衡查找树

## lab-04 图

- 无向图
- 有向图
- 最小生成树
- 最短路径

## lab-05 字符串

- 字符串排序
- 单词查找树
- 子字符串查找
- 正则表达式
- 数据压缩

## lab-06 递归

- 分而治之：基线条件和归纳法

### lab-06-02 加法问题

```python
from functools import reduce


def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x - 1)


def fact2(x):
    if x <= 1:
        return 1
    ret = 1
    for i in range(1, x + 1):
        ret *= i
    return ret


if __name__ == '__main__':
    factNum = 5
    print(reduce(lambda x, y: x * y, range(1, factNum + 1), 1))
    print(fact(factNum))
    print(fact2(factNum))
```

- 斐波那契数列
- 分地问题（最小公约数问题）

## lab-07 回溯

- 深度优先算法

## lab-08 动态规划

- 背包问题
- 最长公共子串

## lab-09 贪心算法

- 局部优先

## lab-10 广度优先

- 广度优先搜索
- 迪克斯特拉算法

## lab-11 流量与切割

- 最大流
- 最小割

## lab-12 NP困难

- 旅行商问题
- 遗传算法
- K临近算法（KNN）