Shell脚本快速入门
====================

## 参考资料
- [Advanced Bash-Scripting Guide](http://tldp.org/LDP/abs/html/)，目前第10版
	- 详细易读，既可入门，亦工具书
	- [中文版](http://www.linuxplus.org/kb/)更新到第3.9.1版，[第10版翻译计划](https://github.com/LinuxStory/Advanced-Bash-Scripting-Guide-in-Chinese)夭折了
- [Unix Shell Programming](http://www.tutorialspoint.com/unix/unix-shell.htm)
- [Linux Shell Scripting Tutorial - A Beginner's handbook](http://bash.cyberciti.biz/guide/Main_Page)

## Shell脚本
- 示例

		#!/bin/sh
		cd ~
		mkdir shell_tut
		cd shell_tut
		for ((i=0; i<10; i++)); do
			touch test_$i.txt
		done
- 示例解释
	- 第1行：指定脚本解释器，这里是用/bin/sh做解释器的
	- 第2行：切换到当前用户的home目录
	- 第3行：创建一个目录shell_tut
	- 第4行：切换到shell_tut目录
	- 第5行：循环条件，一共循环10次
	- 第6行：创建一个test_0…9.txt文件
	- 第7行：循环体结束
- `mkdir`, `touch`都是系统自带的程序，一般在`/bin`或者`/usr/bin`目录下。`for`, `do`, `done`是`sh`脚本语言的关键字。

## 一些概念
- shell和shell脚本区别
	- shell是指一种应用程序
		- 这个应用程序提供了一个接口（interface）
		- 用户通过这个接口访问操作系统内核的服务
		- Ken Thompson的sh是第一种Unix Shell
		- Windows Explorer是一个典型的**图形界面Shell**，Windows cmd和powershell是命令行Shell
	- shell脚本（shell script），是一种为shell编写的脚本程序
		- 业界所说的shell通常都是指shell脚本
		- 但shell和shell script是两个不同的概念。由于习惯的原因，本文出现的“shell编程”都是指shell脚本编程，不是指开发shell自身（如Windows Explorer扩展开发）
- 开发环境
	- shell编程跟java、php编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了
	- 一般文本编译器要支持语法高亮、代码自动补全、语法纠错等特性
	- 常见的用于Shell开发的文本编辑器包括：Vim，Sublime等，eclispe之类的IDE也可以
- 运行环境
	- 当前主流的操作系统都支持shell编程
	- 本文所述的shell编程是指POSIX（Portable Operating System Interface）标准，适用于Linux、Unix及BSD（如Mac OS）
		- Linux默认安装就带了shell解释器
		- Mac OS不仅带了sh、bash这两个最基础的解释器，还内置了ksh、csh、zsh等不常用的解释器
		- windows出厂时没有内置posix shell解释器，需要安装[cygwin](http://www.cygwin.com)或者[mingw](http://www.mingw.org)来模拟linux环境

## 脚本解释器
- sh即Bourne shell，POSIX标准的shell解释器。
	- 它的二进制文件路径通常是/bin/sh，由Bell Labs开发。
- Bash是Bourne shell的替代品，更为通用，属GNU Project。
	- 二进制文件路径通常是/bin/bash。
	- 业界通常混用bash、sh、和shell，比如招聘运维工程师的文案：熟悉Linux Bash编程，精通Shell编程。
- 在大部分Linux系统（比如CentOS里），/bin/sh是一个指向/bin/bash的符号链接:

		[root@centosraw ~]# ls -l /bin/*sh
		-rwxr-xr-x. 1 root root 903272 Feb 22 05:09 /bin/bash
		-rwxr-xr-x. 1 root root 106216 Oct 17  2012 /bin/dash
		lrwxrwxrwx. 1 root root      4 Mar 22 10:22 /bin/sh -> bash
- 但在Mac OS上不是，/bin/sh和/bin/bash是两个不同的文件，尽管它们的大小只相差100字节左右:

		iMac:~ wuxiao$ ls -l /bin/*sh
		-r-xr-xr-x  1 root  wheel  1371648  6 Nov 16:52 /bin/bash
		-rwxr-xr-x  2 root  wheel   772992  6 Nov 16:52 /bin/csh
		-r-xr-xr-x  1 root  wheel  2180736  6 Nov 16:52 /bin/ksh
		-r-xr-xr-x  1 root  wheel  1371712  6 Nov 16:52 /bin/sh
		-rwxr-xr-x  2 root  wheel   772992  6 Nov 16:52 /bin/tcsh
		-rwxr-xr-x  1 root  wheel  1103984  6 Nov 16:52 /bin/zsh
- 高级编程语言
	- 理论上讲，只要一门语言提供了解释器（而不仅是编译器），这门语言就可以胜任脚本编程
		- 常见的解释型语言都是可以用作脚本编程的，如：Perl、Tcl、Python、PHP、Ruby
		- Perl是最老牌的脚本编程语言了，Python是后期之秀
	- 编译型语言，只要有解释器，也可以用作脚本编程
		- 如C shell是内置的（/bin/csh）
		- Java有第三方解释器Jshell
		- Ada有收费的解释器AdaScript
	- 如下是一个PHP Shell Script示例（假设文件名叫test.php）：

			#!/usr/bin/php
			<?php
			for ($i=0; $i < 10; $i++)
			        echo $i . "\n";
	
			# 执行
			# /usr/bin/php test.php
			# 或者
			# chmod +x test.php
			# ./test.php

## 如何选择shell编程语言
- 选熟悉的
	- 如果你已经掌握了一门编程语言（如PHP、Python、Java、JavaScript），就直接用
	- 虽然某些地方会有点啰嗦，但你能利用在这门语言领域里的经验（单元测试、单步调试、IDE、第三方类库）
	- 新增的学习成本很小，只要学会怎么使用shell解释器（Jshell、AdaScript）就可以了
- 选适合的
	- 如果只是想做一些备份文件、安装软件、下载数据之类的事情，学着使用sh，bash会是一个好主意
	- 如果你的脚本程序复杂度较高，或者要操作的数据结构比较复杂，还是应该使用Python、Perl这样的脚本语言，Bash功能有限，比如说：
		- 它的函数只能返回字串，无法返回数组
		- 它不支持面向对象，你无法实现一些优雅的设计模式
		- 它是解释型的，连PHP那种预编译都不是，如果脚本包含错误，只要没执行到这一行，就不会报错
- 环境兼容性
	- 如果你的脚本是提供给别的用户使用，使用sh或者bash，你的脚本将具有最好的环境兼容性
	- perl很早就是linux标配了，python这些年也成了一些linux发行版的标配
	- 至于mac os，它默认安装了perl、python、ruby、php、java等主流编程语言

## 第一个shell脚本
- 编写
	- 打开文本编辑器，新建一个文件，扩展名为sh（sh代表shell）
	- 扩展名并不影响脚本执行，见名知意就好，如果你用php写shell 脚本，扩展名就用php好了
	- 输入一些代码，第一行一般是这样：

			#!/bin/bash
			#!/usr/bin/php
	- “#!”是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行。
- 运行，运行Shell脚本有两种方法：
	- 作为可执行程序

			chmod +x test.sh
			./test.sh
		- 注意，一定要写成`./test.sh`，而不是`test.sh`
			- 运行其它二进制的程序也一样，直接写test.sh，linux系统会去PATH里寻找有没有叫test.sh的
			- 只有/bin, /sbin, /usr/bin，/usr/sbin等在PATH里，你的当前目录通常不在PATH里
			- 所以写成test.sh是会找不到命令的，要用./test.sh告诉系统说，就在当前目录找
		- 通过这种方式运行bash脚本，第一行一定要写对，好让系统查找到正确的解释器。
			- 这里的"系统"，其实就是shell这个应用程序（想象一下Windows Explorer），写成系统，是方便理解
			- 既然这个系统就是指shell，那么一个使用/bin/sh作为解释器的脚本是不是可以省去第一行呢？是的。
	- 作为解释器参数

			/bin/sh test.sh
			/bin/php test.php
		- 这种运行方式是，直接运行解释器，其参数就是shell脚本的文件名
		- 这种方式运行的脚本，不需要在第一行指定解释器信息，写了也会被忽略

## 变量
- **定义**变量时，变量名**不加美元符号`$`**，如：
	- `your_name="qinjx"`
	- 注意，变量名和等号之间**不能有空格**，这可能和你熟悉的所有编程语言都不一样
	- 除了显式地直接赋值，还可以用语句给变量赋值，如：```for file in `ls /etc` ```
- 使用变量
	- **使用**一个定义过的变量，只要在变量名前面**加美元符号`$`**即可，如：
	
			your_name="qinjx"
			echo $your_name
			echo ${your_name}
	- 变量名外面的花括号是可选的，**但请记得加上**，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况：
	
			for skill in Ada Coffe Action Java; do
				echo "I am good at ${skill}Script"
			done
	- 如果不给skill变量加花括号，写成`echo "I am good at $skillScript"`，解释器就会把`$skillScript`当成一个变量（其值为空），代码执行结果就不是我们期望的样子了。
	- 推荐给所有变量加上花括号，这是个好的编程习惯。IntelliJ IDEA编写shell script时，IDE就会提示加花括号。
- 重定义变量
	- 已定义的变量，可以被重新定义，如：

			your_name="qinjx"
			echo $your_name
			
			your_name="alibaba"
			echo $your_name
	- 这样写是合法的，但注意，第二次赋值的时候**不能写**`$your_name="alibaba"`，使用变量的时候才加美元符。

## 注释
- 以“#”开头的行就是注释，会被解释器忽略。
- sh里**没有多行注释**，只能每一行加一个#号。就像这样：

		#--------------------------------------------
		# 这是一个自动打ipa的脚本，基于webfrogs的ipa-build书写：https://github.com/webfrogs/xcode_shell/blob/master/ipa-build
		
		# 功能：自动为etao ios app打包，产出物为14个渠道的ipa包
		# 特色：全自动打包，不需要输入任何参数
		#--------------------------------------------
		
		##### 用户配置区 开始 #####
		#
		#
		# 项目根目录，推荐将此脚本放在项目的根目录，这里就不用改了
		# 应用名，确保和Xcode里Product下的target_name.app名字一致
		#
		##### 用户配置区 结束  #####
- 如果在开发过程中，遇到大段的代码需要临时注释起来，过一会儿又取消注释，怎么办呢？
	- 每一行加个#符号太费力了，可以把这一段要注释的代码用一对花括号括起来，定义成一个函数，没有地方调用这个函数，这块代码就不会执行，达到了和注释一样的效果
	- 用一个关爱开发者的IDE，用快捷键快速对大段代码注释/反注视，比如eclispe里的`ctrl+/`

## 字符串
- 字符串是shell编程中最常用最有用的数据类型（除了数字和字符串，也没啥其它类型好用了，哈哈）
- 字符串可以用单引号，也可以用双引号，也可以不用引号。单双引号的区别跟PHP类似。
- 单引号
	- `str='this is a string'`
	- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的
	- 单引号字串中不能出现单引号（对单引号使用转义符后也不行）
- 双引号
	
		your_name='qinjx'
		str="Hello, I know your are \"$your_name\"! \n"
	- 双引号里可以有变量
	- 双引号里可以出现转义字符

## 字符串操作
- 拼接字符串
	
		your_name="qinjx"
		greeting="hello, "$your_name" !"
		greeting_1="hello, ${your_name} !"
		
		echo $greeting $greeting_1
- 获取字符串长度：

		string="abcd"
		echo ${#string} #输出：4
- 提取子字符串

		string="alibaba is a great company"
		echo ${string:1:4} #输出：liba
- 查找子字符串

		string="alibaba is a great company"
		echo `expr index "$string" is` # 输出：3
		# 这个语句的意思是：找出字母i或者s在这个字符串中首次出现的位置
		# 要在linux下运行，mac下会报错，因为mac下的expr不支持这样计算
- 更多，参见本文档末尾的参考资料中[Advanced Bash-Scripting Guid Chapter 10.1](http://tldp.org/LDP/abs/html/string-manipulation.html)

## 数组
- 赋值
	
		array=(var1 var2 var3)
		array[0]=var1
		array[1]=var2
		output=(`shell command`) # 输出的行作为数组的元素 
- 求长度
	- `${#array[@]}` 
	- `${#array[*]}`
- 引用数组
	- `echo ${array[n]}`
- 连接数组
	- `arr3=(${arr1[@]} ${arr2[@]})`
- 遍历数组
	
		fl=(`ls`)
		for i in ${fl[@]};do
			echo ${i}
			done

## 管道

## 条件判断
- `==` is for string comparisons. `==` is a bash-specific alias for `=`
- `-eq` is for numeric ones. The same family as `-lt`, `-le`, `-gt`, `-ge`, and `-ne`
- `[[ "$x" == "$y" ]]`双括号护体 :-)，或者`[ "x$x" == "x$y" ]`，避免变量为空引起语法错误

## 流程控制
- 和Java、PHP等语言不一样，sh的流程控制不可为空
	- 如：

			<?php
			if (isset($_GET["q"])) {
				search(q);
			}
			else {
				//do nothing
			}
	- 在sh/bash里可不能这么写，如果else分支没有语句执行，就不要写这个else
- 还要注意，sh里的`if [ $foo -eq 0 ]`
	- 这个方括号跟Java/PHP里if后面的圆括号大不相同，它是一个可执行程序（和ls, grep一样）
	- 在CentOS上，它在/usr/bin目录下：

			ll /usr/bin/[
			-rwxr-xr-x. 1 root root 33408 6月  22 2012 /usr/bin/[
	- 正因为方括号在这里是一个可执行程序，方括号后面必须加空格，不能写成`if [$foo -eq 0]`
- 分支结构语法
	- `if`

			if condition
			then
				command1 
				command2
				...
				commandN 
			fi

	- 写成一行（适用于终端命令提示符）：```if `ps -ef | grep ssh`;  then echo hello; fi```
	- 末尾的`fi`就是`if`倒过来拼写，后面还会遇到类似的
	- `if else`
	
			if condition
			then
				command1 
				command2
				...
				commandN
			else
				command
			fi
	- if else-if else

			if condition1
			then
				command1
			elif condition2
				command2
			else
				commandN
			fi
- Switch结构语法
	- case

			case "${opt}" in
				"Install-Puppet-Server" )
					install_master $1
					exit
				;;
		
				"Install-Puppet-Client" )
					install_client $1
					exit
				;;
		
				"Config-Puppet-Server" )
					config_puppet_master
					exit
				;;
		
				"Config-Puppet-Client" )
					config_puppet_client
					exit
				;;
		
				"Exit" )
					exit
				;;
		
				* ) echo "Bad option, please choose again"
			esac
	- case语法需要一个esac（就是case反过来）作为结束标记，每个case分支用右圆括号，用两个分号表示break
- 循环结构语法
	- `for`
	
			for var in item1 item2 ... itemN
			do
				command1
				command2
				...
				commandN
			done
	- 写成一行：`for var in item1 item2 ... itemN; do command1; command2… done;`
	- C风格的for

			for (( EXP1; EXP2; EXP3 ))
			do
				command1
				command2
				command3
			done
	- while
	
			while condition
			do
				command
			done
	- 无限循环

			while :
			do
				command
			done

			# 或者
			while true
			do
				command
			done

			# 或者
			for (( ; ; ))
	- until

			until condition
			do
				command
			done

## 函数
- 定义
- 调用

## 文件包含
- 可以使用source和.关键字，如：
	- `source ./function.sh`
	- `. ./function.sh`
- 在bash里，source和.是等效的，他们都是读入function.sh的内容并执行其内容（类似PHP里的include）
- 为了更好的可移植性，推荐使用第二种写法。
- 包含一个文件和执行一个文件一样，也要写这个文件的路径，不能光写文件名
	- 比如上述例子中：`. ./function.sh`
	- 不可以写作：`. function.sh`
- 如果function.sh是用户传入的参数，如何获得它的绝对路径呢？方法是：

		real_path=`readlink -f $1`#$1是用户输入的参数，如function.sh
		. $real_path

## 用户输入
- 执行脚本时传入
- 脚本运行中输入
- select菜单

## stdin和stdout

## 常用的命令
- 字符处理领域，有grep、awk、sed三剑客
	- grep负责找出特定的行
	- awk能将行拆分成多个字段
	- sed则可以实现更新插入删除等写操作
- ps：查看进程列表
- grep
	- 排除grep自身
	- 查找与target相邻的结果
- awk
- sed
	- 插入
	- 替换
	- 删除
- xargs
- curl
- expr
	- ```COUNT=`expr ${COUNT} + 1` ```
	- `COUNT=$(expr ${COUNT} + 1)`

## 综合案例


