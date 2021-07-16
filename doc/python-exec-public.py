'''
Python训练题：

目录：
0101 HelloWorld
0201 Number
0202 String
0203 Tuple/List
0204 Set/Dict
0205 CLI
0206 File
0301 If-Else/While/For
0302 Function
0401 Module/Package
0402 Class
0501 Exception
0502 Regex
0503 Decorator
0504 Generator
0601 Dir&File
0602 Internet Client
0603 Parallel
0701 Scrapy
0801 GUI-TK
0901 Distribution-Env
1001 UnitTest
1002 DB
1003 WSGI/Flask
1004 Django
1101 Automation
1102 DevOps
1201 DataAnalysis
1202 MachineLearning
1301 BlockChain
1401 OpenStack
1501 MineCraft
1601 IoT
1701 Crack-Debug
'''

# -----------------------------------------------
'''
Tip_010101 要求用户输入一个数字，判断这个数字是否大于42。

Run:
Input: 45
> 42

Code:
'''
'''
Check if input-number > 42
'''
aStr = input("Input: ")
# print(aStr)
aInt = int(aStr)
if aInt > 42:
    print("> 42")
else:
    print("<= 42")

'''
Tip_010102 要求用户输入两个整数，计算输出两者的和。

Run:
Int A = 32
Int B = 11
32 + 11 = 43

Code:
'''
# -*- coding: utf-8 -*-

aStr = input('Int A = ')
bStr = input('Int B = ')
aInt = int(aStr)
bInt = int(bStr)
print("%s + %s = %s" % (aInt, bInt, aInt+bInt))

'''
Tip_020101. 要求输入一个秒数（整数），输出这些秒相当于多少分钟加多少秒，以及相当于多少分钟（带小数）。

Run:
Please input seconds number: 72
72 sec = 1.200000 min
72 sec = 1 min + 12 sec

Code:
'''
secStr = input("Please input seconds number: ")
sec = int(secStr)
minFloat = float(sec) / 60
minInt, secMod = divmod(sec, 60)
secMod = sec % 60
print("%d sec = %f min" % (sec, minFloat))
print("%d sec = %d min + %d sec" % (sec, minInt, secMod))

'''
Tip_020102. 要求输入一个实数，输出它的平方和开方数，后者保留两位小数。

Run:
Please input float A: 2
2.000000 ** 2 = 4.000000
2.000000 ** 1/2 = 1.414214
2.000000 ** 1/2 = 1.410000
2 ** 1/2 = 1.41

Code:
'''
aFloatStr = input("Please input float A: ")
aFloat = float(aFloatStr)
print("%f ** 2 = %f" % (aFloat, aFloat ** 2))
print("%f ** 1/2 = %f" % (aFloat, aFloat ** 0.5))
print("%f ** 1/2 = %f" % (aFloat, round(aFloat ** 0.5, 2)))
print("%s ** 1/2 = %.2f" % (aFloatStr, pow(aFloat, 0.5)))

'''
Tip_020103 随机生成两个10以内的实数（小数点后两位）并输出到屏幕，要求输入他们的和，输出True/False。

Run:
Please input sum for 4.96 + 4.91 =
9.87
Right!

Code:
'''
from random import random

MIN_DELTA = 10 ** -10

aFloat = round(random() * 10, 2)
bFloat = round(random() * 10, 2)
sumStr = input("Please input sum for %.2f + %.2f =\n" % (aFloat, bFloat))
if abs(float(sumStr) - (aFloat+bFloat)) < MIN_DELTA:
    print("Right!")
else:
    print("Wrong!")

''' 
Tip_020104. 随机生成4个[1-10]之间的自然数并输出到屏幕，要求输入24点的算法，输出True/False。
 
Run:
Numbers are: 6, 1, 2, 6: 
6*1*(6-2)
Right!
 
Code:
'''
from random import choice, randint

aInt = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bInt = choice(range(1, 11))
cInt = randint(1, 10)
dInt = choice(range(1, 11))

aStr = input("Numbers are: %d, %d, %d, %d: \n" % (aInt, bInt, cInt, dInt))
if eval(aStr) == 24:
    print("Right!")
else:
    print("Wrong!")

''' 
Tip_020105. 提示用户输入一个整数（X元人民币），输出这笔钱等于多少张50元，10元，5元，1元纸币（优先用大额纸币）。

Run:
Please input X Yuan:
72
72 Yuan = 1 Fifty, 2 Ten, 0 Five, 2 One

Code:
'''
aNumStr = input("Please input X Yuan:\n")
aNum = int(aNumStr)

tmpNum = aNum
FiftyNum, tmpNum = divmod(tmpNum, 50)
TenNum = tmpNum / 10
tmpNum = tmpNum % 10
FiveNum, OneNum = divmod(tmpNum, 5)

print("%d Yuan = %d Fifty, %d Ten, %d Five, %d One" % (aNum, FiftyNum, TenNum, FiveNum, OneNum))

'''
Tip_020106. 一英寸=2.54厘米。提示用户输入一个英寸数（浮点数），将其换算成浮点数输出，计算时保留两位小数，输出时保留到小数点后四位。

Run:
Please input Inch:
2.698
2.698000 inch = 6.8500 celi

Code:
'''
INCH_CELI = 2.54

aNumStr = input("Please input Inch:\n")
inchNum = float(aNumStr)

celiNum = round(inchNum * INCH_CELI, 2)

print("%f inch = %.4f celi" % (inchNum, celiNum))

'''
Tip_020107. 玛雅人用二十进制计数，如果有个玛雅人跟你说“30”年后是世界末日，请问多少年后是世界末日？

Code:
'''
print(int("30", 20))

'''
Tip_020108. 一些非洲的土著人只会用八进制计数，如果你想给他20瓶可乐换他9只羊，你该怎么告诉他？

Code:
'''
print("%o Coco Cola <=> %o Sheep" % (20, 9))

'''
Tip_020201. 提示用户输入一个字符串，判断该字符串是否包含"apple"子字符串（忽略大小写，Apple, APPLE都算）。

Run:
Please input a string:
I like aPple
'Apple' in 'I like aPple'

Code:
'''
aStr = input("Please input a string:\n")

aStrUpper = aStr.upper()
if "APPLE" in aStrUpper:
    print("'Apple' in '%s'" % aStr)
else:
    print("'Apple' not in '%s'" % aStr)

'''
Tip_020202. 提示用户输入一个若干个单词，单词要用空白符隔开（两个单词之间可以有多个空白符），程序要将每个单词首字母大写，再用单个空白符连接所有的单词，并输出到屏幕。

Run:
Please input a string:
    I    like apple
I Like Apple

Code:
'''
aStr = input("Please input a string:\n")

aStrTitle = aStr.title()
aList = aStrTitle.split()
aStrNew = " ".join(aList)

print(aStrNew)

''' 
Tip_020203. 提示用户输入一个字符串，判断该字符串是否回文（回文是指正读反读都一样，注意忽略用户输入的字符串两头的空白），并统计字符串长度。
 
Run:
Please input a string:
   bob
len = 3
'bob' is a huiwen string
 
Code:
'''
aStr = input("Please input a string:\n")

aStr = aStr.strip()
print("len = %d" % len(aStr))
if aStr == aStr[::-1]:
    print("'%s' is a huiwen string" % aStr)
else:
    print("'%s' is not a huiwen string" % aStr)

'''
Tip_020204. 提示用户输入一个字符串，将其中所有的hello替换成HELLO，并将其中第一个world替换成WORLD。

Run:
Please input a string:
hello world hello world hello world
HELLO WORLD HELLO world HELLO world

Code:
'''
aStr = input("Please input a string:\n")

aStr = aStr.replace("hello", "HELLO")
aStr = aStr.replace("world", "WORLD", 1)

print(aStr)

'''
Tip_020205. 提示用户输入一个字符串，去掉两头空格，逆序间隔1位输出。

Run:
Please input a string:
123456789
97531

Code:
'''
aStr = input("Please input a string:\n")
aStr = aStr.strip()
print(aStr[::-2])

'''
Tip_020206. 提示用户输入一个字符串，统计其中字母a的个数（不区分大小写，A也算），并输出第一个a在字符串中的位置。

Run:
Please input a string:
haha
String 'haha' has 2 a(or A), first a(or A) in 1.

Code:
'''
aStr = input("Please input a string:\n")

aCount = aStr.lower().count('a')
aIndex = aStr.lower().find('a')

print("String '%s' has %d a(or A), first a(or A) in %d." % (aStr, aCount, aIndex))

'''
Tip_020301. 输入若干(>3)个评分，去掉一个最高分，一个最低分，求平均分，保留2位小数。

Run:
Please input some integer numbers:
9 7 5 0 100
The average is: 7.00.

Code:
'''
aStr = input("Please input some integer numbers:\n")
aNumList = [float(item) for item in aStr.split()]
if len(aNumList) < 3:
    print("Please input at least 3 integer numbers!")
else:
    aNumList.sort()
    bNumList = aNumList[1:-1]
    avg = sum(bNumList) / len(bNumList)
    print("The average is: %0.2f." % avg)

