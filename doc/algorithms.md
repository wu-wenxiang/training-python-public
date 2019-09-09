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

- 生成测试随机序列

    ```python
    import random

    loopN = 1000000
    aList = [random.randint(1, loopN) for i in range(loopN)]
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

- Demo：对一个列表进行模拟排序（不实际排序，而是返回排序后的原始索引值）

    ```python
    >>> aList = [1, 3, 4, 2, 5, 2]
    >>> aDict = {i:j for i,j in enumerate(aList)}
    >>> print(sorted(aDict, key=lambda x: aDict[x]))
    [0, 3, 5, 1, 2, 4]
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

### lab-02-05 排序算法案例

- Demo：[56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/submissions/)

    ```python
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        aList = sorted(intervals)
        bList = []
        for i in aList:
            if bList and bList[-1][1] >= i[0]:
                bList[-1][1] = max(i[1], bList[-1][1])
            else:
                bList.append(i)
        return bList
    ```

- Demo: 测试排序算法速度

### lab-02-06 堆排序

- 定义

    **Heaps are binary trees for which every parent node has a value less than or equal to any of its children.** This implementation uses arrays for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all k, counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that its smallest element is always the root, heap[0].

    | | 入队 | 出队 |
    | :-- | :-- | :-- |
    | 普通数组	| O(1) | O(n) |
    | 顺序数组 | O(n) | O(1) |
    | 堆 | O(lgn) | O(lgn) |

- [heapq — Heap queue algorithm](https://docs.python.org/3.7/library/heapq.html)

    ```python
    >>> def heapsort(iterable):
    ...     h = []
    ...     for value in iterable:
    ...         heappush(h, value)
    ...     return [heappop(h) for i in range(len(h))]
    ...
    >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    ```python
    >>> h = []
    >>> heappush(h, (5, 'write code'))
    >>> heappush(h, (7, 'release product'))
    >>> heappush(h, (1, 'write spec'))
    >>> heappush(h, (3, 'create tests'))
    >>> heappop(h)
    (1, 'write spec')
    ```

    ```
                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30
    ```

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

### lab-03-04 二叉树

- [满二叉树](https://baike.baidu.com/item/满二叉树)
- [完全二叉树](https://baike.baidu.com/item/完全二叉树)
- Demo：[treelib](https://treelib.readthedocs.io/en/latest/)
- 二叉树的遍历

    ![](http://songwenjie.vip/blog/180426/jlIAfhlcL3.png?imageslim)

    ```python
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    ```

    - 前序遍历：中、左、右：[Leetcode 44. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

        ```python
        def preorderTraversal1(self, root):
            result = []
            self.helper(root, result)
            return result

        def helper(self, root, result):
            if root:
                result.append(root.val)
                self.helper(root.left, result)
                self.helper(root.right, result)
        ```

        ```python
        class Solution:
            def preorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []
                return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        ```

        ```python
        class Solution:
            def preorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if not root: return []

                result, stack = [], [root]

                while stack:
                    cur_node = stack.pop() # 访问根节点，直接进行操作(输出到数组)
                    result.append(cur_node.val)
                    if cur_node.right: # 先入栈右节点
                        stack.append(cur_node.right)
                    if cur_node.left: # 后入栈左节点，这样下一轮循环先访问左节点，维护了访问顺序
                        stack.append(cur_node.left)

                return result
        ```

    - 中序遍历：左、中、右，适用排序，[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

        ```python
        class Solution:
            def inorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []
                return [] if root is None else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        ```

        ```python
        class Solution:
            def inorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []
                result, stack = [], []

                p_node = root # 当前访问节点指针
                while p_node or stack:

                    while p_node: # 把所有当前访问节点的左孩子都入栈
                        stack.append(p_node)
                        p_node = p_node.left

                    cur_node = stack.pop() # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
                    result.append(cur_node.val) # 因为已经保证没有左节点，可以访问根节点
                    if cur_node.right:
                        p_node = cur_node.right # 将指针指向当前节点的右节点

                return result
        ```

    - 后序遍历：左、右、中，适用删除节点，判断相同子树。[145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

        ```python
        class Solution:
            def postorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []
                return [] if root is None else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        ```

        ```python
        class Solution:
            def postorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []

                result, stack = [], [(root, False)]

                while stack:
                    cur_node, visited = stack.pop()
                    if visited: # 只有访问状态为True的节点才能被操作
                        result.append(cur_node.val)
                    else:
                        stack.append((cur_node, True))
                        if cur_node.right:
                            stack.append((cur_node.right, False))
                        if cur_node.left:
                            stack.append((cur_node.left, False))

                return result
        ```

        ```python
        class Solution:
            def preorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
                if root is None: return []
                
                result, stack = [], [root]

                while stack:
                    cur_node = stack.pop()
                    result.append(cur_node.val)
                    if cur_node.left: # 修改顺序
                        stack.append(cur_node.left)
                    if cur_node.right: # 修改顺序
                        stack.append(cur_node.right)

                return result[::-1] # 反序操作
        ```

    - 层级遍历：广度优先，[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)，[107. Binary Tree Level Order Traversal 2](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

        ```python
        from collections import deque

        class Solution:
            def levelOrder(self, root):
                """
                :type root: TreeNode
                :rtype: List[List[int]]
                """
                if root is None: return []
                result, queue = [], deque([root])
                
                while queue:
                    level_len = len(queue) # 记录现在队列中的节点数量
                    level_nodes = [] # 每层输出
                    while level_len > 0: # 具体出队入队操作，保证本层所有节点的子节点都入队
                        cur_node = queue.popleft()
                        level_nodes.append(cur_node.val)
                        if cur_node.left:
                            queue.append(cur_node.left)
                        if cur_node.right:
                            queue.append(cur_node.right)
                        level_len -= 1
                    result.append(level_nodes)
                
                return result
        ```

    - Demo：[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree)，Brew

        ```python
        class Solution:
            def invertTree(self, root):
                """
                :type root: TreeNode
                :rtype: TreeNode
                """
                if root is None: return []
                # 在本节点的操作，左右孩子互换
                root.left, root.right = root.right, root.left
                # 已经搞定的左右孩子，使用递归的思路写出函数表达式
                self.invertTree(root.right) # 下面两句的顺序并不重要
                self.invertTree(root.left)
                return root
        ```

        ```python
        class Solution:
            def invertTree(self, root):
                """
                :type root: TreeNode
                :rtype: TreeNode
                """
                if root is None: return []
                stack = [root]

                while stack:
                    cur_node = stack.pop()
                    # 对当前节点进行操作
                    cur_node.left, cur_node.right = cur_node.right, cur_node.left
                    # 进行入栈操作，保证访问到每一个节点
                    if cur_node.left: stack.append(cur_node.left)
                    if cur_node.right: stack.append(cur_node.right)

                return root
        ```

    - Demo: leetcode 104. 二叉树的最大深度，类似111

        ```c++
        class Solution {
            public:
                //求节点root的深度
                int maxDepth(TreeNode* root) {
                    //终止条件
                    if(root == NULL){ 
                        return 0;
                    }
                    
                    return 1 + max(maxDepth(root -> left), maxDepth(root -> right));
                    
                }
            };
        ```

- [二叉查找树](https://baike.baidu.com/item/二叉排序树)
- [平衡二叉查找树 AVL](https://zhuanlan.zhihu.com/p/56066942)
- [红黑树](https://zhuanlan.zhihu.com/p/31805309)：红黑树并不追求完全平衡，它只要求部分地达到平衡要求，降低了对旋转的要求，从而提高了性能。
- Demo：[bintrees](https://pypi.org/project/bintrees/)

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