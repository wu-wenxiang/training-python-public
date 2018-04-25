## 问题分类
- 核心知识
	- **基础**: 开始，开发环境搭建，基本对象和变量，流程控制，文件，函数式编程
	- **进阶**: 模块和包，类和实例，面向对象和设计模式，异常处理，正则表达式，装饰器，生成器
- 常见应用
	- **系统运维**: Bash，Python与Bash联合编程，文件和目录，系统监控，网络协议，并行处理
	- **DevOps**: 版本控制，测试，日志处理，部署，自动化管理，容器，APM
	- **Web开发**: ORM模型，Web架构和接口，MVC，WebService，Flask，Django，微信
	- **数据采集**: 爬虫，Scrapy框架
	- **数据挖掘**: 基本概念，常见类库，案例分析
- 其它应用
	- **云计算OpenStack**: 架构，安装，使用，排错 
	- **PaaS云平台**: GAE, SAE
	- **Office文档处理**: Word，Excel
	- **Python-C**: Python调用C-Lib，C调用Python-Lib，C实现Python-Module
	- **PVM内存分析和调试**：pdb，dump，windbg，gdb
	- **IoT**: 树莓板，GPIO，Azure IoT DevKit
	- **MineCraft**: MineCraft, 绘制三维图形，捕捉玩家位置，虚拟连接现实
	- **GUI**: TK
	- **区块链**: BitCoin, IoT via BitCoin

---------------------------------------
---------------------------------------


## 核心知识

