## 数字

### 整除
- 要求输入一个秒数（整数），输出这些秒相当于多少分钟加多少秒，以及相当于多少分钟（带小数）。
		
		Please input seconds number: 72
		72 sec = 1.200000 min
		72 sec = 1 min + 12 sec

### 随机数
- 随机生成4个[1-10]之间的自然数并输出到屏幕，要求输入24点的算法，输出True/False

		Numbers are: 6, 1, 2, 6: 
		6*1*(6-2)
		Right!

### 小数精度+判断浮点数相等+随机数
- 随机生成两个10以内的实数（小数点后两位）并输出到屏幕，要求输入他们的和，输出True/False。

		Please input sum for 4.96 + 4.91 =
		9.87
		Right!

### 进制
- 玛雅人用二十进制计数，如果有个玛雅人跟你说“30”年后是世界末日，请问多少年后是世界末日？

		60
- 一些非洲的土著人只会用八进制计数，如果你想给他20瓶可乐换他9只羊，你该怎么告诉他？

		24 Coco Cola <=> 11 Sheep

## 字符串

### 子串
- 提示用户输入一个字符串，判断该字符串是否包含"apple"子字符串（忽略大小写，Apple, APPLE都算）。

		Please input a string:
		I like aPple
		'Apple' in 'I like aPple'
- 提示用户输入一个字符串，统计其中字母a的个数（不区分大小写，A也算），并输出第一个a在字符串中的位置。

		Please input a string:
		haha
		String 'haha' has 2 a(or A), first a(or A) in 1.

### 字符串处理
- 提示用户输入一个若干个单词，单词要用空白符隔开（两个单词之间可以有多个空白符），程序要将每个单词首字母大写，再用单个空白符连接所有的单词，并输出到屏幕。

		Please input a string:
		    I    like apple
		I Like Apple

- 提示用户输入一个字符串，去掉两头空格，逆序间隔1位输出。

		Please input a string:
		123456789
		97531

- 如何判断一个字符串是否回文字符串？

### 字符串替换
- 提示用户输入一个字符串，将其中所有的hello替换成HELLO，并将其中第一个world替换成WORLD。

		Please input a string:
		hello world hello world hello world
		HELLO WORLD HELLO world HELLO world

## 序列

### 列表解析
- 输入若干(>3)个评分，去掉一个最高分，一个最低分，求平均分，保留2位小数。

		Please input some integer numbers:
		9 7 5 0 100
		The average is: 7.00.
- 输入若干(>1)个整数，生成一个长度为10000的随机数列表，列表中的每个数字都是随机从你输入的几个数字中选取的，统计列表中各个数字出现了多少次。

		Please input some integer numbers:
		1 3 7
		1 => 3333
		3 => 3357
		7 => 3310
- 输入一个整数，输出比它小的平方数。

		Please input an integer:
		19
		Numbers: 1 4 9 16
- 输入一个年份，输出其属相，不考虑公历年和农历年之间的差月，比如1983年全年都认为是属猪。

		Please input an integer:
		2012
		ShengXiao: 2012 => Long
- 输出一个字符串，将其加密(每个字母的ascii加一)输出，再解密输出。

		Please input a string:
		I love you
		------------------------------
		J!mpwf!zpv
		I love you

- 输入一个整数，输出比它小的能被三整除的自然数。

		Please input a integer:
		50
		3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48

## 散列

### 集合问题
- 让用户输入A、B两个整数数列，统计并排序输出A数列中独有的整数，B中独有的整数，以及A、B公有的整数。

		Please input int list A: 1 3 5 7 9
		Please input int list B: 5 6 7
		Only in A: [1, 3, 9]
		Only in B: [6]
		Both in A & B: [5, 7]

### 唱票算法
- 让用户输入一行字符串，统计并输出其中每个字符出现的次数。

		Please input a Str:
		abcdcdabcd
		The stat char list:
		a => 2 
		c => 3
		b => 2
		d => 3
- 输入一个句子，按首字母统计句中的单词(限定每个单词都只能由字母组成)，输出统计结果。

		Please input a string:
		it is my book.
		The stat char list:
		i => ['it', 'is']
		m => ['my']
- Tip_26. 输入一行字符串，按字母顺序输出其中每个字符出现的位置。

		Please input a string:
		abacd
		a => [0, 2]
		b => [1]
		c => [3]
		d => [4]

## 循环和分支

### 循环
- 根据用户的输入（直角边长），用`*`号打印直角等腰三角形

		Please input length:
		5
		*
		**
		***
		****
		*****
- 根据用户的输入（腰长），打印等腰三角形。

		Please input length:
		5
		    *
		   ***
		  *****
		 *******
		*********
