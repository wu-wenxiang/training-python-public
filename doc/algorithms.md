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

    - Demo: leetcode 235. 二叉搜索树的最近公共祖先
        - 如果我们给的p,q节点都小于node节点，那么他们最近的公共祖先一定在node左边。
        - 如果我们给的p,q节点都大于node节点，那么他们最近的公共祖先一定在ndoe右边。
        - 如果一小一大，那么node一定是最近的公众祖先。
    - Demo: [1038. 从二叉搜索树到更大和树](https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/submissions/)

        ```python
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None

        class Solution:
            def bstToGst(self, root: TreeNode) -> TreeNode:
                tmp = None

                if root is None: return []
                result, stack = [], []

                p_node = root # 当前访问节点指针
                while p_node or stack:

                    while p_node: # 把所有当前访问节点的左孩子都入栈
                        stack.append(p_node)
                        p_node = p_node.right

                    cur_node = stack.pop() # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
                    if tmp != None:
                        cur_node.val += tmp
                    tmp = cur_node.val
                    result.append(cur_node.val) # 因为已经保证没有左节点，可以访问根节点
                    if cur_node.left:
                        p_node = cur_node.left # 将指针指向当前节点的右节点

                return root
        ```

### lab-03-05 [二叉查找树](https://baike.baidu.com/item/二叉排序树)