'''
Tip_020302. 输入若干(>1)个整数，生成一个长度为10000的随机数列表，列表中的每个数字都是随机从你输入的几个数字中选取的，统计列表中各个数字出现了多少次。

Run:
Please input some integer numbers:
1 3 7
1 => 3333
3 => 3357
7 => 3310
# 可以看到1，3，7三个数字出现的次数差不多，列表越大，其概率越接近频率。
Please input some integer numbers:
1 1 4
1 => 6617
1 => 6617
4 => 3383
# 可以看到1出现的次数大约是4的两倍，美中不足1的统计出现了两次，尝试把重复的行去掉？
# 后面学习散列（集合，字典）的时候，会用更简单的方法去掉重复的行。

Code:
'''
from random import choice
aStr = input("Please input some integer numbers:\n")
aList = aStr.split()
aNumList = [int(item) for item in aList]
if len(aNumList) < 1:
    print("Please input at least 1 integer numbers!")
else:
    bNumList = [choice(aNumList) for i in range(10000)]
    cNumList = [(i, bNumList.count(i)) for i in aNumList]
    for x,y in cNumList:
        print("%d => %d" % (x, y))

'''
Tip_020303. 输入5个字符串，去掉字符串两端的空格，按字母顺序逆序输出其中长度大于3的字符串。(按长度排序输出所有字符串，这个在学完函数之后会容易实现)

Run:
Please input string 0:	haha
Please input string 1:	xi
Please input string 2:	hello
Please input string 3:	world
Please input string 4:	eee
--------------------
world
hello
haha

Code:
'''
aList = []
for i in range(5):
    aStr = input("Please input string %d:\t" % i)
    aList.append(aStr.strip())

bList = [item for item in aList if len(item) > 3]
bList.sort(reverse=True)
print("-" * 20)
for item in bList:
    print(item)

'''
Tip_020304. 输入一个整数，输出比它小的平方数。

Run:
Please input an integer:
19
Numbers: 1 4 9 16

Code:
'''
from math import ceil

aNum = int(input("Please input an integer:\n"))
aList = [str(i**2) for i in range(1, int(ceil(aNum ** 0.5)))]
print("Numbers: %s" % " ".join(aList))

'''
Tip_020305. 输入一个年份，输出其属相，不考虑公历年和农历年之间的差月，比如1983年全年都认为是属猪。

Run:
Please input an integer:
2012
ShengXiao: 2012 => Long

Code:
'''
SX_LIST = "Shu Niu Hu Tu Long She Ma Yang Hou Ji Gou Zhu".split()

aNum = int(input("Please input an integer:\n"))
index = (aNum - 1984) % 12
shengXiao = SX_LIST[index]

print("ShengXiao: %d => %s" % (aNum, shengXiao))

'''
Tip_020306. 输出一个字符串，将其加密(每个字母的ascii加一)输出，再解密输出。

Run:
Please input a string:
I love you
------------------------------
J!mpwf!zpv
I love you

Code:
'''
aStr = input("Please input a string:\n")

print("-" * 30)
aList = [chr(ord(char)+1) for char in aStr]
print("".join(aList))
bList = [chr(ord(char)-1) for char in aList]
print("".join(bList))

'''
Tip_020307. 输入一个整数，输出比它小的能被三整除的自然数。

Run:
Please input a integer:
50
3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48

Code:
'''
aInt = int(input("Please input a integer:\n"))
aList = [str(item) for item in range(3, aInt, 3)]
#aList = [str(item) for item in range(1, aInt) if item % 3 == 0]
print(" ".join(aList))

'''
Tip_020401. 让用户输入一行字符串，统计并输出其中每个字符出现的次数。
Run:
Please input a Str:
abcdcdabcd
The stat char list:
a => 2 
c => 3
b => 2
d => 3

Code:
'''
aStr = input("Please input a Str:\n")

aDict = {chr:aStr.count(chr) for chr in set(aStr)}

# aDict = {}
# for i in aStr:
#     aDict[i] = aDict.get(i, 0) + 1
#     # aDict.setdefaut(i, 0)
#     # aDict[i] += 1
# 	
# from collections import Counter
# aDict = Counter(aStr)

print("The stat char list:")
for tmpKey, tmpValue in aDict.items():
    print("%s => %d" % (tmpKey, tmpValue))

'''
Tip_020402. 让用户输入A、B两个整数数列，统计并排序输出A数列中独有的整数，B中独有的整数，以及A、B公有的整数。
Run:
Please input int list A: 1 3 5 7 9
Please input int list B: 5 6 7
Only in A: [1, 3, 9]
Only in B: [6]
Both in A & B: [5, 7]

Code:
'''
aNumStr = input("Please input int list A: ")
bNumStr = input("Please input int list B: ")

aNumSet = set([int(item) for item in aNumStr.split()])
bNumSet = set([int(item) for item in bNumStr.split()])

print("Only in A: %s" % sorted(aNumSet - bNumSet))
print("Only in B: %s" % sorted(bNumSet - aNumSet))
print("Both in A & B: %s" % sorted(aNumSet & bNumSet))

'''
Tip_020403. 输入一个句子，按首字母统计句中的单词(限定每个单词都只能由字母组成)，输出统计结果。
Run:
Please input a string:
it is my book.
The stat char list:
i => ['it', 'is']
m => ['my']

Code:
'''
aStr = input("Please input a string:\n")

wordList = [word for word in aStr.split() if word.isalpha()]
aDict = {}

for word in wordList:
    firstChar = word[0]
    aDict.setdefault(firstChar, [])
    aDict[firstChar].append(word)
    
print("The stat char list:")
for tmpKey, tmpValue in aDict.items():
    print("%s => %s" % (tmpKey, tmpValue))

'''
Tip_020404. 输入一行字符串，按字母顺序输出其中每个字符出现的位置。
Run:
Please input a string:
abacd
a => [0, 2]
b => [1]
c => [3]
d => [4]

Code:
'''
aStr = input("Please input a string:\n")

aDict = {}
for i, char in enumerate(aStr):
    aDict[char] = aDict.get(char, [])
    aDict[char].append(i)

for char in sorted(aDict):
    print(char, "=>", aDict[char])

'''
Tip_020405 字典格式化有什么好处？
    1. 避免顺序问题
    2. 避免冗余输入

Tip_020501. 计算命令行参数的和，保留两位小数。
Run: python cmdLineSum.py 4 5 6
The sum was 15.00 !

Code:
'''
import sys
floatList = [float(item) for item in sys.argv[1:]]
print("The sum was %.2f !" % sum(floatList))

'''
Tip_020502. 使用命令行输入职工信息。
1. 职工信息包括姓名，性别，婚姻情况，年龄，薪水，职位。
2. 职工信息中的“职位”字段的缺省值为“staff”。
3. 年龄字段必须是整数，薪水字段必须是浮点数，性别只能是N个选项中的一个，否则报错。
4. 婚姻情况只有两种，已婚和未婚。

Run: python test.py -n John -s male -a 40 -p 50000 -m -r manager
Worker Information:
name =>  John
sex =>  male
age =>  40
pay =>  50000.0
marriageFlag =>  True
role =>  manager

Code:
'''
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
    
    #print(options)
    
    print("Worker Information:")
    print("name => ", options.name)
    print("sex => ", options.sex)
    print("age => ", options.age)
    print("pay => ", options.pay)
    print("marriageFlag => ", options.marriageFlag)
    print("role => ", options.role)

'''
Tip_020601 输出被指定的文件中带有指定字符串的行。
a.txt文件的内容如下：
test 1 apples
apple store
pear banana

Run: python filter.py a.txt apple
test 1 apples
apple store

Code:
'''
import sys
fileName = sys.argv[1]
subStr = sys.argv[2]

for line in open(fileName):
    if subStr in line:
        print(line, end='')

'''        
Tip_020602 统计指定的文件中单词的个数，并追加写到文件末尾。
a.txt文件中内容如下：
test 1 apples
apple store
pear banana

Run: python calNum.py a.txt

Code:
'''
import sys
fileName = sys.argv[1]

wordCount = 0
for line in open(fileName):
    wordCount += len(line.split())
open(fileName, 'a').write("\n%d" % wordCount)

''' 
Tip_020603 打印指定文件中的内容，在打印时将A字符串替换为B字符串(原文件中的内容则不改变)
a.txt文件中内容如下：
test 1 apples
apple store
pear banana
 
Run: python replace.py a.txt apple other
test 1 others
other store
pear banana
 
Code:
'''
import sys
fileName = sys.argv[1]
subStr = sys.argv[2]
repStr = sys.argv[3]

for line in open(fileName):
    print(line.replace(subStr, repStr), end='')

''' 
Tip_020604 将字典序列化到文件，再从文件读出
    略
'''

'''
Tip_030101. 根据用户的输入（直角边长），用*号打印直角等腰三角形
Run:
Please input length:
5
*
**
***
****
*****

Code:
'''
aNum = int(input("Please input length:\n"))

for i in range(1, aNum + 1):
    print("*" * i)

'''
Tip_030102. 根据用户的输入（腰长），打印等腰三角形。
Run:
Please input length:
5
    *
   ***
  *****
 *******
*********

Code:
'''
aNum = int(input("Please input length:\n"))

for i in range(1, aNum + 1):
    print(" " * (aNum - i) + "*" * (2*i-1))

'''
Tip_030103. 打印九九乘法表。
Run:
1 * 1 = 1
2 * 1 = 2       2 * 2 = 4
3 * 1 = 3       3 * 2 = 6       3 * 3 = 9
4 * 1 = 4       4 * 2 = 8       4 * 3 = 12      4 * 4 = 16
5 * 1 = 5       5 * 2 = 10      5 * 3 = 15      5 * 4 = 20      5 * 5 = 25
……

Code:
'''
import sys

