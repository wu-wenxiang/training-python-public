# Python Training in 2 Days

## Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 课前准备 | N/A | [lab-00 Python Environment](#lab-00-python-environment) | [Python Installation](#python-installation) |
| | | | [IDE Configuration](#ide-configuration) |
| 第 1 天 | 上午 | [lab-01 Python Basic](#lab-01-python-basic) | [Quick Start](#quick-start) |
| | | | [Data Structure](#data-structure) |
| | | | [Functions](#functions) |
| | | [lab-02 Common Usage Modules](#lab-02-common-usage-modules) | [OS/SYS](#ossys) |
| | 下午 | | [I/O](#io) |
| | | [lab-03 Object Oriented](#lab-03-object-oriented) | [Class & Instance](#class--instance) |
| | | | [Operator Overloading](#operator-overloading) |
| | | | [Inheritance & Composition](#inheritance--composition) |
| 第 2 天 | 上午 | [lab-04 Scientific Computation Modules](#lab-04-scientific-computation-modules) | [Numpy & Pandas](#numpy--pandas) |
| | | | [Scipy & SkLearn](#scipy--sklearn) |
| | | | [Matplotlib](#matplotlib) |
| | | [lab-05 Pythonic Code Style](#lab-05-pythonic-code-style) | [Functional Programming](#functional-programming) |
| | | | [Iterator & Generator](#iterator--generator) |
| | | | [PEP8](#pep8) |
| | 下午 | [lab-06 Other Categories](#lab-06-other-categories) | [Parallel Process](#parallel-process) |
| | | | [Debug](#debug) |
| | | | [Decorator](#decorator) |
| | | | [Memory Management](#memory-management) |
| | | | [Time & Space Complexity](#time--space-complexity) |
| | | [lab-07 RobotFrameWork](#lab-07-robotframework) | [Quick Start](#quick-start) |
| | | | [Demo](#demo) |

    import re
    reCmp=re.compile('^\s*#+\s+(.+)$')
    aList = [reCmp.search(i).groups()[0].strip() for i in aStr.split('\n') if reCmp.search(i)]
    bList = [(i, '-'.join(i.split()).lower().replace('&','').replace('/','')) for i in aList]
    template = '| | | | [%s](%s) |'
    print('\n'.join(template % i for i in bList))

## lab-00 Python Environment

### Python Installation
- **推荐**：[单独安装 Python](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Python.md)，3.7 版本
- 其它选项：
    - [Anacoda（ 包含Python ）](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Anaconda.md)，3.7 版本

### IDE Configuration
- **推荐**：[Eclipse+Pydev](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Eclipse-Pydev.md)
- 其它选项：
    - [VS Code](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-VSCode.md)
    - [PyCharm](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-PyCharm.md)

## lab-01 Python Basic

### Quick Start

1. [开始] **Python在编程语言世界中的处于什么样的位置？**[TIOBE](https://tiobe.com/tiobe-index/)
1. [开始] **Python有什么样的特质和设计哲学？**简单优于繁复，明确优于晦涩，解决一个问题只用一种方法。
1. [开始] **作为一个初入门者，我们应该怎样学习编程？**[如何成为一名黑客-Eric-S-Raymond](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/%E5%A6%82%E4%BD%95%E6%88%90%E4%B8%BA%E4%B8%80%E5%90%8D%E9%BB%91%E5%AE%A2-Eric-S-Raymond.pdf)
1. [开始] **应该选择Python2还是Python3开始学习，以及进行开发？**[参考](https://wiki.python.org/moin/Python2orPython3)，用Python3
1. [开始] **有哪些优秀的Python学习资源可以参考？** [Python学习手册5th](https://book.douban.com/subject/30364619/)，[Python3标准库](https://book.douban.com/subject/30346181/)
1. [环境] **如何查阅Python帮助文档？** pydoc, help, chm
1. [环境] **Python代码中如何包含中文？**源文件存成utf-8，文件头：`# -*- coding: utf-8 -*`

### Data Structure

1. [数字] **如何实现取整运算？截余取整、四舍五入、向上取整、向下取整。**
1. [数字] **整数的除法运算和整除运算是如何实现的？**怎么写兼容代码？
1. [数字] **Python如何处理进制转换（整数与字符串的互相转换）？**0b/0/0x，bin/ocx/hex，%o/%x
1. [数字] **应如何判断两个浮点数是否相等？**原理
1. [数字] **浮点数精度控制(`round`)和精度显示(`%.2f`)应用场景？如何编码？**
1. [数字] **如何产生随机数？`random/randint/choice`**
1. [数字] **如何理解Python中变量和对象的存储模型？id**
1. [数字] 如何理解Python语言的三个定语：动态语言，动态类型语言，强类型语言？
1. [字符] 如何编码单行、多行和分行输入的字符串？
1. [字符] 我们应该用单引号还是双引号？
1. [字符] **什么是原始字符串？**
1. [字符] **如何处理Unicode字符串和编解码问题？**`'我们'.encode('utf-8').decode('utf-8')``
1. [字符] **如何实现字符串的乘法和加法？**
1. [字符] **如何操作字符串切片？负index、左开右闭、None、负步长**
1. [字符] **如何实现子字符串的替换、查找？**
1. [字符] **如何实现字符串的切割和粘合？**
1. [字符] **如何移除字符串两端的空白？**
1. [字符] **如何格式化字符串？`%`，`format`**
1. [字符] **什么是反射和自省机制？`__dict__`, `dir`**
1. [序列] **元组/列表对象在PVM中的存储模型是怎样的？**
1. [序列] 基于元组的赋值语法有哪些常见的应用场景？
1. [序列] **序列的通用运算？`in`, `for`, `+/*`, 切片, `len/min/max/sorted`**
1. [序列] **如何理解列表对象的可变性与元组对象的不可变性？**
1. [序列] 生成器对象和列表对象的区别是什么？
1. [序列] **列表对象的常见运算有哪些？元素的添加，访问，排序，反序，移除，修改，遍历**
1. [序列] **什么是列表解析？**
1. [序列] **重映射，浅拷贝，深拷贝的区别是什么？**`[[0]]*5`
1. [散列] 如何利用集合对序列元素去重？
1. [散列] **集合运算有哪些？**
1. [散列] **集合/字典的存储模型是怎样的？**
1. [散列] **字典的常见运算有哪些？元素的添加，访问，移除，修改，遍历，排序，存在判断**
1. [散列] **什么是唱票算法？它适用于什么场合？Counter类能实现什么功能？**
1. [散列] 除了列表解析外，还有什么类似的语法？生成器表达式，集合解析，字典解析

### Functions

1. [函数] **如何定义和调用一个函数？**
1. [函数] 函数对象的存储模型是怎样的？
1. [函数] **什么是LEGB规则？有哪些陷阱？`a += 3`**
1. [函数] **默认参数的陷阱有哪些？`time.time()`, `[]`**
1. [函数] 如何在函数内使用Global变量？
1. [函数] **Python中的实参传递有哪些特殊的语法？**
1. [函数] **Python中的形参传递有哪些特殊的语法？**
1. [函数] 函数传参和Return返回值时实际发生了什么？重映射？浅拷贝？深拷贝？
1. [函数] **Lambda函数的概念和语法如何？**
1. [函数] 如何理解和编写递归函数？优势：语义明确；劣势：性能隐患。斐波那契数列，递归，递推。
1. [函数] **什么是高阶函数？**
1. [函数] 闭包closure是什么？如何用闭包实现加法器？有状态的函数。FP与OOP。
1. [函数] **如何使用高阶函数？Map/Filter/Reduce/Sort/Max/偏函数**，`from functools import reduce`

## lab-02 Common Usage Modules

### OS/SYS

### I/O

## lab-03 Object Oriented

### Class & Instance

1. [对象] **如何定义和实例化一个类？**
1. [对象] **类与实例的存储模型是怎样的？类的属性和实例的属性存在怎样的关系？**
1. [对象] **类中的字段属性为什么不推荐使用可变对象？**
1. [对象] 什么是伪私有属性？
1. [对象] 什么是属性property？
1. [对象] 什么是静态static方法与类class方法？

### Operator Overloading

1. [对象] 什么是钩子方法与运算符重载？
1. [对象] **常见的重载方法有哪些？`__init__`, `__str__`, `__call__`, `__getattr__`, `__len__`**
1. [对象] 如何用类来实现闭包？`__init__`, `__call__`
1. [对象] 如何约束类，使其实例不能随意添加属性？`__slot__`

### Inheritance & Composition

1. [对象] Python的继承是单继承还是多继承？继承的搜索策略是深度优先还是广度优先？
1. [对象] **组合和继承各自有什么优缺点？如何用组合和继承分别实现Name类？**
1. [对象] **Python如何实现一个符合开放封闭原则的简单工厂模式？**
1. [对象] 设计模式的基本原则和六大原则是什么？23种设计模式分为哪3类，每个设计模式用于什么场景？参考：[设计模式摘录](http://blog.wuwenxiang.net/Design-Pattern) 

## lab-04 Scientific Computation Modules

### Numpy & Pandas

### Scipy & SkLearn

### Matplotlib

## lab-05 Pythonic Code Style

### Functional Programming

### Iterator & Generator

### PEP8

## lab-06 Other Categories

### Parallel Process

### Debug

### Decorator

### Memory Management

### Time & Space Complexity

## lab-07 RobotFrameWork

### Quick Start

### Demo