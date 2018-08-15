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
- 概述：数据库系统的发展和架构 
- 数据库建模：需求分析、建模、E/R图
- 关系数据模型：E/R -> 关系数据库模式。关系、属性、函数依赖、范式
- 关系代数：关系代数表示抽象的关系计算。主要的计算：投影、选择、笛卡尔积、连接
- 数据库语言SQL：使用SQL语言来建立数据库并实现关系计算。查询(更新)语句->关系运算
- SQL约束和触发器：如何用SQL实现各种约束条件，包括触发器
- SQL系统特性：如何用SQL事务保证数据完整性，如何通过用户授权和访问控制来保证数据库的安全性

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
	- 结构图：
	
			                                                  /--- 事务处理器
			查询(Select)                  -----\              /        |             
			模式更新(Create/Alter/Drop)    -----| --- 查询处理器 --- 存储管理器 --- 数据/元数据
			数据更新(Insert/Delete/Update) -----/       
	- 存储管理器：对数据读写进行管理，包含文件管理和缓冲区管理。依赖于特定OS。
		- 文件file管理：磁盘文件分块block：1K---16K 
		- 缓冲区buffer管理：文件到内存的映像。内存分页page：1K---4K 
	- 查询处理器：SQL命令预处理，把SQL命令转变为对存储数据的操作序列，主要问题是优化。 
	- 事务管理器：负责系统数据的完整性。保证并发运行的多个SQL命令相互不冲突；保证系统出现故障时不丢失不损坏数据。延迟和操作日志log。    
- **[概述] 数据和元数据指什么？索引是什么？**
	- 数据和元数据存储在数据文件中
	- 元数据metadata：关于数据的结构的信息
	- 数据按元数据规范的格式存储
	- 索引index是一种数据结构，用于快速查找数据项(item)
	- 索引是数据的一部分，而对索引的说明则是元数据的一部分
	- Hash表是早期建立索引的主要方法，现一般使用B(Balance)树
- **[概述] 什么是事务？**
	- 一组操作作为一个单元，按次序全部执行，称为事务Transaction。 
	- 事务的特性：ACID
		- Atomicity：原子性，一个事务中的一组操作，要么全部执行，要么一点也不执行
		- Consistency：一致性，保持正确状态
		- Isolation：隔离性，多个事务并发运行时，作用效果相互分开。有一定隔离级别
		- Durability：持久性，事务完成后，即使系统发生故障，事务的结果不丢失
	- 通过加锁(locking)，日志(logging)和提交(commit)保持事务特性
- **[概述] 什么是模式？**
	- 模式(schema)是对某个数据库的逻辑结构的完整描述，通常用一组DDL来描述
	- 结构图
	
			外模式1 -----\              
			外模式2 -----| --- 模式 --- 内模式
			外模式3 -----/             
	- 外模式：也被称为子模式、用户模式，视图应用相关的局部特征
	- 模式：公共逻辑结构
		- 表（属性、外键、索引、触发器）
		- 过程与函数
		- 用户和组等
	- 内模式：物理结构与存储方式的内部表示
		- Hash表
		- B树索引
		- 压缩
		- 加密
	- 数据独立性依靠模式分级及模式之间的映射实现
- [概述] 数据库应用客户/服务器(Client/Server,C/S)结构
	- 客户端Client：请求SQL服务的软件进程。Java / C++ / Python
	- 服务器Server：提供SQL服务的软件进程（MySQL / PostGre / Oracle）。一个服务器可支持多个数据库；一个数据库包含多个关系
- [概述] 我们需要掌握什么技术？
	- 设计design：如何建立一个有用的数据库。需求分析，数据建模，关系设计。 
	- 编程programming：在数据库设计基础上，如何进行各种查询和计算操作。 
- **[建模] 什么是E/R图？**
	- Entity/Relationship图，简称E/R图，一种传统的图形化数据库建模语言。E/R模型。 
	- E/R图的主要建模元素 ：
		- 实体集entity set：与类class相对应。描述名称。矩形表示。 
		- 属性attribute：描述实体某一个性质的值。只描述名称，不描述类型。椭圆表示。 
		- 联系relationship：两个或多个实体集之间的连接关系。通常需要描述名称。菱形表示。 
	- ![DB-ER.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/fd830d9d700c495b9cf39be3fe17c1c6-DB-ER.png)
- [建模] 设计一个仓库管理的ER模型
	- 需求分析
		- 仓库主要管理零件(Part)的入库、出库和采购等事项。
		- 仓库根据需要向外面厂家(Supplier)订购零件。
		- 而许多工程项目(Project)需要仓库供应零件。 
	- 工程项目的属性：项目编号，项目名称，项目开工日期。
	- 零件的属性：零件编号，零件名称，规格，颜色，重量。
	- 供应厂家的属性：工厂编号，工程名称，工程地址。
- **[建模] 什么是ER联系的多重性？**
	- 多重性是实体之间存在的定量的约束关系。 
	- 本质上区分为两种多重性：
		- 1：关联零个或一个实体，“最多一个” 
		- 多：关联零个到多个实体，“能超过一个”
	- 组合起来，考虑实体集A到B的联系：
		- 1对1：A的一个实体对应B的零个或一个实体；且B的一个实体对应A的零个或一个。 
		- 1对多：A的一个实体对应B的零个到多个实体；而B的一个实体对应A的零个或一个。（多对1是1对多的逆联系）  
		- 多对多：A到B是1对多、且B到A也是1对多。
	- 有箭头所指的实体集为1；无箭头所连接的实体集为多
- [建模] 什么是多元联系？
	- 一个联系涉及两个以上的实体集，该联系就是多元联系。通常是三元联系。
	- ![DB-ER-Multi.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/fd830d9d700c495b9cf39be3fe17c1c6-DB-ER-Multi.png)
	- Contracts是一个三元联系，表示一个制片公司和一个影星签约以参演某一部电影。
	- 一个联系可表示为一个三元组：(studio, star, movie) 
	- 三元联系中的多重性是如何确定：实体集A和B先分别确定一个实体，判断联系的C的实体是一个还是多个。 
- **[建模] 什么是联系中的角色？**
	- 在一种联系中，一个实体相对于被关联的其它实体的职责。
	- 当两个不同实体集之间建立一种联系时，假定双方实体集的名称作为各自角色。 
	- 当一个实体集自身存在某种联系时，就需要确定联系的双方实体所扮演的不同角色。 
	- ![DB-ER-Role.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/fd830d9d700c495b9cf39be3fe17c1c6-DB-ER-Role.png)
	- ![DB-ER-Role-2.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/fd830d9d700c495b9cf39be3fe17c1c6-DB-ER-Role-2.png)
- **[建模] xx**
- [建模] xx