for i in range(1, 10):
    for j in range(1, i+1):
        k = "%d * %d = %d\t" % (i, j, i*j)
        print(k, end='')
        # sys.stdout.write(k)
    print()

for i in range(1, 10):
	aList = []
	for j in range(1, i+1):
		aList.append("%d * %d = %d" % (i, j, i*j))
	print("\t".join(aList))

'''
Tip_030104. 编写猜数字游戏
Run:
please input number:
3
too small
please input number:
67
good ,right
count number times = 2

Code:
'''
from random import randint

GUESS_MAX = 5

c = randint(1, 100)
#print(c)

count = 0
while(count < GUESS_MAX):
    a = input("please input number:\n")
    a = int(a)

    count = count + 1 
    if a > c:
        print("too large")
    elif a < c:
        print("too small")
    else:
        print("good ,right")
        print("count number times = %d" % count)
        break  
else:
    print("answer = %d" % c)

'''
Tip_030201 实现一个函数sumAny，能满足如下运算：(参数个数是两个或多个，参数彼此之间能做+运算)
print(sumAny(1, 2))
print(sumAny(1.2, 2.3, 3.4))
print(sumAny("hello, ", "world!"))
print(sumAny([0,1,2,3,4], [0,1,2])

输出：
3
6.9
hello, world!
[0, 1, 2, 3, 4, 0, 1, 2]

Code:
'''
from functools import reduce

def sumAny(*arg):
    return reduce(lambda x,y:x+y, arg)

print(sumAny(1, 2))
print(sumAny(1.2, 2.3, 3.4))
print(sumAny("hello, ", "world!"))
print(sumAny([0,1,2,3,4], [0,1,2]))

'''
Tip_030202 打印指定文件中最长的一行，如果有多行并列最长，只打印最靠前的最长的一行。
a.txt文件中内容如下：
test 1 apples
apple store
pear banana

Run: python printLong.py a.txt
test 1 apples

Code:
'''

import sys
from functools import reduce

fileName = sys.argv[1]
print(reduce(lambda x,y:x if len(x)>len(y) else y, open(fileName)))

''' 
Tip_030203 多维列表求和
    略
'''

'''
Tip_030204 遍历打印自然数1-30，如果遇到能被2整除的数只打印duck代替，如果遇到能被3整除的数只打印goose代替，如果遇到既能被2又能被3整除的数只打印pig代替。
	略
'''

'''
Tip_030205 打印输出符合如下条件之一的100以内的自然数：
1. 能被30整除
2. 个位+十位=10
3. 个位-十位=5

Run:
[0, 5, 16, 19, 27, 28, 30, 37, 38, 46, 49, 55, 60, 64, 73, 82, 90, 91]

Code:
'''
funList = [lambda x: x%30==0,
           lambda x: x%10+x/10==10,
           lambda x: x%10-x/10==5]

def testFun(i):
    return any(fun(i) for fun in funList)

print(filter(testFun, range(100)))

'''
Tip_030206 实现一个函数，将字符串序列按长度排序。
Run:
['bool', 'hello', 'smiles', 'objective']

Code:
'''
def sortStrbyLen(x, y):
    return cmp(len(x),len(y))

testStrList = ["hello", "smiles", "bool", "objective"]

print(sorted(testStrList, cmp=sortStrbyLen))

'''
Tip_030207 打印杨辉三角
Run:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
	
Code:
'''
N = 5

def nextLine(line):
    return [1]+map(lambda x,y:x+y, line[:-1], line[1:])+[1]

def printLine(level, index, numList):
    strList = [str(i) for i in numList]
    print(" "*(level-index)  + " ".join(strList))

yhList = [[1], [1,1]]
for i in range(2, N):
    yhList.append(nextLine(yhList[i-1]))

for i in range(N):
    printLine(N, i, yhList[i])

'''
Tip_030208 汉诺塔问题
	略
'''
    
''' 
Tip_040101 打印输出math模块的所有方法属性和字段属性，打印输出其中fsum函数的用法
 
Run:
 
['pow', 'fsum', 'cosh', 'ldexp', 'hypot', 'acosh', 'tan', 'asin', 'isnan', 'log', 'fabs', 'floor', 'atanh', 'modf', 'sqrt', 'frexp', 'degrees', 'lgamma', 'log10', 'asinh', 'fmod', 'atan', 'factorial', 'copysign', 'expm1', 'ceil', 'isinf', 'sinh', 'trunc', 'cos', 'tanh', 'radians', 'sin', 'atan2', 'erf', 'erfc', 'exp', 'acos', 'log1p', 'gamma']
['__package__', '__doc__', '__file__', '__name__', 'pi', 'e']
 
fsum(iterable)
 
Return an accurate floating point sum of values in the iterable.
Assumes IEEE-754 floating point arithmetic.
 
Code:
'''
import math

funList = [attr for attr,value in math.__dict__.items() if callable(value)]
fieldList = [attr for attr,value in math.__dict__.items() if not callable(value)]

print(funList)
print(fieldList)

print(math.fsum.__doc__)

'''
Tip_040102 编写一个模块，使得以下脚本代码运行之后，得到如下输出：

脚本代码：
import aModule
help(aModule)
aModule.aFun()

Run:

Import module: aModule
Help on module aModule:

NAME
    aModule - Title example

FILE
    /Users/wuwenxiang/Documents/workspace/test/aModule.py

DESCRIPTION
    Description example

FUNCTIONS
    aFun()

aFun

Code: 
'''
'''
Title example

Description example
'''

print("Import module: " + __name__)

def aFun():
    print("aFun")

'''
Tip_040103 编写一个包，使得一下脚本代码运行之后，得到输出如下：

脚本代码

import aPkg
help(aPkg)
print(aPkg.math.pi)

Run:

Help on package aPkg:

NAME
    aPkg - Package Title

FILE
    /Users/wuwenxiang/Documents/workspace/test/aPkg/__init__.py

DESCRIPTION
    Package Description

PACKAGE CONTENTS
    aModule

3.14159265359

Code:
'''
'''
Package Title

Package Description
'''
import math

'''
Tip_040104 输入一个标准库的名字，打印它的属性

Run:

Please input module name:math
{'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'modf': <built-in function modf>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'degrees': <built-in function degrees>, 'lgamma': <built-in function lgamma>, 'log10': <built-in function log10>, '__doc__': 'This module is always available.  It provides access to the\nmathematical functions defined by the C standard.', 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, 'factorial': <built-in function factorial>, '__file__': '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so', 'copysign': <built-in function copysign>, 'expm1': <built-in function expm1>, 'ceil': <built-in function ceil>, 'isinf': <built-in function isinf>, 'sinh': <built-in function sinh>, '__name__': 'math', 'trunc': <built-in function trunc>, 'cos': <built-in function cos>, 'pi': 3.141592653589793, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sin': <built-in function sin>, 'atan2': <built-in function atan2>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}

Code:
'''
moduleName = input("Please input module name:")
aMoObj = __import__(moduleName)
print(aMoObj.__dict__)

# 
# Tip_040201 编写一个类Name，能被如下代码调用：
# 
# aName = Name("John Green")
# print(aName.getLastName())
# print(len(aName))
# print(aName.split())
# print(aName.lower())
# 
# Run:
# 
# Green
# 10
# ['John', 'Green']
# john green
# 
# Code:

class Name(str):
    def getLastName(self):
        return self.split()[-1] if self else ""

'''  
Tip_040202 实现一个队列类FIFO，push/pull

客户端代码/Run：
aQueue = Queue()
aQueue.push("hello")
aQueue.push(42)
print(len(aQueue))
print(aQueue.pull()) # hello
print(aQueue.pull()) # 42
print(aQueue.pull()) # IndexError

Code:
'''
class Queue(list):
    def push(self, i):
        self.append(i)
    def pull(self):
        return self.pop(0)

''' 
Tip_040203 实现tail功能(每隔1秒检查文件中的内容，并将新增的行输出)
 
Code:
'''
import time

def follow(fileName):
    with open(fileName) as aFile:
        aFile.seek(0, 2)
        while True:
            curPos = aFile.tell()
            aFile.seek(0, 2)
            endPos = aFile.tell()
            aFile.seek(curPos)
            if endPos > curPos:
                for line in aFile:
                    print(line, end='')
            time.sleep(1)

if __name__ == "__main__":
    follow("a.txt")

'''
Tip_040204 Tail类

客户端代码:
def printLine(txt):
    """ Prints received text """
    print(txt)

t = Tail('/var/log/syslog')
t.register_callback(printLine)
t.follow(s=5)

Code:

https://github.com/maodouzi/python-tail
'''

''' 
Tip_050101 让用户输入两个实数，输出他们的和。如果用户的输入有误，给出提示。
 
Run:
 
Please input A: 4
Please input B: 56
Sum = 60.0
 
Please input A: dd
Please input B: 3
Value Error!
could not convert string to float: dd
 
Code:
'''

aNum = input("Please input A: ")
bNum = input("Please input B: ")

try:
    sumNum = float(aNum) + float(bNum)
except ValueError as e:
    print("Value Error!")
    print(e)
    exit()

print("Sum =", sumNum)

