## 安装PyCharm

### 注意事项
- 本文是Pycharm的安装文档
- 适用于Win7 / Win10

### 安装步骤
- 安装Python，确认Python安装完成
	- 打开一个CMD窗口，运行`python --version`和`pip --version`可以看到正常版本信息
	- ![Python-Version.png](https://github.com/wu-wenxiang/Media-WebLink/raw/master/qiniu/9da5527f336948b59f2e5f195552cb61-Python-Version.png)
	- 如果没有安装，可以安装[纯净版Python](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Python.md)，或者[Anaconda](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Anaconda.md)，二者有其一即可
- 安装Pycharm
	- [下载页面](https://www.jetbrains.com/pycharm/download/#section=windows)，选择社区版
	- ![Pycharm-Download.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-Download.png)
	- 下载后一路默认安装，直至如下界面，勾选如下
	- ![Pycharm-Installation.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-Installation.png)
	- 安装完成后，首次打开Pycharm，会出现License说明，拖到最后，Accept就变成黑色，可以确认
	- ![Pycharm-License.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-License.png)
	- 之后就走到此页面，可以打开或者新建一个Python项目
	- ![Pycharm-Create.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-CreateProject.png)
- 创建项目
	- 在创建了第一个项目之后，如果还想创建`Project`，可以通过`File/New Project`创建
	- ![Pycharm-NewProject.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-NewProject.png)
	- 为方便起见，我们可以不使用默认的虚拟环境，而是直接指定系统的Python解释器（Anaconda中的Python，或者纯净版的Python）
	- ![Pycharm-Interpreter.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-Interpreter.png)
	- ![Pycharm-PythonPath.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-PythonPath.png)
- 在项目中创建Python文件
	- 创建完项目后，可以在项目上右键，创建Python文件
	- ![Pycharm-CodeName.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-NewPythonFile.png)
	- ![Pycharm-NewPythonFile.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-CodeName.png)
	- 然后在新建的文件中写上`print('hello, world!')`，运行代码
	- ![Pycharm-RunCode.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Pycharm-RunCode.png)