- 打印九九乘法表。

		1 * 1 = 1
		2 * 1 = 2       2 * 2 = 4
		3 * 1 = 3       3 * 2 = 6       3 * 3 = 9
		4 * 1 = 4       4 * 2 = 8       4 * 3 = 12      4 * 4 = 16
		5 * 1 = 5       5 * 2 = 10      5 * 3 = 15      5 * 4 = 20      5 * 5 = 25
		……
- 打印杨辉三角

	        1
	       1 1
	      1 2 1
	     1 3 3 1
	    1 4 6 4 1
- 编写猜数字游戏

		please input number:
		3
		too small
		please input number:
		67
		good ,right
		count number times = 2

## 输入输出

### 命令行参数
- 计算命令行参数的和，保留两位小数。
	
		python cmdLineSum.py 4 5 6
		The sum was 15.00 !

- 使用命令行输入职工信息。
	1. 职工信息包括姓名，性别，婚姻情况，年龄，薪水，职位。
	2. 职工信息中的“职位”字段的缺省值为“staff”。
	3. 年龄字段必须是整数，薪水字段必须是浮点数，性别只能是N个选项中的一个，否则报错。
	4. 婚姻情况只有两种，已婚和未婚。

			python test.py -n John -s male -a 40 -p 50000 -m -r manager
			Worker Information:
			name =>  John
			sex =>  male
			age =>  40
			pay =>  50000.0
			marriageFlag =>  True
			role =>  manager

	- Code:

			from optparse import OptionParser
			
			if __name__ == '__main__':
			    parser = OptionParser()
			    parser.add_option("-n", "--name", dest="name", help="name string",
			                      metavar="NAME_STRING")
			    parser.add_option("-s", "--sex", dest="sex", type="choice",
			                      choices=['male', 'female'], help="sex string",
			                      metavar="SEX_STRING")
			    parser.add_option("-a", "--age", dest="age", type="int", help="age int",
			                      metavar="AGE_INT")
			    parser.add_option("-p", "--pay", dest="pay", type="float",
			                      help="pay float", metavar="PAY_FLOAT")
			    parser.add_option("-m", "--marriage", dest="marriageFlag", action='store_true',
			                      help="marriage flag", metavar="MARRIAGE_FLAG")
			    parser.add_option("-r", "--role", dest="role", default="staff",
			                      help="role string", metavar="ROLE STRING")
			    (options, args) = parser.parse_args()
			    
			    #print options
			    
			    print "Worker Information:"
			    print "name => ", options.name
			    print "sex => ", options.sex
			    print "age => ", options.age
			    print "pay => ", options.pay
			    print "marriageFlag => ", options.marriageFlag
			    print "role => ", options.role

### 文件 
- 输出被指定的文件中带有指定字符串的行。
	- a.txt文件的内容如下：

			test 1 apples
			apple store
			pear banana
	- Run: 

			python filter.py a.txt apple
			test 1 apples
			apple store

		
- 统计指定的文件中单词(单词只包含字母，在行内由空白隔开)的个数
	- a.txt文件中内容如下：

			test 1 apples
			apple store
			pear banana

	- Run: 
		
			python calNum.py a.txt
			6

## 函数

### 高阶函数
- 实现一个函数sumAny，能满足如下运算：(参数个数是两个或多个，参数彼此之间能做+运算)
	- 代码
	
			print sumAny(1, 2)
			print sumAny(1.2, 2.3, 3.4)
			print sumAny("hello, ", "world!")
			print sumAny(range(5), range(3))
	- 输出：

			3
			6.9
			hello, world!
			[0, 1, 2, 3, 4, 0, 1, 2]

- 打印指定文件中最长的一行，如果有多行并列最长，只打印最靠前的最长的一行。
	- a.txt文件中内容如下：

			test 1 apples
			apple store
			pear banana

	- Run: 

			python printLong.py a.txt
			test 1 apples

- 打印输出符合如下条件之一的100以内的自然数：	
	- 条件
		1. 能被30整除
		2. 个位+十位=10
		3. 个位-十位=5
	- Run:
	
			[0, 5, 16, 19, 27, 28, 30, 37, 38, 46, 49, 55, 60, 64, 73, 82, 90, 91]
- 实现一个函数，将字符串序列按长度排序。
	- 原字符串
	
			['smiles', 'bool', 'objective', 'hello'] 
	- Run:

			['bool', 'hello', 'smiles', 'objective']