'''
Tip_050201 让用户输入两个实数，输出他们的和。如果用户的输入有误，给出提示。正则表达式。

Run:

Please input A: 4.5
Please input B: 3.d
B not a float!

Please input A: 4.5
Please input B: 0.034
Sum = 4.534

Code:
'''
import re

aNum = input("Please input A: ")
bNum = input("Please input B: ")

reFloatStr = re.compile("^\d+(\.\d+)?$")

flag = True

if not reFloatStr.search(aNum):
    print("A not a float!")
    flag = False
if not reFloatStr.search(bNum):
    print("B not a float!")
    flag = False

if flag:
    sumNum = float(aNum) + float(bNum)
    print("Sum =", sumNum)

''' 	
Tip_050202 统计一个文件所有包含数字的行。
测试文件如下：
apple banana 2
3hello 
good orange
 
Run:
 
apple banana 2
3hello 
 
Code:
'''
import re

reNumStr = re.compile("\d+")

for line in open("test.txt"):
    line = line.rstrip("\n")
    if reNumStr.search(line):
        print(line)

'''
Tip_050203 找出一个文件中所有整数，打印输出它们的和。
测试文件如下：
apple banana 23
33hello 
good 45 orange

Run:
[11, 22, 3, 4]
40

Code:
'''

import re

aList = []
reInt = re.compile("\d+")
for line in open("test.txt"):
    tmpStrList = reInt.findall(line)
    tmpIntList = [int(item) for item in tmpStrList]
    aList.extend(tmpIntList)

print(aList)
print(sum(aList))

'''
Tip_050204. 随机生成4个[1-10]之间的自然数并输出到屏幕，要求输入24点的算法，输出True/False。

Run:
Numbers are: 6, 1, 2, 6: 
6*1*(6-2)
Right!

Code:
'''
import random
import re

reCmp = re.compile(r'^[\d+\-*/()]+$')

# while True:
for i in range(100):
    intList = [random.randint(1,10) for i in range(4)]
    aStr = input('Numbers: %s' % intList)
    aStr = re.sub(r'\s+', '', aStr)
    print(aStr)
    
    if not reCmp.search(aStr):
        print('Input error!')
        continue
    inputList = [i for i in re.split(r'[\D+]', aStr) if i.strip()]
    # print(inputList)
    inputList = map(int, inputList)
    if not sorted(inputList) == sorted(intList):
        print('Wrong number!')
        continue
    if eval(aStr) == 24:
        print(True)
    else:
        print(False)

'''
Tip_050301 编写装饰器makebold和makeitalic

客户端代码：
@makebold
@makeitalic
def hello():
    return "hello world"

print(hello())

Run:
<b><i>hello world</i></b>
	
Code:
'''
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print(hello())

'''
Tip_060201 完成Basic Auth验证，取得API信息

Code:
'''
import urllib.request
import urllib.response
import ssl

userName = "xxxxxx"
passWord  = "HBxxxxxx!@#"
top_level_url = 'https://58.53.185.155:56789/api/report/internet/summary?request={%22report_datetime%22:{%22defined_by%22:%22period%22,%22start_time%22:%222018-04-26%2004:00%22,%22end_time%22:%222018-04-26%2005:00%22},%22unit%22:%22bps%22,%22protocol%22:%22ipv4%22,%22data_format%22:%22graph_data%22,%22display_data%22:%22yes%22}'

ssl._create_default_https_context = ssl._create_unverified_context

# create an authorization handler
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, top_level_url, userName, passWord);

auth_handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(auth_handler)

urllib.request.install_opener(opener)

try:
    req = urllib.request.Request(top_level_url, headers={'Content-Type': 'application/json'})    
    result = opener.open(req)
    messages = result.read()
    print (messages)
except IOError as e:
    print (e)

'''
Tip_060301 编写一个多线程执行的Demo，每个线程打印出线程名，模拟IO密集型和CPU密集型两种情况。

Code:
'''
import time, threading, random

def doWork():
    name = threading.currentThread().getName()
    print("%s start..." % name)
    # print(sum(random.random() for i in range(10000000)))
    print("%s stop..." % name)

startTime = time.time()
aThread = threading.Thread(target=doWork, name="aThread")
bThread = threading.Thread(target=doWork, name="bThread")
aThread.start()
bThread.start()

aThread.join()
bThread.join()
print(time.time()-startTime)

'''
Tip_060302 编写Demo验证线程竞争情况

Code:
'''
import time, threading, random
a = 0
lock = threading.Lock()

def doWork():
    global a
    for i in range(1000000):
        lock.acquire()
        a = a + 1
        lock.release()

startTime = time.time()
aThread = threading.Thread(target=doWork, name="aThread")
bThread = threading.Thread(target=doWork, name="bThread")
aThread.start()
bThread.start()

aThread.join()
bThread.join()
print(a)

'''
Tip_060303 像管理线程一样管理进程

Code:
'''
import time, multiprocessing, random, logging, sys

def doWork():
    print(sum([random.random() for i in range(10000000)]))
    sys.stdout.flush()

if __name__ == "__main__":
    multiprocessing.log_to_stderr(logging.DEBUG)
    startTime = time.time()
    time.clock()
    aProcess = multiprocessing.Process(target=doWork, name="aProcess")
    aProcess.start()
    bProcess = multiprocessing.Process(target=doWork, name="bProcess")
    bProcess.start()
    
    aProcess.join()
    bProcess.join()
    print("== ", time.time() - startTime)

'''
Tip_060304 进程池Demo

Code:
'''
import time, multiprocessing, random

def doWork(j):
    print("%s: start... : %s" % (multiprocessing.current_process().name, time.time()))
    ret = j
    ret = sum([random.random() for i in range(10000000)])
    print("%s: stop...  : %s" % (multiprocessing.current_process().name, time.time()))
    return j,ret

if __name__ == "__main__": # Bug
    startTime = time.time()
    p = multiprocessing.Pool(4) # 1
    aList = p.map(doWork, range(8))
    print(aList)
    print(time.time() - startTime)

'''
Tip_060305 线程池

Code:
'''
import time, multiprocessing.dummy, random

def doWork(j):
    print("%s: start... : %s" % (multiprocessing.dummy.current_process().name, time.time()))
    ret = j
    ret = sum([random.random() for i in range(10000000)])
    print("%s: stop...  : %s" % (multiprocessing.dummy.current_process().name, time.time()))
    return j,ret

if __name__ == "__main__": # Bug
    startTime = time.time()
    p = multiprocessing.dummy.Pool(4) # 1
    aList = p.map(doWork, range(8))
    print(aList)
    print(time.time() - startTime)

'''
Tip_060306 Subprocess获取中文输出

Code:
项目右键/property/Resource/Text-File-Encoding/Other/Utf-8
'''

# -*- utf-8 -*-
ret = u'哈'
print(ret)
#print(ret.encode(encoding='utf_8', errors='strict'))

######## test.py ######### 
import subprocess

ret = subprocess.check_output([r'C:\Users\pear\AppData\Local\Programs\Python\Python36\python.exe',
                               r'C:\Users\pear\eclipse-workspace\test\test2.py'])

print(ret)
print(ret.decode('utf-8'))

'''
Tip_070101 Scrapy Demo，获取http://quotes.toscrape.com/tag/humor/中的箴言

[官方文档] https://docs.scrapy.org/en/latest/
[css & xpath] https://github.com/scrapy/quotesbot

scrapy runspider /Users/wxdev_mac/eclipse-workspace/test3/test.py -o test.json 

Code:
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

'''
Tip_080101 TK，编写加法计算器

+---------------+
| NumA: ______  |
| NumB: ______  |
| NumC: ______  |
|               |
|  (Button)     |
+---------------+

Code: 
'''
from tkinter import Label, Frame, Tk, Button, Entry
from tkinter import RIGHT, LEFT
# from tkinter.filedialog import askopenfilename
tk = Tk()

def cmd():
    # aStr = askopenfilename
    aFloat = float(entryList[0].get())
    bFloat = float(entryList[1].get())
    entryList[2].delete(0, len(entryList[2].get()))
    entryList[2].insert(0, round(aFloat+bFloat, 2))

nameList = ['NumberA', 'NumberB', 'NumberC']
frameList = [Frame(tk) for i in nameList]
labelList = [Label(i, text=j) for i,j in zip(frameList, nameList)]
entryList = [Entry(i) for i in frameList]

for lable,entry,frame in zip(labelList, entryList, frameList):
    lable.pack(side=LEFT)
    entry.pack(side=RIGHT)
    frame.pack()
    
btn = Button(tk, text="Add", command=cmd)
btn.pack(side=RIGHT)

tk.mainloop()

'''
Tip_090101 如何在一个虚拟环境中运行Python项目？不同的Python版本/Module版本。

参考：https://github.com/maodouzi/LearningDjango-1-4
'''
'''
Tip_100101 为如下方法编写单元测试，要求覆盖整数加法，字符串加法，类型不匹配抛出异常三种情况

Code:
'''
import unittest

def add(x, y):
    return x+y

class ATest(unittest.TestCase):
    def testAddInt(self):
        exp = 8
        ret = add(3, 5)
        self.assertEqual(ret, exp)
    def testValueError(self):
        self.assertRaises(TypeError, add, 3, "5")
    def testAddString(self):
        self.skipTest("Skip due to Bug #13452")
        self.assertEqual(add("hello", "string"), "hellostring")

'''
Tip_100102 单元测试，获取大于20000的数字

