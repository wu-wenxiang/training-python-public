# 自动化运维在容器化场景中的最佳实践

## 注意 ⚠️

- _斜体表示引用_
- **未经允许，禁止转载**

## Prerequisite

- 熟悉 Linux 系统的基本配置和命令
- 了解或使用过 Python 更佳

## 课程目录

| 日程    | 时间 | 课程              | 内容                                     |
| ----- | -- | --------------- | -------------------------------------- |
| 第 1 天 | 上午 | [运维基础](#1-运维基础) | [1.1 自动化运维概述](#11-自动化运维概述)       |
|       |    |                 | [1.2 Python 和系统运维](#12-python-和系统运维)   |
|       | 下午 |                 | [1.3 容器技术和自动化运维](#13-容器技术和自动化运维)       |
|       |    |                 | [1.4 K8S 和自动化运维](#14-k8s-和自动化运维)       |
| 第 2 天 | 上午 | [配置管理](#2-配置管理) | [2.1 Ansible 基础](#21-ansible-基础)       |
|       |    |                 | [2.2 Ansible 和容器技术](#22-ansible-与容器技术) |
|       | 下午 |                 | [2.3 Ansible 与云平台](#23-ansible-与云平台)   |
|       |    |                 | [2.4 其它自动化框架](#24-其它自动化框架)             |
| 第 3 天 | 上午 | [任务管理](#3-任务管理) | [3.1 Jenkins](#31-jenkins)             |
|       |    |                 | [3.2 Zuul](#32-zuul)                   |
|       | 下午 |                 | [3.3 Drone](#33-drone)                 |
|       |    |                 | [3.4 CI-CD](#34-ci-cd)                 |
| 第 4 天 | 上午 | [监控计量](#4-监控计量) | [4.1 监控框架对比](#41-监控框架对比)               |
|       |    |                 | [4.2 Promtheus](#42-prometheus)        |
|       |    |                 | [4.3 Alertmanager](#43-alertmanager)   |
|       |    |                 | [4.4 Grafana](#44-Grafana)             |
|       | 下午 | [日志分析](#5-日志分析) | [5.1 Fluentd](#51-Fluentd)             |
|       |    |                 | [5.2 ElasticSearch](#52-ElasticSearch) |
|       |    |                 | [5.3 Kibana](#53-Kibana)               |
|       |    |                 | [5.4 其它的日志收集和分析方案](#54-其它的日志收集和分析方案)   |

## 1. 运维基础

[返回目录](#课程目录)

### 1.1 自动化运维概述

[返回目录](#课程目录)

当我们讨论“自动化运维”，我们在讨论什么？

- 数据中心自动化（DCA）？
- 开发运营一体化（DevOps）？

Redhat 对“自动化运维“的定义：[*the use of software to create repeatable instructions and processes to replace or reduce human interaction with IT systems.*](https://www.redhat.com/en/topics/automation/whats-it-automation) **使用软件创建可重复的指令和过程，以取代或减少与 IT 系统的人机交互。自动化软件在这些指令、工具和框架的限制下工作，以执行任务，几乎不需要人工干预**。

自动化运维包括：

- **自动化**
    - 应用的自愈
    - 资源的自动弹性缩放
    - 无人工干预下的安装部署
    - 不影响业务的升级和回滚
    - 自服务化的资源和权限获取
    - 基于机器学习的监控、日志分析、告警和预警
- **配置管理**
- **监控**

自动化应用于：

- **基础设施即代码**：通过自动化代码在各类基础设施平台（依据各类模版）管理资源
- **配置管理**：应用所需的配置（不同的设置、文件系统、端口、用户等等）
- **应用编排**：应用可能会被部署在不同的云平台上
- **IT 迁移**：数据或软件从一个系统（操作系统、云平台）转移到另一个系统
- **安全与合规**：流程标准化与审计

未来的自动化形态：

- *From bare metal to middleware, apps, security, updating, notifications, failover, predictive analytics, and decisions being made with no direct oversight.* 从裸机到中间件的自动化、应用程序、安全性、更新、通知、故障切换、预测分析，以及在没有直接监督的情况下做出的决策。
- *A security risk being automatically detected, reported, patched, tested, and deployed while your IT staff are asleep. Your system could self-heal, gather relevant information to discover if and where an attack came from, notify the correct people—all without losing uptime.* 在 IT 员工睡觉时自动检测、报告、修补、测试和部署安全风险。您的系统可以自我修复，收集相关信息以发现攻击是否以及来自何处，并在不损失正常运行时间的情况下通知所有相关的人。

**自动化运维技术栈**：

- Linux 基础：bash / vim / systemd
- 企业级应用服务管理：文件服务 / Web 服务 / DNS 等
- 流程管理：版本控制 / review / 任务管理 / 工单系统 / 制品仓库
- 中间件服务：数据库、缓存、消息队列、LB、VIP、Cluster
- 云平台：OpenStack / KVM / EXSI / K8S / Docker
- 运维框架：Ansible / Fabric / Puppet / Chef
- 监控和日志： Zabbix / SkyWalking / GAP / EFK
- 编程：Python / Java / Web Service Framwork
- 数据分析和机器学习：Numpy / Pandas / Sklearn / TF / PyTorch

运维技术的判断标准：八荣八耻

- 以可配置为荣，以硬编码为耻
- 以互备为荣，以单点为耻
- 以随时重启为荣，以不能迁移为耻
- 以整体交付为荣，以部分交付为耻
- 以无状态为荣，以有状态为耻
- 以标准化为荣，以特殊化为耻
- 以自动化工具为荣，以手动和人肉为耻
- 以无人值守为荣，以人工介入为耻

### 1.2 Python 和系统运维

[返回目录](#课程目录)

#### 1.2.1 无处不在的 Bash

[返回目录](#课程目录)

[bash 编程快速入门](shell-quick-start.md)

- 作业：[字符串处理、流程控制、数值计算](/src/automation/automation.sh)

#### 1.2.2 简单强大的 Python

[返回目录](#课程目录)

##### 1.2.2.1 Windows 环境中 Python 安装和调试

[返回目录](#课程目录)

参考：[Python 安装](Installation-Python.md)

- 作业：部署完成 Python

    ```console
    $ python --version
    Python 3.9.7

    $ pip --version
    pip 22.0.3 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)

    $ python
    Python 3.9.7 (default, Sep  3 2021, 12:37:55)
    [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    ```

    ```python
    >>> print(2**64)
    18446744073709551616

    >>> print('hello, world')
    hello, world

    >>> exit()
    ```

参考：[VSCode 部署](Installation-VSCode.md)

- 作业：VSCode 对 Python 程序进行断点调试

##### 1.2.2.2 Linux 环境中 Python 安装和调试

[返回目录](#课程目录)

**基础环境安装**，参考：[Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#111-%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#111-%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7)

- 作业：升级内核到 5.4
- 作业：升级 Python 到 3.8
- 作业：升级 Git 到 2 版本

**VSCode 安装 Remote 插件**

- 作业：VSCode 远程访问 Linux 服务器上的代码

**[virtualenv 环境](https://pypi.org/project/virtualenv)

```bash
python -m pip install virtualenv
```

```console
$ python -m virtualenv --version
virtualenv 20.7.0 from /usr/local/lib/python3.9/site-packages/virtualenv/__init__.py

$ python -m virtualenv .venv
created virtual environment CPython3.9.7.final.0-64 in 869ms
  creator CPython3Posix(dest=/Users/wuwenxiang/local/github-99cloud/lab-openstack/.venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/wuwenxiang/Library/Application Support/virtualenv)
    added seed packages: pip==22.1.2, setuptools==62.2.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator

$ . .venv/bin/activate

(.venv) $ python --version
Python 3.9.7

(.venv) $ pip --version
pip 22.1.2 from /Users/wuwenxiang/local/github-99cloud/lab-openstack/.venv/lib/python3.9/site-packages/pip (python 3.9)
```

##### 1.2.2.3 Python 和自动化运维

[返回目录](#课程目录)

参考：[Python 入门](we-know-python.md)

对于自动化运维，你应该掌握的 Python 知识：

- 基础语法：分支结构、循环、函数、类、异常处理
- 基本对象类型和数据结构：变量和对象、数字、字符串（正则表达式）、元组、列表、集合、字典
- 与 Bash 交互：`-c`，`sys.argv`，`os.system`，`subprocess.check_output`，标准输入输出重定向
- 文件和目录：目录遍历、临时文件
- 数据库：SqlAlchemy
- Web 客户端：requests、json
- 其它客户端：mail / ssh / office 等
- 系统相关模块：psutil / IPy 等

作业：

1. [文件和字符串处理](python-exec-public.py#L628-666)
1. [数据库相关](python-exec-public.py#L1669-2010)
1. [Excel 处理](python-exec-public.py#L2377-2407)
1. [系统相关模块](python-exec-public.py#L2086-2375)
1. [文件目录、子进程、FTP、SSH](/src/automation/automation.py)
1. [XML 解析](python-exec-public.py#L2012-2074)
1. [结构化数据爬取](python-exec.py)
1. [非结构化数据爬取](python-exec-public.py#L1483-1511)
1. [科学计算和机器学习](python-exec-public.py#L2445-3195)

### 1.3 容器技术和自动化运维

[返回目录](#课程目录)

#### 1.3.1 Linux 容器和 Docker

[返回目录](#课程目录)

参考：[Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#211-linux-%E5%AE%B9%E5%99%A8%E5%92%8C-docker) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#211-linux-%E5%AE%B9%E5%99%A8%E5%92%8C-docker)

- 作业：安装 Docker
- 作业：熟悉 Docker 命令

#### 1.3.2 Docker 和 Containerd

[返回目录](#课程目录)

参考 [Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#22-containerd) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#22-containerd)

- 作业：安装 Containerd
- 作业：熟悉 crictl / ctr / nerdctr 命令

### 1.4 K8S 和自动化运维

[返回目录](#课程目录)

#### 1.4.1 K8S 部署

[返回目录](#课程目录)

组件和基本架构，参考：[Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#3-k8s-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E7%AE%A1%E7%90%86) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#3-k8s-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E7%AE%A1%E7%90%86)

部署单节点 K8S，参考：[Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#3111-%E5%8D%95%E8%8A%82%E7%82%B9%E9%9B%86%E7%BE%A4%E9%83%A8%E7%BD%B2) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#3111-%E5%8D%95%E8%8A%82%E7%82%B9%E9%9B%86%E7%BE%A4%E9%83%A8%E7%BD%B2)，注意：Containerd 如果已经部署好的话，前面部署 Containerd 的步骤可以跳过，直接部署 K8S 即可。

- 作业：完成 K8S 单节点部署

#### 1.4.2 降应用部署到 K8S

参考：[Github](http://github.com/99cloud/training-kubernetes/blob/master/doc/class-01-Kubernetes-Administration.md#29-%E5%90%AF%E5%8A%A8%E4%B8%80%E4%B8%AA-pod) 或 [Gitee](https://gitee.com/dev-99cloud/training-kubernetes/blob/master/doc/class-01-Kubernetes-Administration.md#29-%E5%90%AF%E5%8A%A8%E4%B8%80%E4%B8%AA-pod)

- 作业：完成 K8S 应用部署和发布

## 2. 配置管理

[返回目录](#课程目录)

### 2.1 Ansible 基础

[返回目录](#课程目录)

### 2.2 Ansible 和容器技术

[返回目录](#课程目录)

### 2.3 Ansible 与云平台

[返回目录](#课程目录)

### 2.4 其它自动化框架

[返回目录](#课程目录)

## 3. 任务管理

[返回目录](#课程目录)

### 3.1 Jenkins

[返回目录](#课程目录)

### 3.2 Zuul

[返回目录](#课程目录)

### 3.3 Drone

[返回目录](#课程目录)

### 3.4 CI/CD

[返回目录](#课程目录)

## 4. 监控计量

[返回目录](#课程目录)

### 4.1 监控框架对比

[返回目录](#课程目录)

### 4.2 Promtheus

[返回目录](#课程目录)

### 4.3 Alertmanager

[返回目录](#课程目录)

### 4.4 Grafana

[返回目录](#课程目录)

## 5. 日志分析

[返回目录](#课程目录)

### 5.1 Fluentd

[返回目录](#课程目录)

### 5.2 ElasticSearch

[返回目录](#课程目录)

### 5.3 Kibana

[返回目录](#课程目录)

### 5.4 其它的日志收集和分析方案

[返回目录](#课程目录)
