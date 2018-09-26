## Eclipse+Pydev

### 注意事项
- 本文描述了`Eclipse+Pydev`IDE开发环境的安装和配置过程。
- 本文用到的软件都可以在[这里](http://url.cn/52g5jKH)下载
	- Java
	- Eclipse
	- Pydev

### 安装步骤：
- 安装Python，确认Python安装完成，[参考](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Python.md)
- 安装Java
	- 下载Java，至少1.8以上，一路默认安装
	- ![Install-Java.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Install-Java.png)
	- 验证Java是否装好，**重新**打开一个CMD窗口，运行命令：`java -version`
	- ![Java-Version.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Java-Version.png)
- 安装Eclipse
	- 安装Eclipse，解压缩Eclipse，解压缩Pydev，将Pydev下的两个目录，复制到eclipse目录下，覆盖同名目录
	- ![Install-Pydev.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Install-Pydev.png)
	- 然后Eclipse就应该可以正常打开了，关闭欢迎页面。
	- 然后配置Pydev，Window / Preference / Pydev / Interpreters / Python Interpreter，可以直接选Quick Auto Config，完成自动配置。如果自动配置不成功，可以选New，然后选择Python的安装目录。
	- ![Config-Eclispe-Interpreter.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Config-Eclispe-Interpreter.png)
	- 验证Eclipse是否装好，File / New / Project / Pydev / Pydev Project 
	- ![Eclispe-Project.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Eclispe-Project.png)
	- ![Eclispe-Run.png](https://github.com/wu-wenxiang/Media-WebLink/blob/master/qiniu/9da5527f336948b59f2e5f195552cb61-Eclispe-Run.png) 