Code:
'''
import unittest
import sys, re

def myPrint(obj):
    print(obj)

# def find20000(aStr):
#     ret = re.findall(r'((\d{6,})|([2-9]\d{4,}))', aStr)
#     print(ret)
#     ret = [int(i[0]) for i in ret]
#     ret = [i for i in ret if i > 20000]
#     return ret

def findNumber(aStr, aNum):
    ret = re.findall(r'\d+', aStr)
    ret = [int(i) for i in ret]
    ret = [i for i in ret if i > 20000]
    return ret

def find20000(aStr):
    return findNumber(aStr, 20000)

class FixtureTest(unittest.TestCase):
    def setUp(self):
        myPrint('In setUp')
    def tearDown(self):
        myPrint('In tearDown')
    def testCaseA(self):
        aStr = "abcde100001"
        ret = find20000(aStr)
        exp = [100001]
        self.assertEqual(ret, exp)
    def testCaseB(self):
        aStr = "abcde20001"
        ret = find20000(aStr)
        exp = [20001]
        self.assertEqual(ret, exp)
    def testCaseC(self):
        aStr = "abcde20000"
        ret = find20000(aStr)
        exp = [20000]
        self.assertNotEqual(ret, exp)
    def testCaseD(self):
        aStr = "abcde20000a1000001b20001"
        ret = find20000(aStr)
        exp = [1000001, 20001]
        self.assertEqual(ret, exp)

if __name__ == '__main__':
    unittest.main()

'''
Tip_100103 Mock，为checkWeb编写Unittest，Mock模拟http.client模块中的对象

Code:
'''
import unittest, http.client, socket
from unittest.mock import MagicMock, create_autospec

# import unittest, http.client, socket
# from mock import MagicMock, create_autospec

def checkWeb(addr, port, resource):
    resource.lstrip(r'/')
    resource = '/' + resource
    try:
        con = http.client.HTTPConnection(addr, port)
        con.request('GET', resource)
        response = con.getresponse()
    except socket.error:
        return False
    finally:
        con.close()
    if response.status in [200, 301]:
        return True
    return False

class HttpConnTest(unittest.TestCase):            
    def test_checkWebOK(self):
        mockResp = MagicMock()
        mockResp.status = 200
        
        mockHttpConn = MagicMock()
        mockHttpConn.getresponse.return_value = mockResp

        http.client.HTTPConnection = MagicMock(return_value = mockHttpConn)
        
        ret = checkWeb("www.bing.com", 80, "/")
        self.assertTrue(ret)

'''
Tip_100201 MySQL，创建表，插入数据，查询数据
'''
# pip install PyMySQL
import pymysql

connection = pymysql.connect(host='65.52.172.145',
                             port=3306,
                             user='root',
                             password='a44e604C3279',
                             db='test',
                             charset='utf8')

# 获取游标
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS `users`')

# 创建数据表
effect_row = cursor.execute('''
CREATE TABLE `users` (
  `name` varchar(32) NOT NULL,
  `age` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
''')

try:
    connection.begin()
    
    # 插入数据(元组或列表)
    effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    
    # 插入数据(字典)
    info = {'name': 'test', 'age': 19}
    effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)
    
    connection.commit()
except:
    connection.rollback()
# 批量插入
effect_row = cursor.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('hello', 13),
        ('fake', 28),
    ])

# 执行查询 SQL
cursor.execute('SELECT * FROM `users`')
# 获取单条数据
ret = cursor.fetchone()
print(ret)
# 获取前N条数据
ret = cursor.fetchmany(3)
print(ret)
# 获取所有数据
ret = cursor.fetchall()
print(ret)

'''
Tip_100202 Sqlite3，创建表，插入数据，查询数据
'''
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('drop table if exists user')
cursor.execute('create table user '
               '(id varchar(20) primary key, name varchar(20))')
cursor.execute("insert into user (id, name) "
               "values ('1', 'Michael')")
cursor.execute('select * from user')
rows = cursor.fetchall()
print(rows)
cursor.close()
conn.commit()
conn.close()

'''
Tip_100203 SqlAlchemy+Sqlite3，创建表，插入数据，查询数据

Code:
'''

from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base = declarative_base()
class User(Base):
    __tablename__ = 'user' # 表的名字
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
engine = create_engine(r'sqlite:///database.db')
# engine = create_engine(r'mysql+pymysql://root:a44e604C3279@65.52.172.145:3306/test', echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

session = DBSession()
user = session.query(User).filter(User.id=='5').all()
if not user:
    new_user = User(id='5', name='Bob')
    session.add(new_user)
    session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)
session.close()

'''
Tip_100204 SqlAlchemy，一对多关系

Code:
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine(r'sqlite:///database.db')
Base = declarative_base()

# 单表
class Test(Base):
    __tablename__ = 'test'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))

# 一对多
class Team(Base):
    __tablename__ = 'team'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32))

class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    team_id = Column(Integer, ForeignKey('team.tid'))
    #加上底下这行后，不用使用.join()也可实现联表查询
    #哪个表做外链，就把relationship加到哪个表
    favor = relationship("Team", backref='user')

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

drop_db()
init_db()

Session = sessionmaker(bind=engine)
session = Session()

#往team表里插入两条数据
session.add(Team(caption='dba'))
session.add(Team(caption='ddd'))
# session.add(Team(caption='dd2'))
session.commit()

session.add_all([
    User(name='zzz',team_id=1),
    User(name='sss',team_id=2),
    User(name='ccc',team_id=3),
])
session.commit()

ret = session.query(User).filter(User.name=='zzz').all()
# ret = session.query(User.name).filter(User.name=='zzz').all()
obj = ret[0]
print(ret, obj, obj.name)

# 等价于SELECT user.name AS FROM user INNER JOIN team ON team.tid = user.team_id
ret = session.query(User.name, Team.caption).join(Team).all()
print(ret)

ret = session.query(User.name, Team.caption).join(Team,isouter=True).all()
print(ret)

ret = session.query(User).all()
for obj in ret:
    print(obj.nid,obj.name, 
          obj.favor,
          obj.favor.tid if obj.favor else None,
          obj.favor.caption if obj.favor else None)

ret = session.query(Team).filter(Team.caption == 'dba').all()
print(ret[0].tid)
print(ret[0].caption)
print(ret[0].user)

'''
Tip_100205 SqlAlchemy，多对多关系

Code:
'''
# coding:utf-8
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DB_URI = r'sqlite:///database.db'
# DB_URI = "mysql+mysqldb://root:root@127.0.0.1:3306/python?charset=utf8"
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# 创建一个多对多的关系(老师与学生的关系)需要创建一个中间表
# 创建一个中间表
teacher_classes = Table(
    "teacher_classes",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.id"), nullable=False, primary_key=True),
    Column("classes_id", Integer, ForeignKey("classes.id"), nullable=False, primary_key=True)
)

# 创建老师的映射
class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(100))
    classes = relationship("Classes", secondary=teacher_classes)

    def __repr__(self):
        return "<Teacher id='%s' teacher_name='%s'>" % (self.id, self.teacher_name)


# 创建学生的映射
class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classes_name = Column(String(100))
    teacher = relationship("Teacher", secondary=teacher_classes)

    def __repr__(self):
        return "<Classes id='%s' classes_name='%s'>" % (self.id, self.classes_name)

# 创建数据库
Base.metadata.create_all()

# 创建两个老师
teacher1 = Teacher(teacher_name='admin')
teacher2 = Teacher(teacher_name='grunt')
teacher3 = Teacher(teacher_name='shuihen')

# 创建两门课程
classes1 = Classes(classes_name="java")
classes2 = Classes(classes_name="python")

# 添加数据
teacher1.classes = [classes1,classes2]
teacher2.classes = [classes1,classes2]
teacher3.classes = [classes1]
session.add(teacher1)
session.add(teacher2)
session.add(teacher3)
session.commit()

# 查询下数据(根据老师查询课程)
teacher = session.query(Teacher).first()
print(teacher.classes)

# 根据课程查询老师
classes = session.query(Classes).get(1)
print(classes.teacher)

# 根据老师查询课程
teacher = session.query(Teacher).get(3)
print(teacher.classes)

'''
Tip_100206 XPath
'''
# pip install lxml
# https://doc.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html
# https://www.w3schools.com/xml/xpath_syntax.asp
# https://cuiqingcai.com/2621.html 

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html).decode()
# html = etree.parse('hello.html')
# result = etree.tostring(html, pretty_print=True)
print(result)

print(type(html))
# 获取所有的 <li> 标签
result = html.xpath('//li')
print(result)
print(len(result))
print(type(result))
print(type(result[0]))

# 获取 <li> 标签的所有 class
result = html.xpath('//li/@class')
print(result)

# 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result = html.xpath('//li/a[@href="link1.html"]')
print(result)

# 获取 <li> 标签下的所有 <span> 标签
# 注意这么写是不对的
# result = html.xpath('//li/span')
# 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
result = html.xpath('//li//span')
print(result)
# 获取 <li> 标签下的所有 class，不包括 <li>
result = html.xpath('//li/a//@class')
print(result)

# 获取最后一个 <li> 的 <a> 的 href
result = html.xpath('//li[last()]/a/@href')
print(result)

# 获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
print(result[0].text)

# 获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print(result[0].tag)

