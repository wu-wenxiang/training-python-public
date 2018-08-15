## Database Installation & Config
- MySQL
	- [How To Install MySQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
	
			sudo apt-get update
			sudo apt-get upgrade -y 
			sudo apt install mysql-server
			sudo mysql_secure_installation # 全选No
	- 远程访问，需要修改下配置文件，binding到`0.0.0.0:3306`，再打开防火墙
	- 重启服务，发现本地root账户不能登陆，可以参考[这里](https://blog.csdn.net/qq_34771403/article/details/73927962)
		- 先su到root，然后mysql，就可以登进去
		- 然后运行如下命令，重启服务
		
				mysql> update mysql.user set authentication_string=PASSWORD('newPwd'), plugin='mysql_native_password' where user='root';
				mysql> flush privileges;
	- 此时再参考[这里](https://blog.csdn.net/leroy008/article/details/16116847)，令远程也能访问
		- `GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'newPwd' WITH GRANT OPTION;`
	- phpmyadmin
		- `sudo apt-get install phpmyadmin `
		- 访问: `http://65.52.172.145/phpmyadmin/`
- PostGre
	- [参考](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
- Sqlite3

## 目录
- 概述
	- 数据库系统的发展 
	- 数据库管理系统的结构 
- 数据库建模
- 关系数据模型
- 关系代数
- 数据库语言SQL
- SQL约束和触发器
- SQL系统特性

## 自测题
- **[概述] 什么是数据库？** 
	- 一个数据库是由一个数据库管理系统(DBMS, Database Management System)所管理的一个数据集合。
- **[概述] 一个DBMS主要为用户提供什么功能？** 负责数据库存取、维护和管理
	- 持久存储
		- 数量大
		- 持续时间长
	- 用户接口和编程接口
		- 数据定义语言和模式
		- 数据查询语言，数据操作语言
		- 数据共享，并发控制，容错
	- 事务管理
- **[概述] 什么是DDL和schema？** 
	- 数据定义语言(DDL,Data Definition Language)：创建数据库并确定其模式(schema)
	- 一个schema模式是一组用DDL表达的语句集合，以完整描述某个数据库的逻辑结构
- **[概述] 什么是数据查询和操作语言？** 
	- 数据查询语言(Data Query Language)
	- 数据操作语言(Data Manipulation Language)
	- 依据数据库的模式，查询或更新数据。
- **[概述] 数据库对数据共享要注意什么？**
	- 多用户并发访问，避免某用户的动作影响其他人
	- 避免意外（并发竞争/物理故障）损坏数据
- [概述] 数据库由文件系统演化而来，文件系统有什么特点，有什么缺点？
	- 特点
		- 数据以文件的形式长期保存
		- 数据的物理结构与逻辑结构可以不一致
		- 文件形式多样化
		- 数据的存取以记录为单位
	- 缺点
		- 数据冗余度(Redundancy)大：数据面向应用，无法共享，比如pdf格式的文件只能被pdf软件打开
		- 数据和程序彼此耦合，缺乏独立性
- [概述] 关系型数据库的发展历史节点和契机是什么？
	- 时间：60年代后期
		- 背景：数据管理规模更为庞大，应用更广泛，数据量剧增，共享要求(多种应用、多种语言互相覆盖地共享数据集合)更强
		- 硬件：有了大容量和快速存取磁盘
		- 指导思想：对所有的数据实行统一的、集中的、独立的管理，使数据存储独立于使用数据的程序，实现数据共享。
	- 时间：1970年，Ted Codd在ACM发表“A Relational Model for Large Shared Data Banks”，奠定了关系型数据库的理论基础。
		- 主要思想是把数据库中的所有数据组织为“表table”的“关系relation”。
		- 可组织复杂数据结构；对大量查询能快速反应；查询可表示为一种高级语言，以提高编程效率。 
		- 关系代数提供了关系模型的数学基础。 
		- 使用简单的结构和方法可表示和实现复杂结构和复杂计算。 
		- SQL(Structural Query Language)出现。
- [概述] 数据模型的作用是什么？ 
	- 数据库不仅反映数据本身的内容，同时也反映数据之间的关系
	- 在数据库中是用数据模型来对现实世界进行抽象的
	- 数据模型是数据库系统中用于提供信息表示和操作手段的形式架构
- **[概述] 数据库系统的结构是怎样的？**
	
		
		App1 -----\              /----- DB1
		App2 -----| --- DBMS --- |
		App3 -----/              \----- DB2
- **[概述] 数据库系统构建和数据处理是怎样的？**

		                                                  /--- 事务处理器
		查询(Select)                  -----\              /        |             
		模式更新(Create/Alter/Drop)    -----| --- 查询处理器 --- 存储管理器 --- 数据/元数据
		数据更新(Insert/Delete/Update) -----/           
- **[概述] 数据和元数据指什么？索引是什么？**
	- 数据和元数据存储在数据文件中
	- 元数据metadata：关于数据的结构的信息
	- 数据按元数据规范的格式存储
	- 索引index是一种数据结构，用于快速查找数据项(item)
	- 索引是数据的一部分，而对索引的说明则是元数据的一部分
	- Hash表是早期建立索引的主要方法，现一般使用B(Balance)树
- **[概述] 数据库系统的结构是怎样？**