### 递归函数
- 汉诺塔问题
	- 问题
		- 汉诺塔（又称河内塔）问题是印度的一个古老的传说。传说中，开天辟地的神勃拉玛在一个庙里留下了三根金刚石的棒，第一根上面套着64个圆形的金片，最大的一个在底下，其余一个比一个小，依次叠上去，寺院的僧侣依照一个古老的预言，不知疲倦地把它们一个个地从这根棒搬到另一根棒上，规定可利用中间的一根棒作为帮助，但每次只能搬一个，而且大的不能放在小的上面，预言说，当这些金片移动完毕后，世界就会灭亡。
	- 解法

			Hanoi(3, 'A', 'C', 'B')
			# 3阶汉诺塔，从A柱移动到C柱，B柱作为辅助
			1:      A -> C
			2:      A -> B
			3:      C -> B
			4:      A -> C
			5:      B -> A
			6:      B -> C
			7:      A -> C

## 模块和包

### 模块
- 打印输出math模块的所有方法属性和字段属性，打印输出其中fsum函数的用法
	- 运行

			['pow', 'fsum', 'cosh', 'ldexp', 'hypot', 'acosh', 'tan', 'asin', 'isnan', 'log', 'fabs', 'floor', 'atanh', 'modf', 'sqrt', 'frexp', 'degrees', 'lgamma', 'log10', 'asinh', 'fmod', 'atan', 'factorial', 'copysign', 'expm1', 'ceil', 'isinf', 'sinh', 'trunc', 'cos', 'tanh', 'radians', 'sin', 'atan2', 'erf', 'erfc', 'exp', 'acos', 'log1p', 'gamma']
			
			['__package__', '__doc__', '__file__', '__name__', 'pi', 'e']

			fsum(iterable)
			
			Return an accurate floating point sum of values in the iterable.
			Assumes IEEE-754 floating point arithmetic.
- 输入一个标准库的模块名称，输出其属性
	- 运行
	
			Please input module name:math
			{'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'modf': <built-in function modf>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'degrees': <built-in function degrees>, 'lgamma': <built-in function lgamma>, 'log10': <built-in function log10>, '__doc__': 'This module is always available.  It provides access to the\nmathematical functions defined by the C standard.', 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, 'factorial': <built-in function factorial>, '__file__': '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so', 'copysign': <built-in function copysign>, 'expm1': <built-in function expm1>, 'ceil': <built-in function ceil>, 'isinf': <built-in function isinf>, 'sinh': <built-in function sinh>, '__name__': 'math', 'trunc': <built-in function trunc>, 'cos': <built-in function cos>, 'pi': 3.141592653589793, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sin': <built-in function sin>, 'atan2': <built-in function atan2>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}

## 类与面向对象

### 组合与继承
- 编写一个类Name，能被如下代码调用：
	- 调用代码

			aName = Name("John Green")
			print aName.getLastName()
			print len(aName)
			print aName.split()
			print aName.lower()
	- 运行结果
		
			Green
			10
			['John', 'Green']
			john green
- 实现一个缓存类
	- 调用代码

			aBuff = Buff(3)
			aBuff.add('test1')
			aBuff.add('test2')
			print('buffer length = %d' % len(aBuff))
			print(aBuff)
			
			aBuff.add('test3')
			aBuff.add(42)
			print('buffer length = %d' % len(aBuff))
			print(aBuff)
	- 运行结果

			buffer length = 2
			['test1', 'test2']
			buffer length = 3
			['test2', 'test3', 42]
- 遍历一个大文件，输出其中最长的5行

## 异常处理
- 让用户输入两个实数，输出他们的和。如果用户的输入有误，给出提示
	- Run:

			Please input A: 4
			Please input B: 56
			Sum = 60.0
			
			Please input A: dd
			Please input B: 3
			Value Error!
			could not convert string to float: dd

## 正则表达式
- 统计一个文件所有包含数字的行。
	- 测试文件如下：

			apple banana 2
			3hello 
			good orange
	- Run:

			apple banana 2
			3hello 
- 找出一个文件中所有整数，打印输出它们的和。
	- 测试文件如下：

			apple banana 23
			33hello 
			good 45 orange

	- Run:

			[11, 22, 3, 4]
			40

## 装饰器
- 编写装饰器makebold和makeitalic
	- 客户端代码：

			@makebold
			@makeitalic
			def hello():
			    return "hello world"
			
			@makeitalic
			@makebold
			def hello2():
			    return "hello world"
			
			print hello()
			print hello2()
			
	- Run:

			<b><i>hello world</i></b>
			<i><b>hello world</b></i>

## 生成器
- 编写一个函数，产生无限个数的斐波那契数列，实现如下调用
	- 客户端代码：

			for i in Fib():
				if i < 1000:
					print i
				break
	- 输出<1000的斐波那契数列	
	- 思考如何用上述Fib()取得斐波那契数列前50个值

 