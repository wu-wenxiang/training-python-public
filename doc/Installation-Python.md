## Python安装

### 注意事项

- 本文描述了纯净版 Python 开发环境的安装和配置过程
- Python3 只支持 Windows 7 SP1 以上版本
- 如果是 XP 或者 Win7 RTM，只能安装 Python2
- Python 安装包的[下载地址](https://www.python.org/downloads/)

### 安装步骤

- 安装 Python，注意勾选 `Add Python to PATH`，如果选 `Install Now` 会安装到个人 Roaming 目录下。若不希望安装到个人 Roaming
  目录，可以选下方的 `Customize Installation`

  ![Install-Python.png](images/9da5527f336948b59f2e5f195552cb61-Install-Python.png)

  如果选了 `Customize Installation`，接着选 `Install for all users`，会默认将 Python 安装到 `C:\Program Files` 目录下

  ![](images/python-install-all-users.png)

- **重新**打开一个 CMD 窗口，验证 Python 是否装好，运行命令：`python --version` 和 `pip --version`

  ![Python-Version.png](images/9da5527f336948b59f2e5f195552cb61-Python-Version.png)