'''
Tip_100401 使用Django实现一个账目管理系统

https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest
或者 https://gitee.com/wu-wen-xiang/project-django-demo

https://github.com/wu-wenxiang/Project-Python-Webdev
或者 https://gitee.com/wu-wen-xiang/project-python-webdev-demo
'''

'''
Tip_110101 psutil的使用

Code:
'''

# https://github.com/giampaolo/psutil
import datetime
import psutil
import pprint
from subprocess import PIPE

print(psutil.cpu_times())
print(psutil.cpu_times())
print(psutil.cpu_times().user)
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times(percpu=True))

print(psutil.virtual_memory())
print(psutil.virtual_memory().total)
print(psutil.swap_memory())

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.disk_io_counters(perdisk=True))

print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

pprint.pprint(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats()) # 获取网络接口状态
# print(psutil.net_connections()) # need admin permission

print(psutil.users())
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S'))

print(psutil.pids())
print(psutil.Process(1800))
p = psutil.Process(1800)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.status())
print(p.create_time())
print(p.uids())
print(p.gids())
print(p.cpu_times())
print(p.memory_percent())
print(p.memory_info())
print(p.connections())
print(p.num_threads())

print(psutil.test())

p = psutil.Popen(['ls', '-l'], stdout=PIPE)
print(p.name())
print(p.username())
ret = p.communicate()
print(ret[0].decode())

'''
Tip_110102 IPy
'''
# https://github.com/autocracy/python-ipy/

from IPy import IP
ip = IP('127.0.0.0/30')
for x in ip:
    print(x)
# 127.0.0.0
# 127.0.0.1
# 127.0.0.2
# 127.0.0.3

ip2 = IP('0x7f000000/30')
print(ip == ip2) # True

print(ip.reverseNames())
# ['0.0.0.127.in-addr.arpa.', '1.0.0.127.in-addr.arpa.', '2.0.0.127.in-addr.arpa.', '3.0.0.127.in-addr.arpa.']
print(ip.reverseName())
# '0-3.0.0.127.in-addr.arpa.'
print(ip.iptype())
# 'LOOPBACK' / 'PRIVATE'

print(IP('10.0.0.0/8').version())
# 4
print(IP('::1').version())
# 6
print(IP(0x7f000001))
# 127.0.0.1
print(IP('0x7f000001'))
# 127.0.0.1
print(IP('127.0.0.1'))
# 127.0.0.1
print(IP('10'))
# 10.0.0.0
print(IP('1080:0:0:0:8:800:200C:417A'))
# 1080::8:800:200c:417a
print(IP('1080::8:800:200C:417A'))
# 1080::8:800:200c:417a
print(IP('::1'))
# ::1
print(IP('::13.1.68.3'))
# ::d01:4403
print(IP('127.0.0.0/8'))
# 127.0.0.0/8
print(IP('127.0.0.0/255.0.0.0'))
# 127.0.0.0/8
print(IP('127.0.0.0-127.255.255.255'))
# 127.0.0.0/8

# Derive network address
print(IP('127.0.0.1/255.0.0.0', make_net=True))
# 127.0.0.0/8
print(IP('127.0.0.1').make_net('255.0.0.0'))
# 127.0.0.0/8

# Convert address to string
# Nearly all class methods which return a string have an optional parameter 'wantprefixlen' which controls if the prefixlen or netmask is printed. Per default the prefilen is always shown if the network contains more than one address:
# 
# wantprefixlen == 0            / None                  1.2.3.0
# wantprefixlen == 1            /prefix                 1.2.3.0/24
# wantprefixlen == 2            /netmask                1.2.3.0/255.255.255.0
# wantprefixlen == 3            -lastip                 1.2.3.0-1.2.3.255
# You can also change the defaults on an per-object basis by fiddling with the class members:
# 
# NoPrefixForSingleIp
# WantPrefixLen
# Examples of string conversions:
# 
print(IP('10.0.0.0/32').strNormal())
# '10.0.0.0'
print(IP('10.0.0.0/24').strNormal())
# '10.0.0.0/24'
print(IP('10.0.0.0/24').strNormal(0))
# '10.0.0.0'
print(IP('10.0.0.0/24').strNormal(1))
# '10.0.0.0/24'
print(IP('10.0.0.0/24').strNormal(2))
# '10.0.0.0/255.255.255.0'
print(IP('10.0.0.0/24').strNormal(3))
# '10.0.0.0-10.0.0.255'
ip = IP('10.0.0.0')
print(ip)
# 10.0.0.0
ip.NoPrefixForSingleIp = None
print(ip)
# 10.0.0.0/32
ip.WantPrefixLen = 3
print(ip)
# 10.0.0.0-10.0.0.0

