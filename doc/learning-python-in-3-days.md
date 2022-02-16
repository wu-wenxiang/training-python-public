# Python 3 日谈

## 注意 ⚠️

- *斜体表示引用*
- **未经允许，禁止转载**

## 课程目录

| 日程    | 时间 | 课程              | 内容                |
| ------ | ---- | ---------------- | ------------------ |
| 第 1 天 | 上午 | [1. 基础](#1-基础) | [1.1 简介](#11-简介) |
|        |      |                  | [1.2 开发环境搭建](#12-开发环境搭建) |
|        |      |                  | [1.3 变量和对象](#13-变量和对象) |
|        |      |                  | [1.4 基本对象类型](#14-基本对象类型) |
|        | 下午 | [2. 进阶](#2-进阶) | [2.1 函数和高阶函数](#21-函数和高阶函数) |
|        |      |                  | [2.2 类和实例](#22-类和实例) |
|        |      |                  | [2.3 正则表达式](#23-正则表达式) |
|        |      |                  | [2.4 异常处理](#24-异常处理) |
| 第 2 天 | 上午 | [3. 开发](#3-开发相关) | [3.1 版本控制](#31-版本控制) |
|        |     |                   | [3.2 自动化测试](#32-自动化测试) |
|        |     |                   | [3.3 自动化任务](#33-自动化任务) |
|        |     |      | [3.4 开发规范](#34-开发规范) |
|        |     |      | [3.5 模块和发布](#35-模块和打包) |
|        | 下午 | [4. Web](#4-web-开发) | [4.1 MVC 框架](#41-mvc-框架) |
|        |     |                   | [4.2 Restful API](#42-restful-api) |
|        |     |                   | [4.3 服务部署](#43-服务部署) |
| 第 3 天 | 上午 | [5. 算法](#5-算法和设计模式相关) | [5.1 算法复杂度](#51-算法复杂度) |
|        |     |                   | [5.2 算法实践](#52-算法实践) |
|        |     |                   | [5.3 设计模式实践](#53-设计模式实践) |
|        | 下午 | [6. 系统](#6-系统相关) | [6.1 shell 编程](#61-shell-编程) |
|        |     |                   | [6.2 父子进程调用](#62-父子进程调用) |
|        |     |                   | [6.3 文件和目录](#63-文件和目录) |
|        |     |                   | [6.4 并行计算](#64-并行计算) |

## 1. 基础

[返回目录](#课程目录)

### 1.1 简介

[返回目录](#课程目录)

#### 1.1.1 比较流行的程序语言是哪些？

- TIOBE Index：<https://tiobe.com/tiobe-index/>

    *TIOBE 编程社区指数是编程语言流行度的一个指标。该索引每月更新一次。评级基于全球熟练工程师的数量、课程和第三方供应商的数量。Google、Bing、Yahoo!、维基百科、亚马逊、YouTube 和百度等流行搜索引擎用于计算评级。*

    截至 2022 年 1 月，编程语言流行趋势图如下：

    ![](images/tiobe-202201.png)

    *Python 于 2021 年初从 TIOBE 索引的第 3 位开始，将 Java 和 C 抛在后面，成为 TIOBE 索引的第一名。但 Python 的流行并不止于此。目前，它比其他人领先 1% 以上。Java 在 2001 年创下 26.49% 评级的历史记录还很遥远，但 Python 已经成为许多领域事实上的标准编程语言。没有迹象表明 Python 的胜利行军将很快停止。*

    *Python 有没有真正的竞争者？未来可能会竞争的任何新的闪亮语言？如果我们看看过去几年有前途的语言，我们会看到 2021 年的以下变化：Swift 从 #13 到 #10，Go 从 #14 到 #13，Rust 从 #26 到 #26，Julia 从 #23 到#28，Kotlin 从 #40 到 #29，Dart 从 #25 到 #37，TypeScript 从 #42 到 #49。因此，除了 Swift 和 Go 之外，我们预计不会很快有任何新语言进入前 5 名甚至前 3 名。*

- 一种编程语言为什么会流行？
    - 主要原因：**应用广泛（有用）、开发效率高 & 易维护（好用）**
    - 次要原因：性能优异、暂无竞争对手（垄断）

    思考：排名靠前的语言们，它们各自为什么流行？

#### 1.1.2 Python 的起源

- 创始人：[Guido van Rossum](https://baike.baidu.com/item/%E5%90%89%E5%A4%9A%C2%B7%E8%8C%83%E7%BD%97%E8%8B%8F%E5%A7%86/328361)，数学和计算机硕士
- 大龄男青年：1989 年圣诞假期，MAC 笔记本一夜完成
- Python 命名源自 Guido 最英国肥皂剧《Monty Python 马戏团》

#### 1.1.3 什么是 Pythonic 的编程思维？

- **Python 是工程，不是艺术（解决同一个问题用同一种方法）**
    - Python 中的 None 只有一种写法，不能写成 none / null / nul / Null / NONE
    - True/False 也只有一种写法，不能写成 true / TRUE
    - Python 中的分支结构只有 if/else，没有 switch
    - Python 中的 for 循环也只有一种写法 `for i in items: ...`
- **简单优于复杂**
    - Python 只有很少的语法糖，比如装饰器
    - Python 的对象属性设计基本都是可以自圆其说的，包括切片和 range 的开闭区间一致性，装饰器没有黑魔法，for 和 while 中的 else，迭代器的设计，等等。
- **明确优于晦涩**（复杂优于难懂，要始终保持代码的易读性，“让易读的代码进行性能优化”远比“让高效的代码变得易读”要容易）

更具体一点：

- 自顶而下的面向接口的设计
- 恰当地使用数据结构、算法和设计模式
- 代码越少越好（尽量用标准库，代码越少 Bug 越少）
- 尽量减少写复杂的嵌套循环和分支结构，善用解析和高阶函数，把一个复杂的大循环拆成多个简单的小循环

#### 1.1.4 新手应该如何学习编程？

- Eric Raymond 推荐的学习路径：**Python -> Java -> C**，参考：[如何成为一名黑客-Eric-S-Raymond.pdf](如何成为一名黑客-Eric-S-Raymond.pdf)
- 选择基础而全面的入门书
    - 官方网站：<http://www.python.org>
    - [Python 学习手册 5th](https://book.douban.com/subject/30364619/)
    - [Python 3 标准库](https://book.douban.com/subject/30346181/)
- 到开源项目中去读代码、提交代码

    Python 开源项目非常多，其中 [OpenStack](https://opendev.org/openstack) 是集 Python 工程实现之大成的 IaaS 云计算项目，囊括几乎所有 Python 的应用相关技术，包括：

    - 基于 MVC 的 Web 网站（Horizon 用了 Django 框架）
    - 基于 Restful API 的 Web Service（Pecan / Webob / Flask / Paste 等框架）
    - Restful API 客户端框架（SDK）
    - 数据库处理（SqlAlchemy）
    - 对接消息队列
    - 对接（缓存处理）
    - 命令行编程
    - 类库打包和动态加载
    - 配置文件解析
    - 日志处理
    - 容器化封装（Kolla）
    - 自动化部署（Ansible）
    - 认证、鉴权和准入
    - 服务注册和服务发现
    - 对接时序数据库
    - 计量和监控（ceilometer 等）
- 程序语言以外的部分
    - 系统（容器、虚拟化）、存储、网络和知识
    - 算法和数据结构
    - 面向对象和设计模式
    - 软件工程和项目管理

### 1.2 开发环境搭建

[返回目录](#课程目录)

#### 1.2.1 Python 如何安装？

参考：[Python 在 Windows 环境上的安装步骤](Installation-Python.md)

> **练习作业**：安装 python。看到下图表示执行成功
>
>   ![Python-Version.png](images/9da5527f336948b59f2e5f195552cb61-Python-Version.png)
>
> - 图中的 python 版本不一定是 3.6，更高版本亦可
> - 图中的 pip 安装路径也可能不同，不用关注

#### 1.2.2 Python 程序在命令行窗口中如何运行？

- 交互式运行环境：用于 Debug
    - 在命令行中输入 `python`，进入交互环境
    - 交互环境会自动打印出对象的值，比如 `2*3`
    - 退出交互环境：`exit()`，回车
- 运行单行命令：用于和 Shell 命令交互，比如：`python -c "print(3*5)"`
- 运行脚本，比如：`python test.py`

#### 1.2.3 如何用 VSCode 编写和调试 Python 程序？

参考：[用 VSCode 编写和调试 Python 程序](Installation-VSCode.md)

> **练习作业**：在 VSCode 中运行 python 程序。看到下图表示执行成功
>
>    ![](images/vscode-run.png)

#### 1.2.4 Python 体系结构

- Python 虚拟机
    - Python 虚拟机是安装在操作系统上的软件，用来解析和运行符合Python 语法的命令或者脚本
    - 之前安装 python 就是在安装 Python 虚拟机
- Python 语法
    - Python 程序由**模块**组成，模块由**语句**组成，语句由**表达式**组成，表达式建立和处理**对象**
    - 表达式有返回值，语句没有返回值
    - Python 语法基于**冒号**和**缩进**，缩进可以选择用 tab 或者空格，但在整个程序中要保持一致

        ```python
        '''
        Check if input-number > 42
        '''
        aStr = input("Input: ")
        # print aStr
        aInt = int(aStr)
        if aInt > 42:
            print("> 42")
        else:
            print("<= 42")
        ```

        - 多行注释：`"""…"""` 或者 `'''…'''`，也是 PyDoc 的写法
        - 标准输入：`input("Prompt string: ")`
        - 单行注释: `#...`
        - 强制缩进 / 所见即所得
        - 没有大括号 / 小括号 / 分号（其实可以有，但会被鄙视）
        - 标准输出：`print(...)`

    - python 的分支结构语法（if/elif/else）

        ```python
        if 5 > 3:
            print("5 > 3")
        elif 5 > 4:
            print("5 > 4")
        else:
            print("5 < 4")

        # 三目运算符
        d = 32 if 15 > 14 else 16
        ```

    - 比较运算符：`>, >=, <, <=, !=, ==, is`，同类型对象之间的比较有意义，不同类型之间比较无意义。

        == 表示值相等，is 表示引用相同

        支持：4>3>2, 5>4<6>5>3，只要所有相邻两个值关系成立，结果即为 True

        冷知识（用不到，单纯介绍）：序列的比较是从头开始，依次比较每一个元素；集合的比较是：子集/超集；字典的比较是将 key 排序，然后逐个比较 key 值

    - 逻辑运算符：not, and, or，存在短路效应
    - python 的循环语法

        ```python
        # while 循环
        i = 0
        while i < 10:
            print(i)
            i += 1
        else:
            print(i)

        # for 循环
        for i in range(10):
            print(i)
        else:
            print(i)
        ```

        **注意这里的 else，如果由 break 跳出循环，就不会执行 else block，反之就会执行**

#### 1.2.5 帮助文档 Pydoc

- 交互环境：查询 sys 模块的帮助文档：`help(sys)`
- chm 文档（Windows 环境）
- 本地网页，执行 Shell：`python -m pydoc -p 1234`，Web 浏览器访问：<http://localhost:1234>

### 1.3 变量和对象

[返回目录](#课程目录)

#### 1.3.1 变量

- 变量（引用）的概念
    - 变量本身没有类型，对象才有类型，引用可以映射到不同类型的对象
    - 变量要赋值（映射到对象）才能使用
    - 变量只有位于等号左边的时候表示为变量建立映射关系，其他时候都表示其映射到的对象本身。
    - 没有被引用映射的对象会被 PVM 的 GC 机制回收
- 变量的命名规则
    - 由字母，下划线，数字组成，且首字符不为数字
    - 区分大小写

#### 1.3.2 对象的属性 attribute

- 字段（field）属性和方法（method）属性
    - 字段属性用来描述对象的特征
    - 方法属性用来表示对象的行为
- 函数和对象的方法属性
    - 关联到特定对象的函数叫方法
    - 不关联到特定对象的通用方法叫函数
- 反射和自省
    - `id()` 函数，可以查看对象在 PVM 中的 hash（身份证号）
    - `__dict__` 属性或者 `dir()` 函数可以查看对象的属性

#### 1.3.3 对象的可变性

- 不可变（Immutable）对象

    包括：整数，浮点数，字符串，元组，不可变集合

    ```python
    aStr = "haha"
    aStr[2] = "e" # Error!
    ```

    对于不可变对象，通常值相等的在PVM中就只保留一份，所以两个值相等的不可变对象，通常其引用也相同。

- 可变（Mutable）对象

    列表，集合，字典

    ```python
    aList = ['h', 'a', 'h', 'a']
    aList = "e" # OK!
    aList.sort()
    ```

#### 1.3.4 在 PVM 中的存储模型

- 数字、字符串、元组、列表

    ![](images/python-objects-storage-model.png)

- 文件、类

    ![](images/python-function-file-class-instance.png)

#### 1.3.4 对象的复制

- 重映射
    - 等号赋值
    - 实参传递
    - 函数返回值
- 浅拷贝
    - `copy.copy(aObj)`
    - 绝大多数运算符运算之后都会生产新的对象，比如序列的切片，加法，乘法
    - 对可变对象，`+=` 需要注意（它改变原对象）
- 深拷贝
    - `copy.deepcopy(aObj)`

### 1.4 基本对象类型

[返回目录](#课程目录)

参考：<https://docs.python.org/3/library/stdtypes.html>

#### 1.4.1 整数对象（int）

- 整数对象的写法
    - 默认为十进制：`42`
    - 也可以用八进制或者十六进制书写：`0o52`，`0x2a`
    - 可以认为 Python 中能处理的最大整数只取决于该机器的内存
- 基本运算：加减乘除，乘方，整除，取余：`+ - * / ** // %`
    - Python 2 中 `/` 是整除：`5/2 -> 2`
    - python 3 中 `/` 是小数除法：`10/2 -> 5.0`
- 取整运算

    ```python
    截尾取整 int(3.54) -> 3
    向上取整 math.ceil(3.14) -> 4
    向下取整 math.floor(3.14) -> 3
    四舍五入 round(3.14) -> 3, round(3.54) -> 4
    ```

- 字符串转换成整数

    ```python
    按十进制转换
    int("12") -> 12

    按八进制转换
    int("12", 8) -> 10

    按十六进制转换
    int("12", 16) -> 18
    ```

- 整数转换成字符串

    ```python
    转换成十进制形式
    str(12) -> "12"
    "%d" % 12 -> "12"

    转换成八进制形式
    oct(12) -> "014"
    "%o" % 12 -> "14"

    转换成十六进制形式
    hex(12) -> "0xc"
    "%x" % 12 -> "c"
    "%X" % 12 -> "C"
    ```

#### 1.4.2 浮点数对象（float）

- 浮点数对象的写法，带小数点：`3.1415`
- 浮点数的基本运算：加减乘，乘方：`+  -  *  **`
- 浮点数的除法
    - 浮点数和整数一起运算，返回浮点数：`5.0 / 2`
    - Floor 除法：结果是不大于商的最大整数

        ```python
        5 // 2 -> 2
        5 // -2 -> -3
        ```

- 数字的常用函数

    ```python
    int(x)
    float(x)
    divmod(x, y)
    pow(x, y)
    round(x, n)
    abs(x)

    sum(seq)
    max(seq)
    min(seq)

    eval(aStr)
    ```

> **练习作业**：随机生成两个 10 以内的实数（精确到小数点后两位）并输出到屏幕，要求用户输入它们的和，然后判断用户的输入值，然后输出 True/False。
>
> ```python
> 程序运行后界面上显示 Please input sum for 4.96 + 4.91 =
> 然后用户输入 9.87
> 程序输出 True
> ```
>
> [参考](python-exec-public.py#L117-138)

#### 1.4.3 字符串（str）

- 引号
    - 单引号和双引号效果一样，但是都要成对使用
    - 单双引号可以相互嵌套，以避免使用转义

        ```python
        print('isn\'t')
        print("isn't")
        ```

    - 三个单引号或者双引号可以产生多行字符串
- 单行内容太长，分行输入

    ```python
    h1 = "haha \
                Ok"
    h2 = ("haha"
                "xixi")
    ```

- 转义符：`\', \", \\, \n, \t, \b`
- 原始字符串（不转义）

    ```python
    print(r't\nt')
    print('t\\nt')
    ```

- 二进制字符串（）

    ```python
    >>> '测试'.encode()
    b'\xe6\xb5\x8b\xe8\xaf\x95'
    >>> '测试'.encode('utf-8')
    b'\xe6\xb5\x8b\xe8\xaf\x95'
    >>> '测试'.encode('cp936')
    b'\xb2\xe2\xca\xd4'
    >>> b'\xb2\xe2\xca\xd4'.decode('cp936')
    '测试'
    ```

- 加法和乘法

    ```python
    "hello " + "world!"
    "-" * 20
    ```

- 切片 Slice

    ```python
    aStr = "hello, world!"
    print(aStr[0], aStr[-1])
    print(aStr[2:-1]) # 左闭右开
    print(aStr[2:], aStr[:2], aStr[None:2])
    print(aStr[::2], aStr[-1::-1], aStr[::-1])
    ```

- 字符串的常用方法

    ```python
    replace
    count
    find/index
    capitalize/title
    isalpha/isdigit/isalnum
    isspace
    split
    join
    endswith/startswith
    lower/upper
    strip/rstrip/lstrip
    ```

- 字符串常用函数和操作

    ```python
    len("haha")

    chr(70)
    ord('F')

    for x in "hello":
	    print(x)

    if "he" in "hello":
	    print(True)
    ```

- 格式化字符串

    ```python
    "%d %s" % (5, "world")
    "%06.2f" % 3.1415 # 这里的 0 还可以是 +, -, 空格
    # 格式化输出的种类 %s, %r, %c, %d, %i, %u, %o, %x, %X, %e, %E, %f, %g, %G, %%

    '{1},{0},{1}'.format('kzc',18)
    '{a},{b}'.format(a=18,b='kzc')

    a, b, c = 1, 2, 3
    f'{a} + {b} = {c}'
    ```

> **练习作业**：提示用户输入一个字符串，判断该字符串是否回文（回文是指正读反读都一样，比如 accbcca / 123321 是回文）。
>
> [参考](python-exec-public.py#L252-271)

> **练习作业**：提示用户输入一个句子，去掉行首行末的空白，单词之间的空白统一格式化成一个空格。
>
> ```python
> 输入 "It is      my  book. "
> 输出 "It is my book."
> ```
>
> [参考](python-exec-public.py#L234-251)

#### 1.4.4 元组（tuple）

- 元组的初始化

    ```python
    t = (0, "Ni", 1, 0)
    t = (0,) # 单元素元组的末尾要加上逗号，以区别括号运算符，这里若没有逗号就等于0
    t = (0, "Ni", 1, (4, 5,)) # 元组可以嵌套另一个元组或者其它任意对象
    t = tuple("hello") # 从其它可迭代对象生成元组
    ```

    元组赋值：`a,b,c = 1,2,3`

- 元组是**不可变的引用序列对象**
    - 元组是序列，序列元素是引用（临时变量）
    - 元组是不可变对象
- 元组赋值运算

    ```python
    >>> a, b = 4, 5
    >>> (a, b) = 4, 5
    >>> a, b = (4, 5)
    >>> (a, b) = (4, 5)
    >>> (a, b) = (b, a+b)
    >>> a, b = b, a+b
    >>> a, b = divmod(5, 3)
    ```

- 序列的通用表达式和函数

    ```python
    if x in s / if x not in s

    if "ha" in "haha":
        print(True)

    for x in s:
        print(x)

    s + t, s += t
    "hello" + " world!"
    对可变序列对象，s+=t会改变s对象本身

    s * n, n * s
    "hello" * 5

    s[i], s[i:j], s[i:j:k]
    len(s), min(s), max(s)

    sorted()
    sorted([1, 4, 3, 2]) # 排序后生成一个新的列表并返回
    ```

#### 1.4.5 列表（list）

- 列表的初始化

    ```python
    t = [0, "Ni", 1, 3]
    t = [0, "Ni", 1, [4, 5]] # 列表可以嵌套另一个列表或者其它任意对象
    t = list("haha") # 从其它可迭代对象生成列表
    t = list(range(3)) # 生成数字列表：[0, 1, 2]
    ```

- 列表是可变的引用序列对象
    - 列表是序列，序列元素是引用（临时变量）
    - 列表是可变对象
- 列表常用方法

    ```python
    # append / extend
    aList = [1, 3, 2, 4, 7, 6]
    aList.append([4, 5]) # 不生成新的列表对象，而是改变原对象本身
    aList.extend([4, 5])

    # sort
    aList.sort()

    # insert
    aList.insert(1, 4)

    # reverse
    aList.reverse()

    # pop / remove
    aList.pop() # 删除并返回最后一个元素
    aList.remove(1) # 删除指定的元素，没有返回值
    ```

- 列表常用运算

    ```python
    # del L2[i:j]
    del aList[2]
    del aList[0: 1] # 删除变量和映射关系，而非删除对象本身

    # L2[k] = N / L2[i:j] = L3
    aList[2] = 5 # k不可以越界访问
    aList[1:2] = [4, 5, 6] # 等号左边的索引仍然代表一个左闭右开的区间，等号右边的列表表示填入的内容。

    zip()将多个列表合成一个元组对列表
    list(zip([1, 2, 3], ["apple","pear","banana"]))
    ```

- 列表解析

    列表解析的本质是：

    - 遍历可迭代对象的每一个元素
    - 将遍历到的元素代入前端的表达式进行运算
    - 用运算结果生成一个新的列表对象

    列表解析举例

    ```python
    [i**2 for i in range(5)]
    [str(i) for i in range(5) if i > 3]
    [ord(i) for i in "hello"]
    ```

> **练习作业**：提示用户输入若干（>3）个评分，去掉一个最高分，一个最低分，求平均分，保留2位小数。
>
> ```python
> Please input some integer numbers:
> 9 7 5 0 100
> The average is: 7.00.
> ```
>
> [参考](python-exec-public.py#L320-338)

> **练习作业**：提示用户输入一个整数，输出比它小的能被三整除的自然数。
>
> ```python
> Please input a integer:
> 50
> 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48
> ```
>
> [参考](python-exec-public.py#L453-466)

> 思考题：
>
> ```python
> a = [[0]] * 3
> a[0][0] = 1
>
> print(a) # 结果是？
>
> # 进一步思考下以下两者的区别：
> a = [0]
> [a for i in range(3)]
> [[0] for i in range(3)]
>```

#### 1.4.6 序列和散列

序列和散列都是可迭代对象

- 序列包括：字符串/元组/列表
    - 元素有序排列
    - 元素可以重复
- 散列包括：集合/不可变集合/字典
    - 元素没有顺序
    - 元素（键）不可以重复

#### 1.4.7 集合（set）

- 集合的初始化

    ```python
    x = set("hello") # 从其它可迭代对象生成集合
    ```

- 集合表示一些元素的无序集合

    无重复元素，可以用于剔除序列中的重复元素

- 集合只能包含可以计算哈希值的对象（hashable）

    Python 内建的不可变对象都是 hashable 的，元组是 hashable 的，列表不是

    ```python
    >>> set([range(5), range(3)])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    ```

- 集合的常用运算

    ```python
    x - y # 差集
    x & y # 交集
    x | y # 并集
    x ^ y # 外集
    x < y # 真子集
    x <= y # 子集
    x >= y # 超集
    ```

- 集合的常用方法

    ```python
    aSet.update(bSet)
    aSet.intersection_update(bSet)
    aSet.difference_update(bSet)
    aSet.symmetric_difference_update(bSet)
    aSet.add(x)
    aSet.remove(x)
    aSet.discard(x) # remove if exist
    aSet.pop()
    aSet.clear()
    ```

- 不可变的集合（frozenset），不可变对象

    frozenset 和 set 的关系，相当于 tuple 和 list 的关系

> **练习作业**：translations 由哪些不同的字母组成？

> **练习作业**：smiles 和 translations 这两个单词有哪些共有字母（s/i/l），哪些独有的字母（比如 smile 有 m/e）？

#### 1.4.7 字典（dict）

- 字典的初始化

    ```python
    aDict = {'apple': 1.5, 'pear': 2.3}
    aDict = dict(apple = 1.5, pear = 2.3)
    aDict = dict([("apple",1.5), ("pear",2.3)])
    ```

- 键只能是 hashable 的对象，不能重复，通常用字符串或者数字
- 值可以是任意对象，可以重复
- 字典的常用方法

    ```python
    aDict.items()
    aDict.keys()
    aDict.values()
    aDict.copy()
    aDict.get(k[,x])
    aDict.setdefault(k[,x])
    aDict.pop(k[,x])
    aDict.clear()
    ```

- 字典的常见运算
    - 访问字典中的元素

        ```python
        aDict = {"apple":1.5, "banana":2.4}
        print(aDict["apple"])
        print(aDict["pear"]) # 访问不存在的键会报错
        ```

    - 添加一个元素

        ```python
        aDict["pear"] = 3.2
        ```

    - pprint.pprint，用于 Debug 时更清晰地 Dump 复杂对象
    - 基于字典的格式化

        ```python
        "%(n)d %(x)s %(n)d" % {"n":1, "x": "spam"}
        '{a},{b}'.format(a=18,b='kzc')

        aDict = {"n":1, "x": "spam"}
        f'{aDict["n"]} {aDict["x"]}'  # '1 spam'
        ```

> **练习作业**：提示用户输入一行字符串，统计并输出其中每个字符出现的次数。
>
> ```python
> Please input a Str:
> abcdcdabcd
> The stat char list:
> a => 2
> c => 3
> b => 2
> d => 3
> ```
>
> [参考](python-exec-public.py#L468-497)

- 散列的通用运算

    ```python
    # if x in hash / if x not in hash
    if "h" in set("ha"):
        print(True)
    if "h" in aDict:
        print(True)   # 判断 aDict 中是否有 "h" 这个键

    for x in h:
        print(x)

    len(s), min(s), max(s)

    sorted # 对散列元素排序后生成一个列表
    sorted(set(1, 4, 5))
    sorted(aDict)
    ```

## 2. 进阶

[返回目录](#课程目录)

### 2.1 函数和高阶函数

[返回目录](#课程目录)

#### 2.1.1 函数的定义和调用

- 函数对象的属性
    - 函数名称：`__name__`
    - 输入参数（个数和默认值）
    - 函数体
    - 返回值
    - 函数文档：`__doc__`
- 函数定义的过程
    - 产生一个函数对象
    - 将这个函数对象和函数名变量建立映射关系
    - 多次定义同名函数，则后定义的会简单覆盖前面的

    ```python
    def add(a, b=3):
        """
        add function
        >>> add(4, 5) 9
        """
        return a + b

    print(add.__name__)
    print(add.__doc__)
    print(add(4, 5), add(7))
    ```

- 函数内的变量访问规则
    - LEGB：Loca /Enclosed/Global/Built-in
    - 凡是函数内有赋值运算的变量就是 local 变量
    - 如果确实要在函数中修改全局变量，需要用 global 修饰符

    > 思考题（以下代码的运行结果是？）：
    >
    > ```python
    > a = 42
    >
    > def aFun():
    >     a += 1
    >
    > aFun()
    > print(a)
    >```

- 命名空间用来避免变量名冲突
    - 函数对象：局部变量
    - [模块对象](#351-模块)：模块的属性（模块中的全局变量和函数）
    - 类对象：类的属性（字段和方法）
    - 实例对象：实例的属性（字段和方法）
- 函数的实参写法
    - 普通传参 `add(4, 5)`
    - 命名传参 `add(b=5, a=4)`
    - 元组传参 `add(*(4, 5))`
    - 字典传参 `add(**{'a':4, 'b':5})`
- 函数的形参写法
    - 序列变长参数 `def echo(*args): print(args)`
    - 字典变长参数 `def echo(**kwargs): print(kwargs)`
    - 形参顺序
        - 非默认参数要放在默认参数前面
        - 定长参数列表要放在变长参数前面

            ```python
            def echo(arg, *args):
                print(arg, args)
            ```

        - 序列变长参数要放在字典变长参数前面

            ```python
            def echo(arg, *args, **kwargs):
                print(arg, args, kwargs)
            ```

    - 默认参数

        **注意：默认参数的值在函数定义时确定**

        > 思考题（以下代码有什么问题？）：
        >
        > ```python
        > import time
        >
        > def myLog(msg, timestamp=time.time()):
        >     print(f'[{timestamp}]::{msg}')
        >
        > myLog("test")
        > time.sleep(2)
        > myLog("test", time.time())
        >```

        **注意：默认参数的值尽量不要是可变参数**

        > 思考题（以下代码有什么问题？）：
        >
        > ```python
        > import time
        >
        > def addItem(aList=[], i=42):
        >     aList.append(i)
        >     return aList
        >
        > print(addItem([1,2,3], 4))
        > print(addItem())
        >```

- 函数的参数和返回值
    - 参数传递和接收返回值的本质都是映射关系的建立
        - 参数传递本质上就是将实参对象和形参变量建立映射关系
        - 接收返回值本质上就是将返回值对象和接收返回值的变量建立映射关系
        - 如果希望传入参数和函数外部的逻辑解耦，需要传入实参的浅拷贝或者深拷贝。
    - 返回值可以是多个，但本质上是一个元组
        - `return 3,5` == `return (3,5)`
        - `a, b = fun()` == `aTuple = fun(); a, b = aTuple`

#### 2.1.2 高阶函数

- Lambda 函数

    ```python
    fun = lambda x: x**2

    fun(3)
    (lambda x: x ** 2)(3)
    ```

    lambda 的使用场合

    - 定义只用一次的简单函数
    - 尤其用于 callback 场合

- 回调函数

    回调 callback 的定义

    - 回调本质上是将函数对象 A 作为一个参数传递给另一个函数或方法 B 。
    - B函数被调用时，会在函数体中调用 A 函数对象

    因为 A 函数对象是在运行时作为实参动态传递给B函数，所以 B 函数在定义时并不知道 A 函数的具体信息

    回调函数的适用场合

    - 事件驱动编程模型，比如 [TK-GUI](python-exec-public.py#L1512-1550)
    - 异步编程模型

- map

    `map(fun, aIter[, bIter...])`

    map函数的本质

    - 第一个参数是函数对象，后续参数是一个或多个可迭代对象
    - 会将可迭代对象的每一个元素作为参数传递给函数对象，并将返回值组 合成一个生成器返回

    举例

    - `map((lambda x:x+10), range(5))`
    - `map(pow, [1, 2, 3], [2, 3, 4])`

- filter

    `filter(fun, iters)`

    filter函数的本质

    - 第一个参数是函数对象，第二个参数是一个可迭代对象
    - 会将可迭代对象的每一个元素作为参数传递给函数对象，并将返回值为 True的可迭代对象组合成一个生成器返回

    举例

    - `filter((lambda x: x>0), range(-5,5))`
    - `filter(lambda x: sum(x) > 10, zip([5, 6, 7], [4, 5, 6]))`

- reduce

    ```python
    from functools import reduce
    reduce(fun, iters[, initial])
    ```

    reduce函数的本质

    - 第一个参数是函数对象，第二个参数是一个可迭代对象，第三个可选参数是初始值
    - 无初始值

        ```python
        reduce(lambda x,y: x+y, [1,2,3,4,5]) -> ((((1+2)+3)+4)+5)
        reduce(lambda x,y: x+y, []) -> TypeError

        ```
    - 有初始值

        ```python
        reduce(lambda x,y: x+y, [1,2,3,4,5], 10) -> (((((10+1)+2)+3)+4)+5)
        reduce(lambda x,y: x+y, [], 10) -> 10
        ```

- 其它
    - sort/sorted/key

        `sorted(['10','apple','e'], key=len)`

        ```python
        fruits = {'apple':10, 'pear': 4.5, 'banana': 5.8, 'mango':6.7, 'orange':2.8}

        for k in sorted(fruits, key=lambda x:fruits[x]):
            print(f'{k}\t=>\t{fruits[k]}')

        def mySort(aList, key=lambda x:x):
            for i in range(len(aList)):
                for j in range(i, len(aList)):
                    if key(aList[i]) > key(aList[j]):
                        aList[i], aList[j] = aList[j], aList[i]
            return aList

        print(mySort([1,2,3,6,5,4]))
        ```

    - min/max 等
    - 偏函数：为函数对象设置新的默认参数（返回值是函数）

        ```python
        def int2(x, base=2):
            return int(x, base)

        >>> int2('1000000')
        64
        >>> import functools
        >>> int2 = functools.partial(int, base=2)
        >>> int2('1010101')
        85
        ```

### 2.2 类和实例

[返回目录](#课程目录)

#### 2.2.1 类的定义和实例化

```python
class AClass(object):
    """
    AClass Spec

    This a AClass
    """
    aField = "testField"
    def aMethod(self):
        print("testMethod")

print(AClass.__name__)
print(AClass.__doc__)
print(AClass.__dict__)
print(AClass.__base__)
```

- 类对象的属性
    - 类名称: `__name__`
    - 类文档: `__doc__`
    - 类的属性字典: `__dict__`
    - 类的第一个父类: `__base__`
- 类定义的过程
    - 产生一个类对象
    - 将这个类对象和类名变量建立映射关系
    - 多次定义同名类，则后定义的会简单覆盖前面的
- 新式类/经典类
    - Python 3 中默认是新式类
    - 在 Python 2 中，新式类需要继承 object，经典类不继承 object

```python
class AClass(object):
    aVar = "testVar"
    bVar = [1,2,3]
aObj, bObj = AClass(), AClass()

print(aObj, bObj)
print(aObj.__class__, bObj.__class__)
print(aObj.aVar, aObj.bVar)

aObj.aVar = "newString"
print(aObj.aVar, bObj.aVar, AClass.aVar)

aObj.bVar[2] = "newItem"
print(aObj.bVar, bObj.bVar, AClass.bVar)

aObj.newVar = "newVar"
# AClass.newVar = "newVar"
print(aObj.newVar, AClass.newVar)
```

- 实例化的本质

    以类对象为模版，生成实例对象的过程

    ```python
    str(object='') -> string
    >>> str()
    ''
    >>> str(42)
    '42'
    ```

- 实例对象的属性
    - 类信息: `__class__`
    - 访问实例对象的属性时，如果发现没有，会去它的类对象中查找
    - 实例对象可以有自己的属性，并且可以动态增加
- ***[了解即可] 伪私有属性***

    属性的访问权限

    - 私有属性：只能在其所属类的代码中被调用
    - 公有属性：能在所属类以外的代码中被调用

    私有属性的作用

    - 约束类库的接口
    - 增加类库代码的安全性
    - 确保客户端代码的兼容性

    伪私有属性

    - Python中所有的属性都是公有的
    - 为了约束接口，Python增加了伪私有属性：在定义类时，以双下划线为前缀的属性即为伪私有属性。Python会自动帮你加上类前缀。
    - 注意：在定义好类之后，再添加以双下划线为前缀的属性，不是伪私有属性。
- 方法属性
    - 类的方法属性本质上都是成员方法
    - 成员方法带有一个 self 参数，并位于形参列表的第一位
    - self 代表的就是类的实例对象

    特殊的方法属性

    - 类方法 `@classmethod`
    - 静态方法 `@staticmethod`
    - 属性 `@property`

#### 2.2.2 钩子方法和运算符重载

- 钩子方法（Hook）/ 魔术方法（Magic method）

    Hook 方法通常不会被直接 call 到，而是被绑定在其它方法或者运算符上

    ```python
    3+5 -> (3).__add__(5)
    str(3) -> (3).__str__()
    ```

- 运算符重载

    除了显示的运算符，隐式的运算也被包含在运算符重载的范畴中，比如实例化，点号运算，括号运算等都算在内。

    - 初始化方法: `__init__`

        ```python
        class Test(object):
            def __init__(self, param):
                    self.param = param
            def testMethod(self):
                    print(self.param)

        a = Test("haha")
            a.testMethod()
        ```

    - 字符串方法：`__str__` 和 `__repr__`

        ```python
        class Test(object):
            def __str__(self):
                return "str"
            def __repr__(self):
                return "repr"

        a = Test()
        print(a, str(a), repr(a))
        ```

        `str()` 和 `print` 在找不到 `__str__` 方法会去找 `__repr__`，`repr()` 则不会找 `__str__`，所以应该优先实现 `__repr__` 方法。

    - 点号运算符（访问属性）：`__getattr__`

        ```python
        class Test(object):
            def __init__(self, param):
                self.param = param
            def __getattr__(self, param):
                print(param + "not found!")

        a = Test("haha")
        print(a.param)
        a.dddd
        ```

    - 括号运算符（函数调用）：`__call__`

        ```python
        class A(object):
            def __call__(self):
                return 42

        a = A()
        print a()
        ```

        与函数相比，实例对象有什么优势？

        - 纵向扩展：类的继承
        - 更好的封装：可以将子函数封装成类的成员方法

        “闭包”和类

        ```python
        def addN(n):
            def add(x):
                return x+N
            return add

        class addN(object):
            def __init__(n):
                self.n = n
            def __call__(x):
                return x+self.n

        add3, add4 = addN(3), addN(4)
        print(add3(42), add4(42))
        ```

    -  其它运算符重载

        ```python
        __new__
        __cmp__
        __index__
        __lt__, __le__, __gt__, __ge__, __eq__, __ne__
        __add__, __sub__, __mul__, __div__
        __del__
        ```

-  动态属性
    - 为类对象动态绑定属性，影响所有的实例
    - 为实例对象动态动态绑定属性，影响单一实例

    属性绑定: `__slot__`

    ```python
    class Student(object):
        __slots__ = ('name', 'age')
    s = Student()
    s.name = 'Michael'
    s.age = 25
    s.score = 99 # AttributeError
    ```

    slots 定义的属性仅对当前类起作用，对继承的子类是不起作用的，除非在子类中也定义 slots，这样子类允许定义的属性就是自身的 `__slots__` 加上父类的 `__slots__`。

#### 2.2.3 继承和组合

- 继承的意义
    - 子类获得父类所有的属性和方法
    - 分层抽象，结构明确
- 继承树

    ```
                child
                /    \
        father_1    father_2
        /       \    /    \
    ff_1    ff_2  gg_1   gg_2
    ```

- 多继承时的属性查找顺序
    - 子类中属性或方法的查询顺序：由上而下，从左到右。
    - 若查完整棵树没有找到，抛出异常。
    - 经典类深度优先，由左及右。新类广度优先。
- 类继承中的常用方法

    isinstance 用于判断一个对象的类型

    ```python
    >>> isinstance(1, int)
    True
    >>> isinstance(1, (int, str))
    True
    ```

    super

    ```python
    # 用于在新式类中调用父类方法
    # 实际不止是在调用父类方法那么简单

    class AClass(object):
        def __init__(self):
            print("Aclass")

    class BClass(AClass):
        def __init__(self):
            super().__init__()
            print("BClass")
    bVar = BClass()
    ```

### 2.3 正则表达式

[返回目录](#课程目录)

正则表达式是最犀利的字符串处理工具。以 Perl 语言的正则表达式规范为基础形成的正则表达式 POSIX 标准，被广泛应用于各种语言和各种场合。

- 模式匹配的步骤
    - 模式编译
    - 模式匹配
- Search vs Match
    - 模式能匹配到字符串的子串时，Search 返回 True，否则返回 False
    - 模式能匹配到字符串的全部时，Match 返回 True，否则返回 False

    ```python
    import re

    reCmp = re.compile("\d{3,5}")
    if reCmp.search("http404"):
        print("Match!")
    else:
        print("Non-Match!")

    if reCmp.match("http404"):
        print("Match!")
    else:
        print("Non-Match!")
    ```

- 正则表达式规则

    ```
    . 换行以外的任意字符
    + 前面一个元素出现一次或多次
    * 前面一个元素出现零次或多次
    {x, y} 前面一个元素出现[x, y]次之间
    [] 选择框
    [a-z0-9_+]
    [^A-Z]
    ^ 开头
    $ 结尾
    ? 前面一个元素出现零次或一次
    () 组合框
    (ab)+
    | 或
    A|B
    \ 转义
    \\, \w, \s, \d, \b, \W, \S, \D, \B
    ```

    ```
    I  IGNORECASE
    Perform case-insensitive matching.

    L  LOCALE
    Make \w, \W, \b, \B, dependent on the current locale.

    M  MULTILINE
    "^" matches the beginning of lines (after a newline) as well as the string. "$" matches the end of lines (before a newline) as well as the end of the string.

    S  DOTALL
    "." matches any character at all, including the newline.

    U  UNICODE
    Make \w, \W, \b, \B, dependent on the Unicode locale.
    ```

- 贪心和非贪心匹配

    ```python
    *?, +?, ??, {m,n}?
    >>> reCmp = re.compile("(.+?)(.+)")
    >>> reObj = reCmp.search("Hello")
    >>> reObj.groups()
    ('H', 'ello')
    >>> reCmp = re.compile("(.+)(.+)")
    >>> reObj = reCmp.search("Hello")
    >>> reObj.groups()
    ('Hell', 'o')
    ```

- 标记匹配

    ```python
    >>> reCmp = re.compile(r"(\d)(\s+)\1")
    >>> reCmp.search("2 2")
    <_sre.SRE_Match object at 0x10fe6a690>
    ```

- 取得匹配值

    ```python
    line = "Code: A127Z"
    match= re.search('(\w)((\d{3})(\w))', line)
    items = match.groups()
    # 按左括号的先后顺序排列
    ```

- 匹配替换

    ```python
    line = "This is fun"
    print(re.sub("i\w", "was", line))
    line = "dig, dag, dog"
    print(re.sub("d.g", "cat", line, 2))
    ```

- 查找所有匹配（Findall/Finditer）

    ```python
    line = "Code: A127Z Code: B999Y"
    items=re.findall('(\w)(\d{3})(\w)', line)
    items=re.finditer('(\w)(\d{3})(\w)', line)
    ```

- 匹配切割

    ```python
    line = "Code: A127Z Code: B999Y"
    items=re.split('\w\d{3}\w', line)
    ```

### 2.4 异常处理

[返回目录](#课程目录)

## 3. 开发相关

[返回目录](#课程目录)

### 3.1 版本控制

[返回目录](#课程目录)

### 3.2 自动化测试

[返回目录](#课程目录)

### 3.3 自动化任务

[返回目录](#课程目录)

### 3.4 开发规范

[返回目录](#课程目录)

### 3.5 模块和打包

[返回目录](#课程目录)

#### 3.5.1 模块

- 模块对象的本质
    - 就是 Python 文件
    - 文件名必须符合变量的命名规则

    import 模块对象的流程

    - 预编译模块对应的 Python 文件为 pyc 文件
    - 运行一遍这个 pyc 文件
    - 若该对象模块已经存在，再次 import 时不会重复运行其对应的 pyc 文件
- 顶层脚本的概念
    - 当一个 Python 文件直接被 Python 解释器启动，这个 Python 文件被称为该进程的顶层脚本。
    - 顶层脚本和模块
        - 顶层脚本的文件名可以不符合变量的命名规则
        - 顶层文件在运行前，不会被预编译成 pyc 文件
        - 一个进程中的顶层文件可以是另一个进程里的普通模块（只要它符合模块的命名规则）
- 包对象的本质
    - 包含 `__init__.py` 模块的文件夹
    - 文件夹的命名必须符合变量的命名规则
    - 包对象是特殊的模块对象

        ```python
        >>> import testPkg
        >>> testPkg
        <module 'testPkg' from 'testPkg/__init__.pyc'>
        ```
    - import 包对象就是预编译和运行对应的 `__init__.py` 文件
- import 的注意事项
    - **不同的 import 方式，访问到的是相同的模块对象，因为实际只会 import 一次**

        ```python
        >>> import testPkg
        >>> testPkg.testModule
        <module 'testPkg.testModule' from 'testPkg/testModule.py'>
        >>> from testPkg import testModule
        >>> testModule
        <module 'testPkg.testModule' from 'testPkg/testModule.py'>
        >>> from testPkg import testModule as fakeModule
        >>> fakeModule
        <module 'testPkg.testModule' from 'testPkg/testModule.py'>
        >>> id(testPkg.testModule), id(testModule), id(fakeModule)
        (4454769784, 4454769784, 4454769784)
        ```

    - **import 会逐个运行模块路径上的所有包和模块一次且仅运行一次。初次 import 的过程，是运行一个模块，然后将其关心的对象映射到一个变量。**

        ```python
        import aModule
        import aPkg
        from aPkg import aModule
        from aPkg import aModule as bModule
        from aPkg.aModule import aVar as bVar
        from aModule import *
        ```

    - `__import__` 的用法

        ```python
        sys = __import__('sys')
        # 等价于 import sys
        ```

    - `__import__` 和 `import` 的区别
        - import 是语句，import 模块必须 hardcode 在代码里
        - `__import__` 是函数，所以可以动态的 import 输入字符串所对应的模块
- 模块的搜索路径
    - `sys.path` 中包含的路径

        `sys.path` 和 `sys.argv` 一样，是进程起来时被自动赋值的变量，值从父进程的环境变量里读取

    - 当前目录
    - 可以访问到的包对象 `from math import pi`
- reload 的作用
    - `from imp import reload`
    - reload 只对模块对象起作用
    - reload 可以完成模块的再次加载

    ```python
    import time
    import testModule
    from imp import reload

    while True:
        import testModule
        # reload(testModule)
        testModule.echo()
        time.sleep(2)
    ```

- 模块的常用方法

    ```python
    __name__

    if __name__ == '__main__':
        print(f'hello, {__name__}')

    # python -m test

    __dict__
    __doc__
    ```

#### 3.5.2 打包

## 4. Web 开发

[返回目录](#课程目录)

### 4.1 MVC 框架

[返回目录](#课程目录)

### 4.2 Restful API

[返回目录](#课程目录)

### 4.3 服务部署

[返回目录](#课程目录)

## 5. 算法和设计模式相关 TODO

[返回目录](#课程目录)

### 5.1 算法复杂度

[返回目录](#课程目录)

- 时间复杂度和空间复杂度
- 排序算法
    - 选择排序 O(n)=n²

        *searches the smallest value and swap it with the first value, then the same with the next position and with the next, and next and so on...*

        Best case: ，Worst case: O(n)=n²

        ![](images/sort-selection.gif)

    - 插入排序 O(n)=n²

        *Turn the first card, then turn the others till you find a smaller one and then you would swap them.*

        ![](images/sort-insertion.gif)

    - 冒泡排序 O(n)=n²

        *It compares two neighboring values with each other and swap them if they are in the wrong order. It continues with next position right.*

        ![](images/sort-bubble.gif)

    - 快速排序 O(n)=n*log(n)

        *It chooses a value and order all values which are smaller in front of the pivot and all bigger ones behind it. It does that in a more and more smooth range with more and more pivots.*

        ![](images/sort-quick.gif)

    - 归并排序 O(n)=n*log(n)

        *It splits up the list in multiple lists with one or two elements. It is ordering them and then it begins to merge the lists again to bigger lists.*

        ![](images/sort-merge.gif)

    - 不同排序算法用于不同数据集中的情形

        ![](images/sort-all.gif)

    通用排序算法的时间算法复杂度极限是 n*log(n)，但非通用算法是可以突破极限的，比如有穷集合的排序。

- 算法全貌

    ```
    各类排序算法
    随机算法
    分治策略
    二叉树
    红黑树
    动态规划
    贪心算法
    摊还分析
    B 树
    图算法
    多线程算法
    矩阵
    线性规划
    快速傅立叶变换
    数论算法
    NP 完全性
    计算几何学
    近似算法
    ```

- 算法的参考资料
    - [算法参考书]()
    - leetcode
    - 习题参考

### 5.2 算法实践

[返回目录](#课程目录)

在工作中，我们不会有太多机会《算法概论》中的各类经典算法，因此这里仅涉及一些工作中可能遇到的算法技巧。

#### 5.2.1 二进制和位运算

- 位运算
    - 运算符：`<<  >>  &  |  ^  ~`
    - 一个数做右移运算时，高位填充 0
    - 一个数与全 0 异或不变，与全 1 异或即为取反
- 例子
    - 判断 x 是否 2 的平方数：`x & (x-1) == 0`
    - flag 置位：`x | flag`
    - flag 清零：`x & ~flag`

#### 5.2.2 序列算法

- 字符串循环左移2位：abcdefg -> cdefgab
- 逐词反转：apple pear orange -> elppa raep egnaro
- 实现 Buffer，写满即覆盖最前面的内容
- 实现最小固定长度队列，若持续向队列推送数据，只保留最小的 N 个以内的值
- 固定长度栈

#### 5.2.3 散列算法

- 计数器（字典唱票算法）：aabbcccdd -> {'a':2, 'b':2, 'c':3, 'd':2,}

    > **练习作业**：提示用户输入一个句子，按首字母统计句中的单词（限定每个单词都只能由字母组成），输出统计结果。
    >
    > ```python
    > Please input a string:
    > it is my book.
    > The stat char list:
    > i => ['it', 'is']
    > m => ['my']
    > ```
    >
    > [参考](python-exec-public.py#L519-543)

- 集合算法

    > **练习作业**：提示用户输入 A、B 两个整数数列，统计并排序输出 A 数列中独有的整数，B 中独有的整数，以及 A、B 公有的整数。
    >
    > ```python
    > Please input int list A: 1 3 5 7 9
    > Please input int list B: 5 6 7
    > Only in A: [1, 3, 9]
    > Only in B: [6]
    > Both in A & B: [5, 7]
    > ```
    >
    > [参考](python-exec-public.py#L498-518)

#### 5.2.4 递归和递推

- 栈的概念
    - 一个进程中可能包含多个线程
    - 每一个线程都有自己的栈空间，用于存储该线程独有的数据，比如局部变量
- 函数和栈
    - 当一个函数在线程中被调用时，该函数调用时的参数/局部变量/返回值会逐个压入栈中保存
    - 函数调用结束再逐个弹出销毁
- 递归函数
    - 定义：函数定义中调用自身
    - 使用场合：特别适合用递归思想实现的算法
    - 使用限制
        - 要避免无限递归造成：StackOverflow
        - 递归需要频繁的出栈入栈，注重性能的算法要避免递归

    ```python
    def aFun(N):
        print("N = %d" % N)

        if N > 2:
            return
        else:
            aFun(N+1)

    aFun(0)
    ```

- 递推往往比递归更有效率

    斐波那契数列

    ```python
    def fib(n):
        if n < 3:
            return n
        else:
            return fib(n-1) + fib(n-2)

    fib(40)
    ```

    ```python
    fibList = []

    for i in range(100):
        if i < 2:
            fibList.append(i+1)
        else:
            fibList.append(fibList[i-1] + fibList[i-2])

    print(fibList)
    ```

### 5.3 设计模式实践

[返回目录](#课程目录)

#### 5.3.1 装饰器

斐波那契数列

```python
import functools

def memoize(fn):
    known=dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer
```

```python
@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n>=0), 'n must be <= 0'
    return 0 if n==0 else n + nsum(n-1)

@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n>=0), 'n must be >= 0'
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)
```

```python
from timeit import Timer

measure=[
    {'exec':'fibonacci(100)', 'import':'fibonacci','func':fibonacci},
    {'exec':'nsum(200)','import':'nsum','func':nsum}
]

for m in measure:
    t=Timer(
        '{}'.format(m['exec']),
        'from__main__import{}'.format(m['import']))
    print('name:{},doc:{},executing:{},time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'],t.timeit()))
```

#### 5.3.2 迭代器和生成器

- 迭代环境

    ```python
    any(s) / all(s) # s 是布尔类型的迭代
    sum(seq) # seq 是数字
    max(seq) / min(seq)

    for x in h:
        print(x)

    len(s), min(s), max(s)

    sorted # 对散列元素排序后生成一个列表
    sorted(set(1, 4, 5))
    sorted(aDict)
    ```

## 6. 系统相关

[返回目录](#课程目录)

### 6.1 shell 编程

[返回目录](#课程目录)

- 命令行参数
    - sys.argv，命令行参数列表
    - optparse，较好地封装了 sys.argv

### 6.2 父子进程调用

[返回目录](#课程目录)

### 6.3 文件和目录

[返回目录](#课程目录)

- 文件对象初始化

    ```python
    aFile = open('a.txt', 'w')
    # 打开模式:  'r', 'w', 'a', 'w+'，默认以只读打开

    # 文件对象的字段属性
    >>> aFile.name
    'a.txt'
    >>> aFile.mode
    'w'
    ```

- 读文件

    ```python
    aFile = open('a.txt')
    aFile.read()
    aFile.read(N)
    aFile.readline()
    aFile.readlines()

    # 以读模式打开的文件对象是一个可迭代对象，迭代时自动按行读取
    for line in open('a.txt'):
        print(line)
    ```

- 写文件

    ```python
    outputFile = open('a.txt', 'w')
    outputFile.write('test contents')
    outputFile.close()
    # 'a'是追加

    aFile.writelines(aList)
    # 等同于下面的
    for line in aList:
        aFile.write(line)
    ```

- 文件常用方法

    ```python
    flush # 有缓存的文件对象才需要
    seek # 重新定位偏移量
    tell
    truncate
    fileno
    close # 记得 close，否则可能造成文件描述符泄漏
    ```

- 标准输入输出
    - 标准输入 `input() == sys.stdin.readline().rstrip('\n')`
    - 标准输出 `print(aStr) == sys.stdout.write(aStr+'\n')`
    - 标准错误 sys.stderr，和标准输出类似，但没有缓存

    Python进程起来时，系统会自动为这三个变量绑定标准输入输出对象

    标准输出的重定向

    ```python
    output = open('a.txt', 'a')
    sys.stdout = output
    print('haha')
    ```

- Python 对象的序列化（到文件）

    ```python
    aFile = open('test.txt', 'w')
    import pickle
    pickle.dump({"a":1, "b":2}, aFile)
    aFile.close()

    bFile = open('test.txt')
    cDict = pickle.load(bFile)
    ```

- 写入二进制文件

    ```python
    aFile = open('test.bin', 'wb')
    import struct
    bytes = struct.pack('>i4sh',7,'spam', 8)
    aFile.write(bytes)
    aFile.close()
    ```

- 读取二进制文件

    ```python
    aFile = open('test.bin', 'rb')
    data = aFile.read()
    values = struct.unpack('>i4sh', data)
    ```

### 6.4 并行计算

[返回目录](#课程目录)