- [平衡二叉查找树 AVL](https://zhuanlan.zhihu.com/p/56066942)
- [红黑树](https://zhuanlan.zhihu.com/p/31805309)：红黑树并不追求完全平衡，它只要求部分地达到平衡要求，降低了对旋转的要求，从而提高了性能。
- Demo：[bintrees](https://pypi.org/project/bintrees/)

    ```python
    import bintrees

    fruitDict = {'apple': 15, 'pear': 8, 'banana': 14, 'orange': 13}

    avl = bintrees.AVLTree(fruitDict)
    print(len(avl))
    print(avl)

    avl.insert('key1', 10)
    print(len(avl))
    print(avl)
    avl.insert('jake', 11)
    print(len(avl))
    print(avl)

    for i in avl:
        print(i)

    print('jake' in avl)
    avl.remove('jake')
    print('jake' in avl)
    ```

## lab-04 图

### lab-04-01 图的定义和概念
- [无向图定义](https://baike.baidu.com/item/%E6%97%A0%E5%90%91%E5%9B%BE)
- 邻接

    如果两个顶点被同一条边连接，就称这两个顶点是邻接的，如上图 I 和 G 就是邻接的，而 I 和 F 就不是。有时候也将和某个指定顶点邻接的顶点叫做它的邻居，比如顶点 G 的邻居是 I、H、F。

- 路径：

    路径是边的序列，比如从顶点B到顶点J的路径为 BAEJ，当然还有别的路径 BCDJ，BACDJ等等。

- 连通图和非连通图：

    如果至少有一条路径可以连接起所有的顶点，那么这个图称作连通的；如果假如存在从某个顶点不能到达另外一个顶点，则称为非联通的。

- 有向图和无向图：

    如果图中的边没有方向，可以从任意一边到达另一边，则称为无向图；比如双向高速公路，A城市到B城市可以开车从A驶向B，也可以开车从B城市驶向A城市。但是如果只能从A城市驶向B城市的图，那么则称为有向图。

- 有权图和无权图：

    图中的边被赋予一个权值，权值是一个数字，它能代表两个顶点间的物理距离，或者从一个顶点到另一个顶点的时间，这种图被称为有权图；反之边没有赋值的则称为无权图。

### lab-04-02 无向图的程序实现

- 顶点：

    在大多数情况下，顶点表示某个真实世界的对象，这个对象必须用数据项来描述。比如在一个飞机航线模拟程序中，顶点表示城市，那么它需要存储城市的名字、海拔高度、地理位置和其它相关信息，因此通常用一个顶点类的对象来表示一个顶点，这里我们仅仅在顶点中存储了一个字母来标识顶点，同时还有一个标志位，用来判断该顶点有没有被访问过（用于后面的搜索）。

    ```c++
    /**
     * 顶点类
     * @author vae
     */
    public class Vertex {
     public char label;
     public boolean wasVisited;

     public Vertex(char label){
     this.label = label;
     wasVisited = false;
     }
    }
    ```

    顶点对象能放在数组中，然后用下标指示，也可以放在链表或其它数据结构中，不论使用什么结构，存储只是为了使用方便，这与边如何连接点是没有关系的。

- 边

    在前面讲解各种树的数据结构时，大多数树都是每个节点包含它的子节点的引用，比如红黑树、二叉树。也有用数组表示树，树组中节点的位置决定了它和其它节点的关系，比如堆就是用数组表示。

    图并不像树，图没有固定的结构，图的每个顶点可以与任意多个顶点相连，为了模拟这种自由形式的组织结构，用如下两种方式表示图：邻接矩阵和邻接表（如果一条边连接两个顶点，那么这两个顶点就是邻接的）

    - 邻接矩阵：

        邻接矩阵是一个二维数组，数据项表示两点间是否存在边，如果图中有 N 个顶点，邻接矩阵就是 N*N 的数组。上图用邻接矩阵表示如下：

        ![](https://pic2.zhimg.com/80/v2-4d4f9658225599c9c4463d221155861d_hd.jpg)

        1表示有边，0表示没有边，也可以用布尔变量true和false来表示。顶点与自身相连用 0 表示，所以这个矩阵从左上角到右上角的对角线全是 0 。

        注意：这个矩阵的上三角是下三角的镜像，两个三角包含了相同的信息，这个冗余信息看似低效，但是在大多数计算机中，创造一个三角形数组比较困难，所以只好接受这个冗余，这也要求在程序处理中，当我们增加一条边时，比如更新邻接矩阵的两部分，而不是一部分。

    - 邻接表：

        ![](https://pic3.zhimg.com/80/v2-538fc2288d17c1615f63235f8d3597ae_hd.jpg)

        邻接表是一个链表数组（或者是链表的链表），每个单独的链表表示了有哪些顶点与当前顶点邻接。

### lab-04-03 搜索

在图中实现最基本的操作之一就是搜索从一个指定顶点可以到达哪些顶点，比如从武汉出发的高铁可以到达哪些城市，一些城市可以直达，一些城市不能直达。现在有一份全国高铁模拟图，要从某个城市（顶点）开始，沿着铁轨（边）移动到其他城市（顶点），有两种方法可以用来搜索图：深度优先搜索（DFS）和广度优先搜索（BFS）。它们最终都会到达所有连通的顶点，深度优先搜索通过栈来实现，而广度优先搜索通过队列来实现，不同的实现机制导致不同的搜索方式。

- 深度优先搜索（DFS）规则：
    1. 如果可能，访问一个邻接的未访问顶点，标记它，并将它放入栈中。
    1. 当不能执行规则 1 时，如果栈不为空，就从栈中弹出一个顶点。
    1. 如果不能执行规则 1 和规则 2 时，就完成了整个搜索过程。

    ![](https://pic2.zhimg.com/80/v2-93401ce4df91912b1319113312244719_hd.jpg)

    对于上图，应用深度优先搜索如下：

    1. 假设选取 A 顶点为起始点，并且按照字母优先顺序进行访问，那么应用规则1 ，接下来访问顶点 B，然后标记它，并将它放入栈中
    2. 再次应用规则 1，接下来访问顶点 F
    3. 再次应用规则 1，访问顶点 H
    4. 我们这时候发现，没有 H 顶点的邻接点了，这时候应用规则 2，从栈中弹出 H
    5. 这时候回到了顶点 F，但是我们发现 F 也除了 H 也没有与之邻接且未访问的顶点了，那么再弹出 F
    6. 这时候回到顶点 B，同理规则 1 应用不了，应用规则 2，弹出 B
    7. 这时候栈中只有顶点 A了，然后 A 还有未访问的邻接点，所有接下来访问顶点 C
    8. 但是 C又是这条线的终点，所以从栈中弹出它
    9. 再次回到 A，接着访问 D,G,I
    10. 最后也回到了 A，然后访问 E，但是最后又回到了顶点 A
    11. 这时候我们发现 A没有未访问的邻接点了，所以也把它弹出栈
    12. 现在栈中已无顶点，于是应用规则 3，完成了整个搜索过程

    深度优先搜索在于能够找到与某一顶点邻接且没有访问过的顶点。这里以邻接矩阵为例，找到顶点所在的行，从第一列开始向后寻找值为1的列；列号是邻接顶点的号码，检查这个顶点是否未访问过，如果是这样，那么这就是要访问的下一个顶点，如果该行没有顶点既等于1（邻接）且又是未访问的，那么与指定点相邻接的顶点就全部访问过了（后面会用算法实现）。

- 广度优先搜索（BFS）

    深度优先搜索要尽可能的远离起始点，而广度优先搜索则要尽可能的靠近起始点，它首先访问起始顶点的所有邻接点，然后再访问较远的区域，这种搜索不能用栈实现，而是用队列实现。

    1. 访问下一个未访问的邻接点（如果存在），这个顶点必须是当前顶点的邻接点，标记它，并把它插入到队列中。
    1. 如果已经没有未访问的邻接点而不能执行规则 1 时，那么从队列列头取出一个顶点（如果存在），并使其成为当前顶点。
    1. 如果因为队列为空而不能执行规则 2，则搜索结束。

    对于上面的图，应用广度优先搜索：

    1. 以A为起始点，首先访问所有与 A 相邻的顶点，并在访问的同时将其插入队列中，现在已经访问了 A,B,C,D和E
    1. 这时队列（从头到尾）包含 BCDE，已经没有未访问的且与顶点 A 邻接的顶点了，所以从队列中取出B，寻找与B邻接的顶点，这时找到F，所以把F插入到队列中
    1. 已经没有未访问且与B邻接的顶点了，所以从队列列头取出C，它没有未访问的邻接点
    1. 因此取出 D 并访问 G，D也没有未访问的邻接点了，所以取出E，现在队列中有 FG
    1. 再取出 F，访问 H，然后取出 G，访问 I
    1. 现在队列中有 HI，当取出他们时，发现没有其它为访问的顶点了，这时队列为空，搜索结束。

### lab-04-04 最小生成树

对于图的操作，还有一个最常用的就是找到最小生成树，最小生成树就是用最少的边连接所有顶点。对于给定的一组顶点，可能有很多种最小生成树，但是最小生成树的边的数量 E 总是比顶点 V 的数量小1，即：`V = E + 1`

这里不用关心边的长度，不是找最短的路径（会在带权图中讲解），而是找最少数量的边，可以基于深度优先搜索和广度优先搜索来实现。

比如基于深度优先搜索，我们记录走过的边，就可以创建一个最小生成树。因为DFS 访问所有顶点，但只访问一次，它绝对不会两次访问同一个顶点，但她看到某条边将到达一个已访问的顶点，它就不会走这条边，它从来不遍历那些不可能的边，因此，DFS 算法走过整个图的路径必定是最小生成树。

### lab-04-05 最短路径

- 无权图中的最短路径算法的就是广度优先遍历
- 有权无向图的最短路径算法是迪克斯特拉算法

### lab-04-06 类库：networkx

[networkx](https://networkx.github.io/documentation/stable/tutorial.html)

```python
import networkx as nx
import matplotlib.pyplot as plt


# 1.创建一个图
g = nx.Graph()
g.clear     # 将图上元素清空


# 2.节点
g.add_node(1)           # 添加一个节点
g.add_node("a")
g.add_node("spam")
# g.add_nodes_from([2, 3])
nodes_list = [2, 3]     # 添加一组节点
g.add_nodes_from(nodes_list)

g.add_node("spam")          # 添加了一个名为spam的节点
g.add_nodes_from("spam")    # 添加了4个节点，名为s,p,a,m
H = nx.path_graph(10)
g.add_nodes_from(H)         # 将0~9加入了节点, 请勿使用g.add_node(H)

node_name = "spam"
g.remove_node(node_name)        # 删除节点
g.remove_nodes_from("spam")
print('g.nodes:', g.node())     # 0-9共10个节点打印出来


# 3.边
g.add_edge(1, 2)        # 添加一条边
e = (2, 3)
g.add_edge(*e)          # 直接g.add_edge(e)数据类型不对，*是将元组中的元素取出
g.add_edges_from([(0, 9), (1, 3), (1, 4)])  # 添加一组边

n = 10
H = nx.path_graph(n)
g.add_edges_from(H.edges())     # 添加了0~1,1~2 ... n-2~n-1这样的n-1条连续的边

edge_name = (0, 9)
edges_list = [(1, 3), (1, 4)]
g.remove_edge(*edge_name)       # 删除边
g.remove_edges_from(edges_list)
print('g.edges:', g.edges())


# 4.查看信息
g.number_of_nodes()     # 查看点的数量
g.number_of_edges()     # 查看边的数量
g.nodes()               # 返回所有点的信息(list)
g.edges()               # 返回所有边的信息(list中每个元素是一个tuple)
print([i for i in g.neighbors(1)])  # 所有与1这个点相连的点的信息以列表的形式返回
print(g[1])             # 查看所有与1相连的边的属性，格式输出：{0: {}, 2: {}} 表示1和0相连的边没有设置任何属性（也就是{}没有信息），同理1和2相连的边也没有任何属性


# 5.图的属性设置
g = nx.Graph(day="Monday")
g.graph                     # {'day': 'Monday'}

g.graph['day'] = 'Tuesday'  # 修改属性
g.graph                     # {'day': 'Tuesday'}


# 6.点的属性设置
g.add_node('benz', money=10000, fuel="1.5L")
print(g.node['benz'])           # {'fuel': '1.5L', 'money': 10000}
print(g.node['benz']['money'])  # 10000
print(g.nodes(data=True))       # data默认false就是不输出属性信息，修改为true，会将节点名字和属性信息一起输出


# 7.边的属性设置
g.clear()
n = 10
H = nx.path_graph(n)
g.add_nodes_from(H)
g.add_edges_from(H.edges())
g[1][2]['color'] = 'blue'

g.add_edge(1, 2, weight=4.7)
g.add_edges_from([(3, 4), (4, 5)], color='red')
g.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
g[1][2]['weight'] = 4.7


# 8.不同类型的图（有向图Directed graphs , 重边图 Multigraphs）
# Directed graphs
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75), (1, 4, 0.3)])    # 添加带权值的边
print(DG.out_degree(1))                     # 打印结果：2 表示：找到1的出度
print(DG.out_degree(1, weight='weight'))    # 打印结果：0.8 表示：从1出去的边的权值和，这里权值是以weight属性值作为标准，如果你有一个money属性，那么也可以修改为weight='money'，那么结果就是对money求和了
print(list(DG.successors(1)))               # [2,4] 表示1的后继节点有2和4
print(list(DG.predecessors(1)))             # [3] 表示只有一个节点3有指向1的连边

# Multigraphs
MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, .5), (1, 2, .75), (2, 3, .5)])
print(MG.degree(weight='weight'))   # {1: 1.25, 2: 1.75, 3: 0.5}
GG = nx.Graph()
for n, nbrs in MG.adjacency():
    for nbr, edict in nbrs.items():
        minvalue = min([d['weight'] for d in edict.values()])
        GG.add_edge(n, nbr, weight=minvalue)
print(GG.degree(weight='weight'))     # [(1, 0.5), (2, 1.0), (3, 0.5)]
print(nx.shortest_path(GG, 1, 3))     # [1, 2, 3]


# 9.图的遍历
g = nx.Graph()
g.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in g.adjacency():       # n表示每一个起始点，nbrs是一个字典，字典中的每一个元素包含了这个起始点连接的点和这两个点连边对应的属性
    print(n, nbrs)
    for nbr, eattr in nbrs.items():
        # nbr表示跟n连接的点，eattr表示这两个点连边的属性集合，这里只设置了weight，如果你还设置了color，那么就可以通过eattr['color']访问到对应的color元素
        data = eattr['weight']
        if data < 0.5:
            print('(%d, %d, %.3f)' % (n, nbr, data))


# 10.图生成和图上的一些操作
# subgraph(G, nbunch)      - induce subgraph of G on nodes in nbunch
# union(G1,G2)             - graph union
# disjoint_union(G1,G2)    - graph union assuming all nodes are different
# cartesian_product(G1,G2) - return Cartesian product graph
# compose(G1,G2)           - combine graphs identifying nodes common to both
# complement(G)            - graph complement
# create_empty_copy(G)     - return an empty copy of the same graph class
# convert_to_undirected(G) - return an undirected representation of G
# convert_to_directed(G)   - return a directed representation of G


# 11.图上分析
g = nx.Graph()
g.add_edges_from([(1, 2), (1, 3)])
g.add_node("spam")
print(list(nx.connected_components(g)))   # [[1, 2, 3], ['spam']] 表示返回g上的不同连通块
print(sorted(dict(nx.degree(g)).items(), reverse=True, key=lambda x: x[1]))  # [(1, 2), (2, 1), (3, 1), ('spam', 0)]

G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.6), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)
# 'a'可到达节点的list
print(list(nx.dfs_postorder_nodes(G, 'a')))
print(list(nx.dfs_preorder_nodes(G, 'a')))
# 获取两点间的简单路径
print(list(nx.all_simple_paths(G, 'a', 'd')))
print(list(nx.all_simple_paths(G, 'a', 'd', cutoff=2)))     # cutoff为截断常数
# 最短路径
print(nx.shortest_path(G))
print(nx.shortest_path(G, 'a', 'd'))
print(nx.has_path(G, 'a', 'd'))
# dijkstra 最短路径
print(nx.dijkstra_path(G, 'a', 'd'))
print(nx.dijkstra_path_length(G, 'a', 'd'))


# 12.图的绘制
pos = nx.spring_layout(G)
fig = plt.figure(figsize=(13, 8))
fig1 = fig.add_subplot(221)
nx.draw(G, with_labels=True, font_weight='bold', width=2)

fig2 = fig.add_subplot(222)
e = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
nx.draw_networkx_labels(G, pos, edges_label=e)
nx.draw_networkx(G, pos, with_labels=True, font_weight='bold', width=2, edge_cmap=plt.cm.Reds)
plt.axis('on')

fig3 = fig.add_subplot(223)
nx.draw_circular(DG, with_labels=True, font_weight='bold', width=2)

fig4 = fig.add_subplot(224)
nx.draw_random(DG, with_labels=True, font_weight='bold', width=2)
plt.show()
```

[画图的示例](https://zhuanlan.zhihu.com/p/36700425)

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