### 基础
1. [开始] **Python在编程语言世界中的处于什么样的位置？**[TIOBE](https://tiobe.com/tiobe-index/)

1. [开始] **Python有什么样的特质和设计哲学？**简单，明确

1. [开始] **作为一个初入门者，我们应该怎样学习编程？**[如何成为一名黑客-Eric-S-Raymond](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/%E5%A6%82%E4%BD%95%E6%88%90%E4%B8%BA%E4%B8%80%E5%90%8D%E9%BB%91%E5%AE%A2-Eric-S-Raymond.pdf)

1. [开始] **应该选择Python2还是Python3开始学习，以及进行开发？**[参考](https://wiki.python.org/moin/Python2orPython3)

1. [开始] 如果你已经掌握了Python2或者Python3其中一门，[Python2和3有什么区别](https://docs.python.org/3/whatsnew/3.0.html)？[如何迁移](https://docs.python.org/2/library/2to3.html)？

1. [开始] Python2和Python3如何在一个系统中共存？native / venv / docker

1. [开始] **有哪些优秀的Python学习资源可以参考？**

1. [环境] **在Windows下如何搭建Python开发环境？**[参考](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Python-Dev-Env.docx)

1. [环境] 在Mac下如何搭建Python开发环境？

1. [环境] 在Linux下如何搭建Python开发环境？

1. [环境] 如何使用IDLE进行开发和调试？

1. [环境] **如何使用`Eclipse+Pydev`运行和调试Python程序？**

1. [环境] 如何使用Pycharm进行开发和调试？[Download Community](https://www.jetbrains.com/pycharm/download/#section=windows)

1. [环境] 如何使用VSCode进行开发和调试？[Download](https://code.visualstudio.com/Download)，[环境配置](https://code.visualstudio.com/docs/python/python-tutorial)

1. [环境] 如何使用VisualStudio进行开发和调试？[Download](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)

1. [环境] 还有什么其它的Python调试套件？[Notepad++](http://www.cnblogs.com/zhcncn/p/3969419.html)

1. [环境] **如何查阅Python帮助文档？pydoc, chm**

1. [数字] **如何实现取整运算？截余取整、四舍五入、向上取整、向下取整。**

1. [数字] **整数的除法运算和整除运算是如何实现的？**怎么写兼容代码？

1. [数字] **Python如何处理进制转换（整数与字符串的互相转换）？**

1. [数字] **应如何判断两个浮点数是否相等？**

1. [数字] **浮点数精度控制(`round`)和精度显示(`%.2f`)应用场景？如何编码？**

1. [数字] 在Python中我们应该如何同时取商和取余？

1. [数字] 如何对一组数据求和？求最大值？求最小值？

1. [数字] **如何产生随机数？`random/randint/choice`**

1. [数字] Python中如何进行位运算？

1. [数字] **如何理解Python中变量和对象的存储模型？id / dir / __dict__**

1. [数字] 如何理解Python语言的三个定语：动态语言，动态类型语言，强类型语言？

1. [字符] 如何编码单行、多行和分行输入的字符串？

1. [字符] 我们应该用单引号还是双引号？

1. [字符] **什么是原始字符串？**

1. [字符] **如何处理Unicode字符串和编解码问题？**

1. [字符] **如何实现字符串的乘法和加法？**

1. [字符] **如何操作字符串切片？负index、左开右闭、None、负步长**

1. [字符] **如何实现子字符串的替换、查找？**

1. [字符] 如何实现字符串的大小写转换，以及将首字母、每个单词首字母变为大写？

1. [字符] **如何实现字符串的切割和粘合？**

1. [字符] **如何移除字符串两端的空白？**

1. [字符] **如何获取字符串的长度？**

1. [字符] 如何实现ASCII码与字符的相互转换？

1. [字符] **如何格式化字符串？`%`，`format`**

1. [字符] 对象可以有哪些属性？字段属性和方法属性分别有哪些例子？

1. [字符] **什么是反射和自省机制？`__dict__`, `dir`**

1. [序列] 如何初始化一个元组Tuple对象？

1. [序列] **元组对象在PVM中的存储模型是怎样的？**

1. [序列] 基于元组的赋值语法有哪些常见的应用场景？

1. [序列] **序列的通用运算？`in`, `for`, `+/*`, 切片, `len/min/max/sorted`**

1. [序列] **如何理解列表对象的可变性与元组对象的不可变性？**

1. [序列] 生成器对象和列表对象的区别是什么？

1. [序列] **列表对象的常见运算有哪些？元素的添加，访问，排序，反序，移除，修改，遍历**

1. [序列] **什么是列表解析？**

1. [序列] **重映射，浅拷贝，深拷贝的区别是什么？**

1. [散列] 序列和散列的区别是什么？

1. [散列] 如何利用集合对序列元素去重？

1. [散列] **集合运算有哪些？**

1. [散列] 如何初始化一个字典？

1. [散列] **字典的常见运算有哪些？元素的添加，访问，移除，修改，遍历，排序，存在判断**

1. [散列] **什么是唱票算法？它适用于什么场合？Counter类能实现什么功能？**

1. [散列] 除了列表解析外，还有什么类似的语法？生成器表达式，集合解析，字典解析

1. [流程] 什么是连续赋值语法？

1. [流程] **什么是连续比较语法？**

1. [流程] 序列的比较逻辑是怎样的？

1. [流程] **什么是短路效应？**

1. [流程] 分支结构的语法是怎样的？

1. [流程] 三元运算符的语法是怎样的？

1. [流程] **Python中的循环结构语法是怎样的？else部分在什么时候会被运行到？**

1. [流程] **对序列和散列进行循环遍历应如何编码？**

1. [文件] 怎样处理命令行参数？

1. [文件] 文件对象的存储模型是怎样的？

1. [文件] **如何实现文件的读、写、flush和偏移量操作？**

1. [文件] 什么是基本输入/基本输出/基本错误？如何实现它们的重定向？

1. [文件] 如何序列化一个Python对象？

1. [文件] 如何实现二进制文件的读写？

1. [函数] **如何定义和调用一个函数？**

1. [函数] 函数对象的存储模型是怎样的？

1. [函数] **什么是LEGB规则？有哪些陷阱？`a += 3`**

1. [函数] **默认参数的陷阱有哪些？`time.time()`, `[]`**

1. [函数] 如何在函数内使用Global变量？

1. [函数] **Python中的实参传递有哪些特殊的语法？**

1. [函数] **Python中的形参传递有哪些特殊的语法？**

1. [函数] 函数传参和Return返回值时实际发生了什么？重映射？浅拷贝？深拷贝？

1. [函数] **Lambda函数的概念和语法如何？**

1. [函数] 函数调用时，临时变量是如何进栈和出栈的？栈是Per线程还是Per进程的？

1. [函数] 如何理解和编写递归函数？

1. [函数] 回调函数的语法和使用场合是怎样的？

1. [函数] **如何使用高阶函数？Map/Filter/Reduce/Sort/偏函数**

### 进阶
1. [模块] 模块对象的定义和使用是怎样的？

1. [模块] 顶层脚本和模块的区别是什么？

1. [模块] **import一个模块是实际发生了什么事？**

1. [模块] **import语法的变化和最佳实践是怎样的（避免`from x import *`，`import module`）？**

1. [模块] 为什么import应该以module为单位？

1. [模块] reload的应用场景是什么？

1. [模块] **为什么需要这样的语法？`if __name__ == '__main__': `**

1. [模块] 针对模块对象的反射语法是什么？`__import__`

1. [对象] **如何定义和实例化一个类？**

1. [对象] **类与实例的存储模型是怎样的？类的属性和实例的属性存在怎样的关系？**

1. [对象] **类中的字段属性为什么不推荐使用可变对象？**

1. [对象] 什么是伪私有属性？

1. [对象] 什么是钩子方法与运算符重载？

1. [对象] **常见的重载方法有哪些？`__init__`, `__str__`, `__call__`, `__getattr__`, `__len__`**

1. [对象] Python的继承是单继承还是多继承？继承的搜索策略是深度优先还是广度优先？

1. [对象] **Python如何实现一个符合开放封闭原则的简单工厂模式？**

1. [异常] **异常处理的语法是怎样的？else部分在什么时候会被执行？**

1. [异常] 异常处理时的执行流程是怎样的？

1. [异常] 编写异常处理逻辑时，应如何避免过度捕捉异常？

1. [异常] 在什么情况下我们需要自定义异常？应如何编码？

1. [异常] 什么是环境管理协议？

1. [异常] **如何使用With语法？**

1. [异常] 如何实现一个环境管理器？

1. [正则] **Python中使用正则表达式的语法是怎样的？**

1. [正则] **正则表达式中的符号有哪些？**

1. [正则] 什么是非贪心匹配？

1. [正则] 什么是标记匹配？

1. [正则] 如何获取匹配到的字符串？

1. [正则] 如何替换匹配到的字符串？

1. [正则] 如何使用Findall？

1. [正则] 如何按正则表达式切割字符串？

1. [正则] **编写正则表达式时有哪些注意事项？`r`, 如何化繁为简？**

1. [装饰] 什么是装饰器模式？

1. [装饰] **什么是Python中的装饰器语法？如何使用？**

1. [装饰] 装饰器语法有哪些语法变化？装饰器类，多重装饰，装饰器参数

1. [生成] **什么是迭代环境，迭代器和迭代协议？Python2和Python3有何区别？`next`和`__next__`**

1. [生成] **如何编写生成器函数和生成器表达式？**

1. [生成] **生成器函数的执行逻辑是怎样的？**

1. [生成] 什么是扩展生成器协议？

1. [生成] 什么是协程Co-Routine？有哪些应用场景？

1. [生成] 有哪些常见的协程类库？如何使用？

## 常见应用 

### Python的系统和进程管理中的应用
1. [Bash] Bash编程有哪些优秀的参考书和资料？

1. [Bash] **Bash变量的定义和使用方法是怎样的？如何在循环中定义变量？如何重新定义变量？**

1. [Bash] 单引号和双引号对Bash字符串操作有什么区别？

1. [Bash] **常见的Bash字符串操作有哪些？求长度，提取子串，查找子串位置**

1. [Bash] **Bash数组操作有哪些？赋值，求长度，引用数组，连接数组，遍历数组**

1. [Bash] **Bash分支结构的写法是怎样的？**

1. [Bash] **Bash循环的写法是怎样的？for/while**

1. [Bash] Bash中的单行注释和多行注释的写法分别是怎样的？

1. [Bash] Bash中文本处理是怎样的？grep, awk, sed, tr

1. [Bash] Bash中的管道处理是怎样的？xargs

1. [Bash] Bash中的数学运算是如何操作的？expr

1. [联合] Python如何调用Bash？os.system, subprocess

1. [联合] Bash如何调用Python？

1. [联合] os模块主要用于处理什么问题？常用方法有哪些？

1. [目录] **如何遍历一个目录？**

1. [目录] **如何创建和使用临时文件，临时目录？**

1. [目录] shutil模块有哪些常用方法？copy/copy2/copytree/rmtree/move

1. [系统] **psutil模块如何监控CPU/Memory/Network/Disk等资源？**

1. [网络] **IPy模块的使用范围和使用方法是怎样的？**

1. [网络] Python如何处理常见的网络协议？Telnet/FTP/Socket/Http/LDAP/SSH/SFTP/SMTP/POP3/IMAP

1. [网络] Twisted框架的底层实现是怎样的？

1. [网络] Twisted框架的基本使用方法是怎样的？在Windows上如何安装Python3-Twist框架？[知乎](https://www.zhihu.com/question/52281800), [Python Extension Packages for Windows](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)

1. [并行] **如何处理子进程和管道？subprocess**

1. [并行] **如何编写多线程应用？**

1. [并行] **线程join操作有什么作用？**

1. [并行] **什么是后台线程？Daemon**

1. [并行] **什么是线程竞争？**

1. [并行] **如何实现线程同步？锁、信号量**

1. [并行] 什么是全局解释器锁GIL？

1. [并行] 哪些Python内置对象是线程安全的？哪些不是？

1. [并行] 如何像管理线程一样管理进程？

1. [并行] **如何开启和使用进程池？**

1. [并行] **如何开启和使用线程池？**

1. [并行] **Async异步语法应如何使用？**

1. [并行] 异步的底层实现是怎样的？使用时有哪些陷阱？

### DevOps
1. [版本] 有哪些常见的版本控制工具？

1. [版本] 集中式和分布式版本控制有什么区别？

1. [版本] **如何使用Git进行版本控制？CLI & Tortoise**

1. [版本] 应如何理解Git中的rebase概念？ 

1. [测试] **如何编写基于XUnit的单元测试案例？**

1. [测试] **如何Mock一个需要的对象？`MagicMock` & `create_autospec`**

1. [测试] 有哪些常用的单元测试框架以及test runner框架？应如何选择？

1. [测试] Doctest的作用和用法？

1. [日志] **如何使用logging模块打日志？**

1. [日志] 输出日志有哪些注意事项？Async, Daemon, Format, Access/Error/Transaction, RequestID

1. [部署] **pip的常用命令有哪些？**

1. [部署] 如何为pip配置更快的源？Windows, Linux, Mac

1. [部署] 什么是anaconda？[Download](https://www.anaconda.com/download/)

1. [部署] **什么是virtualenv？如何使用？**

1. [自动] 有哪些常用的自动化管理框架？我们应如何选择？

1. [自动] Fabric的实现原理是什么？

1. [自动] Fabric的常用函数有哪些？

1. [自动] **Ansible框架的实现原理是什么？**

1. [自动] Ansible应如何安装？

1. [自动] **Ansible框架的部署架构是怎样的？**

1. [自动] 什么是YAML？

1. [自动] **如何理解和编写YAML描述文件？**

1. [自动] **什么是Ansible中的Inventory？**

1. [自动] Ansible中的常用模块有哪些？

1. [自动] **Ansible中的playbook是什么？**

1. [自动] **Ansible中的Role是什么？**

1. [自动] 什么是AWX？

1. [自动] AWX应如何安装和使用？

1. [自动] SaltStack框架的架构是怎样的？

1. [自动] SaltStack适用于什么场景（Ansible不适用）？

1. [容器] **什么是Docker？LXC，namespace，cgroup，CE/EE架构有何不同？**

1. [容器] Docker的使用场景和使用方法是怎样的？

1. [容器] **DockerFile应如何编写？**

1. [容器] **Docker-Compose应如何使用？**

1. [容器] Docker-Machine是什么？如何使用？

1. [容器] **Docker网络配置方法是怎样的？Linux和Windows环境有什么不同？**

1. [容器] **K8S是什么？应如何使用？**

### Web框架
1. [ORM] MySQL的安装和基本操作是怎样的？

1. [ORM] Sqlite3的原理和使用方法是怎样的？

1. [ORM] 使用什么工具查看和编辑Sqlite3数据库文件？[]

1. [ORM] 基本的数据库连接和处理流程是怎样的？

1. [ORM] 什么是ORM模型？

1. [ORM] **如何使用SqlAlchemy框架？Code First，表初始化，Migration，CRUD**

1. [架构] Web框架的架构和流程是怎样的？

1. [架构] HTML/CSS/JavaScript在前端显示中各自起到什么作用？

1. [架构] **什么是CGI/FastCGI/Module模式？**

1. [架构] **什么是WSGI接口？**

1. [MVC] **什么是MVC模型？**

1. [服务] 什么是WebService？

1. [服务] 什么是JSON？

1. [Flask] Python中常见的Web框架有哪些？各自有什么优缺点？各自有什么代表作？我们应如何选择合适的框架？

1. [Flask] Flask框架的架构和特点是怎样的？

1. [Flask] **Jinja2语法是怎样的？**

1. [Flask] **Flask和SqlAlchemy如何整合？**

1. [Flask] **如何使用Flask框架快速完成一个基本CRUD操作？**

1. [Flask] Flask项目中如何实现用户认证和权限管理？

1. [Flask] Flask项目中如何使用Session/Cookie？

1. [Flask] Flask项目中如何处理表单？

1. [Flask] **一个用于生产环境的“正经”的Flask框架的代码结构是怎样的？blueprint, restful api, configuration, deployment**

1. [Flask] Flask框架应如何部署？Python2和Python3有何不同？

1. [Django] **Django框架的特点和基本流程是怎样的？**

1. [Django] 应该如何选择Django版本？[参考](https://www.djangoproject.com/download/)

1. [Django] **Django框架中如何Startup，编写config文件和Router(urls.py)？**，[参考](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)，[Demo](https://github.com/wu-wenxiang/ZZLARGE-Training-Python-Django)

1. [Django] **Django框架中Views方法如何接收到uri参数？**

1. [Django] **Django框架中的ORM模型如何使用？**

1. [Django] **Django框架中Template的语法是怎样的？与Jinja2有什么区别？**

1. [Django] **Django框架中的表单处理是怎样的？**

1. [Django] **Django框架中的Session和Cookie处理是怎样的？**

1. [Django] **Django框架如何部署？**

1. [Django] 如何对Django框架进行性能监控和调优？

1. [微信] 订阅号和服务号有什么区别？各自的应用场景是什么？

1. [微信] 微信的身份认证机制是怎样的？
 
1. [微信] 微信订阅号的开发和调试步骤是怎样的？

1. [微信] 微信服务号的支付功能是怎样实现的？

1. [微信] 小程序的实现原理是什么？适用于什么场景？

1. [微信] Web站点如何使用微信扫码登录？

### 数据采集
1. [爬虫] 爬虫的基本原理是什么？

1. [爬虫] **urllib2模块的基本使用方法是什么？登录，SSL**

1. [爬虫] 如何使用bs4模块解析HTML数据？

1. [Scrapy] Scrapy框架的架构是怎样的？

1. [Scrapy] **Scrapy的基本使用方法是怎样的？**, [参考](https://docs.scrapy.org/en/latest/)

1. [Scrapy] 如何使用Scrapy框架做整站爬取？

### 数据挖掘
基本概念，常见类库，案例

1. [概念] 什么是结构化数据？

1. [概念] 什么是数据挖掘？

1. [概念] **数据挖掘的基本流程是怎样的？**

1. [概念] 有哪些数据挖掘相关的类库？

1. [概念] 什么是回归分析？适用于哪些场合？

1. [概念] 什么是决策树？适用于哪些场合？

1. [概念] 什么是神经网络算法？适用于哪些场合？

1. [概念] 什么是K-Means聚类算法？适用于哪些场合？

1. [概念] 什么是Apriori算法？适用于哪些场合？

1. [类库] **如何理解和使用Pandas中的DataFrame对象？**

1. [类库] **如何理解和使用Numpy模块中的ndarray对象？**

1. [类库] 如何使用Scipy解非线性方程组？

1. [类库] 如何使用Scipy做数值积分？

1. [类库] **如何使用Matplotlib绘制解析几何图形？**

1. [类库] **如何使用Scikit-Lean完成回归、分类、聚类运算？**

1. [案例] 什么是适用于消费类数据的RFM模型？

1. [案例] 数据分析的一般步骤是什么？数据探索，数据清洗，属性规约，数据变换

1. [案例] 如何完成航空公司客户价值分析？

1. [案例] 如何完成电商评论产品评论数据情感分析？

1. [案例] 如何完成财政收入影响因素分析？

1. [案例] 如何完成电商用户行为分析及服务推荐？

1. [案例] 如何完成电力窃漏电用户自动识别？

## 其它应用

### 云计算OpenStack

### PaSS云平台
1. [GAE] GAE的基本使用方法是怎样的？

1. [SAE] SAE的基本使用方法是怎样的？

### Office文档处理
1. [Word] 如何实现对Word文档的读、写操作？

1. [Excel] **如何实现对Excel文档的读、写操作？**

### Python-C
1. [CType] Python如何调用C类库？

1. [调用] C语言如何使用Python对象？

1. [实现] 如何实现一个基于C的Python模块？

### PVM内存分析
1. [PDB] Pdb的使用和局限性是怎样的？

1. [Dump] 如何收集Dump？

1. [Windbg] 如何使用Windbg分析PVM内存？

1. [GDB] 如何使用Windbg分析PVM内存？

### IoT
1. [树莓] **如何烧制树莓板？Win10/Raspbian**

1. [GPIO] **如何使用Python控制GPIO口**

1. [GPIO] 如何使用面包板搭建GPIO口的输入、输出电路？

1. [Azure IoT DevKit] 如何使用DevKit将收集到的温度/湿度信息上传到Azure云端，并通过PowerBI显示出来？[参考](https://github.com/wu-wenxiang/Training-Python/tree/master/Python-Common/IoT/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%81%9AIoT%E8%AE%BE%E5%A4%87)

### MineCraft
1. [基础] MineCraft基础和Hook原理是什么？

1. [绘制] 如何绘制三维图形？

1. [捕捉] 如何步骤游戏角色的位置？

1. [现实] 如何在游戏中控制GPIO口？

### GUI
1. [TK] TK的基本处理流程和布局方式是怎样的？
 

