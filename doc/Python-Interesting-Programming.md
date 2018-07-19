## 彩票中奖率问题：11选5
- 题目：彩票里面有个玩法叫11选5
	- 1~11共11个数字，开奖号码为5个数字（不分前后顺序，不可复选）
	- 你可以选8个数字，如果包含开奖号码则中奖，一注2元变9元，否则不中奖。
	- 请问中奖概率为多少，盈利率为多少？
- 排列组合解法：
	- 首先，11选8的排列组合是C(11,8)，等于C(11,3)，数学表示是：`C3/11`
	- 其次，其中中奖的排列组合是C(6,3)（5个中奖的，所以剩下来是6选3）
	- 所以，中奖率是C(6,3)除以C(11,3)，也就是`(6*5*4)/(11*10*9)`，等于`12.12%`
	
			>>> (6*5*4)/(11*10*9)
			0.12121212121212122
	- 盈利率是`12.12% * (9/2)`，等于`54.55%`
			
			>>> ((6*5*4)/(11*10*9))*(9/2)
			0.5454545454545454
	- 在交互环境里，我们可以很方便地把Python当计算器用，你可以算算等额本息划算还算等额本金划算。
- 我们如果抛开中国人的数学天赋，来看一些正经公式和代码：
	- `C(x,y) = P(x,y) / P(y,y)`
	- `P(x,y) = F(x) / F(x-y)`
	- 代码实现：
	
			def factorial(n):
			    result = 1
			    factor = 2
			    while factor <= n:
			        result *= factor
			        factor += 1
			    return result
			
			
			def permutation(x, y):
			    return factorial(x) / factorial(x - y)
			
			
			def combination(x, y):
			    return permutation(x, y) / permutation(y, y)
			
			
			if __name__ == '__main__':
			    winningRate = combination(6, 3) / combination(11, 8) * 100
			    print('The winning rate = %.2f%%' % winningRate)
- 让代码再正经一点：
	- 参考Python官网的[示例](https://docs.python.org/3/library/doctest.html)
	- 我们来借鉴一下`factorial`方法的“**标准**”写法

			def factorial(n):
			    """Return the factorial of n, an exact integer >= 0.
			
			    >>> [factorial(n) for n in range(6)]
			    [1, 1, 2, 6, 24, 120]
			    >>> factorial(30)
			    265252859812191058636308480000000
			    >>> factorial(-1)
			    Traceback (most recent call last):
			        ...
			    ValueError: n must be >= 0
			
			    Factorials of floats are OK, but the float must be an exact integer:
			    >>> factorial(30.1)
			    Traceback (most recent call last):
			        ...
			    ValueError: n must be exact integer
			    >>> factorial(30.0)
			    265252859812191058636308480000000
			
			    It must also not be ridiculously large:
			    >>> factorial(1e100)
			    Traceback (most recent call last):
			        ...
			    OverflowError: n too large
			    """
			
			    import math
			    if not n >= 0:
			        raise ValueError("n must be >= 0")
			    if math.floor(n) != n:
			        raise ValueError("n must be exact integer")
			    if n+1 == n:  # catch a value like 1e300
			        raise OverflowError("n too large")
			    result = 1
			    factor = 2
			    while factor <= n:
			        result *= factor
			        factor += 1
			    return result
			
			
			if __name__ == "__main__":
			    import doctest
			    doctest.testmod()
			    # doctest.testmod(verbose=True)
	- doctest是一种简单的单元测试，主要用于文档测试（保证交付正确的文档），更常见的单元测试是：[unittest](http://blog.wuwenxiang.net/Python-Unittest)。有了单元测试，我们可以来改进一下`factorial`方法，试试**函数式编程**的威力。
			
			from functools import reduce
			result = reduce(lambda x,y:x*y, range(int(n), 0, -1), 1)
	- 喜欢reduce么？map/filter/sorted了解一下？
- 来看看通过随机数模拟仿真的解法：
	- 代码

			import copy
			import random
			from functools import reduce
			
			
			def choiceN(n, seq):
			    while True:
			        aList = copy.copy(seq)
			        bList = []
			        for _i in range(n):
			            tmp = random.choice(aList)
			            bList.append(tmp)
			            aList.remove(tmp)
			        yield bList
			
			
			if __name__ == '__main__':
			    SAMPLE = 1000000
			    NUM_ALL = 11
			    NUM_CHOICE = 8
			    NUM_WIN = 5
			
			    seq = list(range(NUM_ALL))
			    gChoiceN = choiceN(NUM_CHOICE, seq)
			    setWin = set(range(NUM_WIN))
			    count = reduce(
			        lambda x,y: x+1 if setWin < set(gChoiceN.__next__()) else x,
			        range(SAMPLE), 0)
			
			    print("Percent %.2f%%" % (100.0*count/SAMPLE))
	- 运行结果
		
			Percent 12.13%
	- 随机选取函数看懂了么？二进制了解一下？有更好的写法了么？
	- 集合运算好玩么？再试试并集/交集/差集/外集？
	- 生成器好玩么？
- 速度有点慢？并行处理了解一下 :-)