# Work with multiple networks
from IPy import IP, IPSet
print(IP('10.0.0.0/22') - IP('10.0.2.0/24'))
# IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24')])
print(IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24'), IP('10.0.2.0/24')]))
# IPSet([IP('10.0.0.0/22')])
s = IPSet([IP('10.0.0.0/22')])
s.add(IP('192.168.1.0/29'))
print(s)
# IPSet([IP('10.0.0.0/22'), IP('192.168.1.0/29')])
s.discard(IP('192.168.1.2'))
print(s)
# IPSet([IP('10.0.0.0/22'), IP('192.168.1.0/31'), IP('192.168.1.3'), IP('192.168.1.4/30')])

# IPSet supports the set method isdisjoint:
print(s.isdisjoint(IPSet([IP('192.168.0.0/16')])))
# False
print(s.isdisjoint(IPSet([IP('172.16.0.0/12')])))
# True

# IPSet supports intersection:
print(s & IPSet([IP('10.0.0.0/8')]))
# IPSet([IP('10.0.0.0/22')])

'''
Tip_110103 dnspython
'''

# http://www.dnspython.org/examples.html
# https://github.com/rthalley/dnspython

# Get the MX target and preference of a name:
 
import dns.resolver
 
answers = dns.resolver.query('dnspython.org', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
           
# Transfer a zone from a server and print it with the names sorted in DNSSEC order:
# import dns.query
# import dns.zone
#  
# z = dns.zone.from_xfr(dns.query.xfr('204.152.189.147', 'dnspython.org'))
# names = z.nodes.keys()
# names.sort()
# for n in names:
#     print(z[n].to_text(n))
           
# Use DNS dynamic update to set the address of a host to a value specified on the command line:
 
# import dns.query
# import dns.tsigkeyring
# import dns.update
# import sys
#  
# keyring = dns.tsigkeyring.from_text({
#     'host-example.' : 'XXXXXXXXXXXXXXXXXXXXXX=='
# })
#  
# update = dns.update.Update('dyn.test.example', keyring=keyring)
# update.replace('host', 300, 'a', sys.argv[1])
#  
# response = dns.query.tcp(update, '10.0.0.1')
# print(response)
           
# Manipulate domain names:
 
import dns.name
 
n = dns.name.from_text('www.dnspython.org')
o = dns.name.from_text('dnspython.org')
print(n.is_subdomain(o))         # True
print(n.is_superdomain(o))       # False
print(n > o)                     # True
rel = n.relativize(o)            # rel is the relative name 'www'
n2 = rel + o
print(n2 == n)                   # True
print(n.labels)                  # ('www', 'dnspython', 'org', '')
           
# Generate reverse mapping information
 
# Usage: reverse.py ...
#
# This demo script will load in all of the zones specified by the
# filenames on the command line, find all the A RRs in them, and
# construct a reverse mapping table that maps each IP address used to
# the list of names mapping to that address.  The table is then sorted
# nicely and printed.
#
# Note!  The zone name is taken from the basename of the filename, so
# you must use filenames like "/wherever/you/like/dnspython.org" and
# not something like "/wherever/you/like/foo.db" (unless you're
# working with the ".db" GTLD, of course :)).
#
# If this weren't a demo script, there'd be a way of specifying the
# origin for each zone instead of constructing it from the filename.
 
import dns.zone
import dns.ipv4
import os.path
import sys
 
reverse_map = {}
 
for filename in sys.argv[1:]:
    zone = dns.zone.from_file(filename, os.path.basename(filename),
                              relativize=False)
    for (name, ttl, rdata) in zone.iterate_rdatas('A'):
        l = reverse_map.get(rdata.address)
        if l is None:
            l = []
            reverse_map[rdata.address] = l
        l.append(name)
 
keys = reverse_map.keys()
for k in sorted(keys, key=lambda a1: dns.ipv4.inet_aton(a1)):
    v = reverse_map[k]
    v.sort()
    l = map(str, v)     # convert names to strings for prettier output
    print(k, l)
           
# Convert IPv4 and IPv6 addresses to/from their corresponding DNS reverse map names:
 
import dns.reversename
n = dns.reversename.from_address("127.0.0.1")
print(n)
print(dns.reversename.to_address(n))
           
# Convert E.164 numbers to/from their corresponding ENUM names:
 
import dns.e164
n = dns.e164.from_e164("+1 555 1212")
print(n)
print(dns.e164.to_e164(n))

'''
Tip_110104 xlsxwriter
'''
# https://github.com/jmcnamara/XlsxWriter

import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
# worksheet.insert_image('B5', 'logo.png')

workbook.close()

'''
Tip_110105 pexpect

https://pexpect.readthedocs.io/en/stable/examples.html
https://github.com/pexpect/pexpect
'''

'''
Tip_110106 redis
'''

# http://redis.io/topics/quickstart
# http://redis.io/commands
# https://github.com/andymccurdy/redis-py

import redis
r = redis.StrictRedis(host='65.52.172.145', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo').decode())

for key, value in (('A', '1'), ('B', '2'), ('C', '3')):
    r.set(key, value)
for key in r.scan_iter():
    print(key.decode(), r.get(key).decode())
# A 1
# B 2
# C 3

'''
Tip_110201 如何使用Fabric实现自动化部署？

参考：https://github.com/wu-wenxiang/Project-Python-Webdev
或者：https://gitee.com/wu-wen-xiang/project-python-webdev-demo
'''

'''
Tip_120101 Numpy快速入门

Code:
'''
# -*- coding: utf-8 -*
import numpy as np #一般以np作为numpy的别名

a = np.array([2, 0, 1, 5]) #创建数组
print(a) #输出数组
print(a[:3]) #引用前三个数字（切片）
print(a.min()) #输出a的最小值
a.sort() #将a的元素从小到大排序，此操作直接修改a，因此这时候a为[0, 1, 2, 5]
b= np.array([[1, 2, 3], [4, 5, 6]]) #创建二维数组
print(b*b) #输出数组的平方阵，即[[1, 4, 9], [16, 25, 36]]

'''
Tip_120102 Pandas快速入门

Code:
'''
# -*- coding: utf-8 -*-
import pandas as pd 

s = pd.Series([1,2,3], index=['a', 'b', 'c']) 
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns = ['a', 'b', 'c']) 
d2 = pd.DataFrame(s) 

print(d.head())
print(d.describe()) 

#读取文件，注意文件的存储路径不能带有中文，否则读取可能出错。
pd.read_excel('data.xls') #读取Excel文件，创建DataFrame。
pd.read_csv('data.csv', encoding = 'utf-8') #读取文本格式的数据，一般用encoding指定编码。

'''
Tip_120103 Pandas，如何实现在多列值情况下的Vlookup

Code:
'''
import pandas as pd
 
data = {'name': ['Alice', 'Bob', 'Charles', 'David', 'Eric'],
        'year': [2017, 2016, 2016, 2017, 2017],
        'salary': [40000, 20000, 30000, 20000, 30000]}
 
df = pd.DataFrame(data)

df2 = pd.DataFrame({'name': ['Alice', 'Bob'],
                    'year': [2017, 2016]})

df_new = df.set_index(['name','year'])

df2Dict = df2.to_dict('index')
rows = [df2Dict[i] for i in sorted(df2Dict)]
rows = [df_new.loc[i['name'], i['year']]['salary'] for i in rows]
df2['salary'] = pd.Series(rows)

print(df2)

'''
Tip_120104 Pandas SQL应用

Code:
'''
from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user' # 表的名字
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    def __repr__(self):
        return '<{}::{}>'.format(self.id, self.name)
    
engine = create_engine(r'sqlite:///database.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()

import pandas as pd
df_old = pd.read_sql('user', con=engine)
df_old.set_index('id', inplace=True)

df = pd.DataFrame({'id': [str(i) for i in range(10, 12)], 
                   'name': ['Name-{}'.format(i) for i in range(10, 12)]})
df.set_index('id', inplace=True)
df = df.append(df_old)
df.to_sql('user', con=engine, if_exists='replace')

session = DBSession()
users = session.query(User).all()
for user in users:
    print(user)
session.close()

'''
Tip_120105 scipy快速入门

Code:
'''
# -*- coding: utf-8 -*
#求解非线性方程组2x1-x2^2=1,x1^2-x2=2
from scipy.optimize import fsolve #导入求解方程组的函数
def f(x): #定义要求解的方程组
  x1 = x[0]
  x2 = x[1]
  return [2*x1 - x2**2 - 1, x1**2 - x2 -2]

result = fsolve(f, [1,1]) #输入初值[1, 1]并求解
print(result) #输出结果，为array([ 1.91963957,  1.68501606])

#数值积分
from scipy import integrate #导入积分函数
def g(x): #定义被积函数
  return (1-x**2)**0.5

pi_2, err = integrate.quad(g, -1, 1) #积分结果和误差
print(pi_2 * 2) #由微积分知识知道积分结果为圆周率pi的一半

'''
Tip_120106 绘制方程曲线，y = (1-x**2)**0.5，x的范围从-1到1

Code:
'''
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt #导入Matplotlib

x = np.linspace(-1, 1, 1000) #作图的变量自变量
y = (1-x**2)**0.5 #因变量y

plt.figure(figsize = (8, 4)) #设置图像大小
plt.plot(x,y,label = '$y=(1-x**2)**0.5$', color = 'red', linewidth = 2) #作图，设置标签、线条颜色、线条大小
plt.xlabel('Time(s) ') # x轴名称
plt.ylabel('Volt') # y轴名称
plt.title('A Simple Example') #标题
plt.ylim(0, 1.1) #显示的y轴范围
plt.legend() #显示图例
plt.show() #显示作图结果

'''
Tip_120107 PyEcharts
'''
# https://github.com/d3/d3/wiki/Gallery
# https://github.com/pyecharts/pyecharts
# https://github.com/pyecharts/flask_demo

'''
Tip_120108 IIS Log Analysis

日志文件：https://share.weiyun.com/5zY4yG9

Code:
'''

aList = [i.split() for i in open('test.txt', encoding='utf-8') if i.startswith('20')]
bList = 'date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) sc-status sc-substatus sc-win32-status time-taken'.split()

# print(aList[:5], end='')
# print(bList)

import pandas as pd

p = pd.DataFrame(aList, columns=bList)
p1 = p.loc[:, ['cs-uri-stem', 'cs-method', 'c-ip', 'time-taken']]
p1['datetime'] = pd.to_datetime(p['date']+' '+p['time'])
p1['time-taken'] = pd.to_numeric(p1['time-taken'])
pTime = p1.set_index('datetime')
pTimeAll = pTime.loc[:, ['time-taken']].resample(rule = '1T').count()
pTime20S = pTime[pTime['time-taken']>20000].loc[:, ['time-taken']].resample(rule = '1T').count()

pIP = p1[p1['time-taken']>20000].loc[:, ['c-ip', 'time-taken']]
pIP = pIP.groupby('c-ip').count()
print(pIP[pIP['time-taken']>10])

pURI = p1[p1['time-taken']>20000].loc[:, ['cs-uri-stem', 'time-taken']]
pURI = pURI.groupby('cs-uri-stem').count()
print(pURI[pURI['time-taken']>10])

import matplotlib.pyplot as plt

# plot the data
pTimeAll.plot()
pTime20S.plot()
plt.show()

'''
Tip_120201 Sklearn-Preprocessing

Code:
'''
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing

X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
print('原数据：\n',X_train)

print('标准化1：')
print(preprocessing.scale(X_train))
min_max_scaler = preprocessing.MinMaxScaler()
print('标准化2：')
print(min_max_scaler.fit_transform(X_train))
print('规范化：')
print(preprocessing.normalize(X_train, norm='l2'))

print('原数据：')
print(X_train)
print('二值化：')
binarizer = preprocessing.Binarizer(threshold=0.0)
binarizer.fit(X_train)  
print(binarizer.transform(X_train))

from sklearn.impute import SimpleImputer
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print('原数据：')
print(X)
imp = SimpleImputer(missing_values=np.nan, strategy='mean') 
print('----------')
print('按列均值填充缺失：')
imp.fit(X)
print(imp.transform(X))

X = np.arange(6).reshape(3,2)
print('原数据：')
print(X)
poly = preprocessing.PolynomialFeatures(2)
print('多项式转化：')
print('(X1, X2)→(1, X1, X2, X1^2, X1X2, X2^2)')
print(poly.fit_transform(X))

'''
Tip_120202 Sklearn-linear-model-plot-polynomial-interpolation
'''
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)


# generate points used to plot
x_plot = np.linspace(0, 10, 100)

# generate points and keep a subset of them
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:20])
y = f(x)

# create matrix versions of these arrays
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

colors = ['teal', 'yellowgreen', 'gold']
lw = 2
plt.plot(x_plot, f(x_plot), color='cornflowerblue', linewidth=lw,
         label="ground truth")
plt.scatter(x, y, color='navy', s=30, marker='o', label="training points")

for count, degree in enumerate([3, 4, 5]):
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(X, y)
    y_plot = model.predict(X_plot)
    plt.plot(x_plot, y_plot, color=colors[count], linewidth=lw,
             label="degree %d" % degree)

plt.legend(loc='lower left')

plt.show()

'''
Tip_120203 Sklearn-DecisionTree
'''
from sklearn.datasets import load_iris   #sklearn.datasets中很多可用的数据集
from sklearn import tree #导入树模块

iris = load_iris()   #导入iris数据集
print('特征：')
print(iris.data[:10])
print('目标：')
print(iris.target[:10])

clf = tree.DecisionTreeClassifier()   #可以自己设定很多参数，如果不写则默认参数
clf = clf.fit(iris.data, iris.target) #模型训练
print('对第一条记录的预测类别：',clf.predict(iris.data[:1, :]))  #预测
print('第一条记录的实际类别：',iris.target[1])
print('对第一条记录的类别概率预测：',clf.predict_proba(iris.data[:1, :])) #概率预测

'''
Tip_120204 Sklearn-SVM

Code:
'''
from sklearn import datasets, svm
import matplotlib.pyplot as plt
from sklearn.externals.joblib.numpy_pickle_utils import np

