## 安装Anaconda

### 注意事项
- 本文是Anaconda的安装文档
- 适用的操作系统：Win7 / Win10

### 安装步骤
- 下载Anaconda
	- [下载页面](https://www.anaconda.com/download/#windows)，选择3版本
	- ![Anaconda-Download.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Anaconda-Download.png)
	- 这里要看你的操作系统是32bit还是64bit，可以通过`我的电脑 / 右键`查看，如果不会看就选32bit
	- ![OS-Arch.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-OS-Arch.png)
- 安装Anaconda 
	- 下载后可以开始安装，安装时一路**默认安装**，选安装路径的时候要记一下，不同的系统中安装路径不同
	- ![Anaconda-Install-Path.jpg](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-Anaconda-Install-Path.jpg)
- 配置环境变量
	- 比如，假设Anaconda默认会安装在`C:\ProgramData\Anaconda3`目录，将此目录添加到环境变量PATH
	- `我的电脑 / 空白处右键 / 属性 (Properties)`
	- `高级系统设置 (Advanced system settings)`
	- ![OS-Settings.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-OS-Settings.png) 
	- `环境变量 (Environment Variables)`
	- ![OS-Environment.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-OS-Environment.png)
	- 如果没有`PATH`这个环境变量，就新建一个
	- 然后将`C:\ProgramData\Anaconda3;C:\ProgramData\Anaconda3\Scripts;`添加到`PATH`环境变量开头，环境变量中的各个字符串用分号隔开。注意，这里假设Anaconda的安装路径是C:\ProgramData\Anaconda3。如果安装在其它路径，要相应地修改。
	- ![OS-Env-Var.png](https://raw.githubusercontent.com/wu-wenxiang/Media-WebLink/master/qiniu/bec937bdec704aee995f610566dcebb0-OS-Env-Var.png)
- 验证Anaconda安装完成
	- **重新打开**一个cmd窗口，运行：`python --version`
	- 出现：`Python 3.6.5 :: Anaconda, Inc.`，表示Python安装成功。
- [入门文档](http://docs.anaconda.com/anaconda/user-guide/getting-started/)