digits = datasets.load_digits()
print(digits.keys())
print(digits.images.shape)

images_and_labels = list(zip(digits.images, digits.target))   #查看 前四个图形
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)
plt.show()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
 
print(digits.images[0])    #原数据集第一个记录
print(data[0])    #转换后的数据集的第一个记录

classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples//2],digits.target[:n_samples//2])  #//的含义是只保留除法运算结果的整数部分
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

plt.figure(figsize=(7,10))
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)
 
plt.show()

'''
Tip_120205 Sklearn-LogisticRegression

Code:
'''
from sklearn import linear_model, datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, :2]  # 只选择2列的特征 为了可视化的便利
Y = iris.target
print(X.shape, Y.shape)

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)

print(logreg.coef_)    #查看模型参数beta的估计

h = 0.02    #作图的间隔
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])   #进行预测

Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(5, 3.888))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

plt.scatter(X[:, 0], X[:, 1], s=60, c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())  #不显示横纵轴数值

plt.show()

'''
Tip_120206 Sklearn-Linear-Model

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score  #metric模块用来评价模型效果
# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression() #建立线性回归模型
regr.fit(diabetes_X_train, diabetes_y_train) #模型训练
diabetes_y_pred = regr.predict(diabetes_X_test) #模型预测

print('系数估计:', regr.coef_[0])
print("均方误差: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('拟合优度: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

plt.style.use('ggplot')
plt.scatter(diabetes_X_test, diabetes_y_test,  color='#FF7F00',alpha=0.5,s=50,label='Real Dot')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', alpha=0.7,linewidth=2.5,label='Predict Line')

plt.xticks(())
plt.yticks(())
plt.legend()
plt.show()

'''
Tip_120207 Sklearn-KernelDensity

Code:
'''
import numpy as np
from matplotlib import pyplot as plt

from scipy.stats import norm
from sklearn.neighbors import KernelDensity

N = 100
np.random.seed(1)
X = np.concatenate((np.random.normal(0, 1, int(0.3 * N)),
                    np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]   # [:,np.newaxis]是为了将其转化为2维列向量

true_dens = (0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0]))  #数据真实的概率密度

fig, ax = plt.subplots()
ax.fill(X_plot[:, 0], true_dens, fc='black', alpha=0.2,label='Real Line')

for kernel in ['gaussian', 'tophat', 'epanechnikov']:   #使用三种核密度估计方法来估计
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(X_plot[:, 0], np.exp(log_dens), '-',label="Kernel = '{0}'".format(kernel))

ax.legend(loc='upper left')
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), '+k')

ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)
plt.show()

'''
Tip_120208 Sklearn-KMeans

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle

n_colors = 64
china = load_sample_image("china.jpg") #加载图片
china = np.array(china, dtype=np.float64) / 255 
#转化数据位float64，且除以255(三原色最大值) 使得数据在0-1之间

w, h, d = original_shape = tuple(china.shape)
assert d == 3
image_array = np.reshape(china, (w * h, d)) #将图片数据reshape成为2维

print("使用数据集的一部分子集训练模型")
image_array_sample = shuffle(image_array, random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample) #将颜色聚成64个类

print("对整张图片进行颜色预测(K-means方法)")
labels = kmeans.predict(image_array)  #每个颜色对应的类

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (96,615 colors)')
plt.imshow(china)

plt.figure(2)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (64 colors, K-Means)')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))
plt.show()

'''
Tip_120209 Sklearn-Decomposition-PCA

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()  #导入数据集
X,y = iris.data, iris.target
print('原始维度：',X.shape)
print('进行PCA处理')
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
print('PCA降维后：',X.shape)

fig = plt.figure()
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.Spectral,
           edgecolor='k',s=50)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
plt.show()

'''
Tip_120210 Sklearn-Decomposition-locally_linear_embedding

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets

print('带入数据集')
X, color = datasets.make_swiss_roll(n_samples=1500)
print(X.shape, color.shape)

fig = plt.figure(figsize=(7,5))

ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral,s =30)

plt.axis('tight')
plt.xticks([]), plt.yticks([])
plt.title('Original Data Set')
plt.show()

print("运行 局部线性嵌入")
X_r, err = manifold.locally_linear_embedding(X, n_neighbors=12,n_components=2)  #选择近邻个数为12个，成分个数为2个
print("完成重构. 重构误差: %g" % err)

ig = plt.figure(figsize=(7,5))

plt.scatter(X_r[:, 0], X_r[:, 1], s=30, c=color, cmap=plt.cm.Spectral)
plt.axis('tight')
plt.xticks([]), plt.yticks([])
plt.title('Locally Linear Embedding Data Set')
plt.show()

'''
Tip_120211 Sklearn-Model_Selection-Cross_Val_Score

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

n_samples = 30
X = np.sort(np.random.rand(n_samples))
y = np.cos(1.5*np.pi*X) + np.random.randn(n_samples) * 0.2

X_test = np.linspace(0,1,100)
plt.plot(X_test, np.cos(1.5*np.pi*X_test),color='red', label=r"original function:$y=cos(x)$")
plt.scatter(X, y, edgecolor='b', s=20, label="sample dataset")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim((0, 1))
plt.ylim((-2, 2))
plt.legend(loc="best")
plt.show()

degrees = [1, 4, 15]   
plt.figure(figsize=(14, 5))
for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    polynomial_features = PolynomialFeatures(degree=degrees[i],
                                             include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    pipeline.fit(X[:, np.newaxis], y)

    X_test = np.linspace(0, 1, 100)
    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), color='green',label=f"{degrees[i]}: Model")
    plt.plot(X_test, np.cos(1.5*np.pi*X_test), color='red',label=f"{degrees[i]}: Real Relationship")
    plt.scatter(X, y, edgecolor='b', s=20, label=f"{degrees[i]}: Sample Dataset")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
plt.show()

from sklearn.model_selection import cross_val_score
#利用交叉验证进行模型评估
for i in range(len(degrees)):
    polynomial_features = PolynomialFeatures(degree=degrees[i],
                                             include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features),("linear_regression", linear_regression)])
    scores = cross_val_score(pipeline, X[:, np.newaxis], y,scoring="neg_mean_squared_error", cv=10)  #利用10折交叉验证计算模型的MSE
    print("Degree {}　　　MSE = {:.2e}(+/- {:.2e})".format(degrees[i], -scores.mean(), scores.std()))

'''
Tip_120212 Sklearn-Learn-Curve

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import learning_curve
from sklearn.kernel_ridge import KernelRidge

# 生成数据
rng = np.random.RandomState(0)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

N = 100

svr = SVR(kernel='rbf', C=1e1, gamma=0.1) 
kr = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
train_sizes, train_scores_svr, test_scores_svr = \
                   learning_curve(svr, X[:N], y[:N], 
                   train_sizes=np.linspace(0.1, 1, 20),
                   scoring="neg_mean_squared_error")
train_sizes_abs, train_scores_kr, test_scores_kr = \
                   learning_curve(kr, X[:N], y[:N], 
                   train_sizes=np.linspace(0.1, 1, 20),
                   scoring="neg_mean_squared_error")

plt.figure()

plt.plot(train_sizes, -test_scores_svr.mean(1), 'o-', color="r",
         label="Support Vector Regression")
plt.plot(train_sizes, -test_scores_kr.mean(1), 'o-', color="g",
         label="Kernel Ridgh Regression")
plt.xlabel("Train Size")
# 真实值-预测值，然后平方之后求和平均。线性回归用 MSE 作为损失函数
plt.ylabel("Mean Squared Error")
# 学习曲线是不同训练集大小，模型在训练集和验证集上的得分变化曲线
plt.title('Learning curves')
plt.legend(loc="best")
plt.xlim(0,N)

plt.show()

'''
Tip_120213 Sklearn-Random-Forest

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

X, y = make_classification(n_samples=1000,n_features=10,n_informative=3,n_redundant=0,
                          n_repeated=0,n_classes=2,random_state=0,shuffle=False)
print(X[:4])
print(y[:4])

# 随机森林随机分裂属性形成不同的决策树，然后取决策树的分类结果中分类最多的那一个作为最终结果
forest = ExtraTreesClassifier(n_estimators=250,random_state=0)
forest.fit(X, y)

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
    
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()

'''
Tip_120214 Sklearn-Isolation-Forest

Code:
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

# 产生训练数据集
X = 0.3 * rng.randn(100, 2)
X_train = np.r_[X + 2, X - 2]     
# 产生一些新的正常的数据点
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# 产生一些异常的新的数据点
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))

# 用一个随机超平面来切割数据空间，直到每个子空间里面只有一个数据点为止
# 密度很高的簇是被切分很多次才会停止切割，低密度的点很容易就停到一个子空间了
# 用于检测异常点
clf = IsolationForest(max_samples=100, random_state=rng)  #构建模型
clf.fit(X_train)     #模型训练
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)

xx, yy = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])  #注意这里要将xx和yy先进行ravel()
Z = Z.reshape(xx.shape)     #将Z的维度进行重构

plt.figure(figsize=(8,6))
plt.title("IsolationForest")
plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)  #画出检索边界，蓝色越深的区域表示异常区域

b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='white',s=30, edgecolor='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c='green',s=30, edgecolor='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='red',s=30, edgecolor='k')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([b1, b2, c],
           ["Training","New-Normal", "New-Abnormal"],
           loc="upper left")
plt.show()
