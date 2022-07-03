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

### 1.2 Python 和系统运维

[返回目录](#课程目录)

系统运维语言：Bash & Python

#### 1.2.1 Bash

[bash 编程快速入门](shell-quick-start.md)

#### 1.2.2 Python

[Python 入门](we-know-python.md)

对于系统运维，你应该掌握的 Python 知识：

- 选择和安装合适的 Python 版本：老系统上如何安装支持版本的 Python？
- IDE 编辑和远程调试：如何方便地修改和调试远程服务器上的 Python？
- 基础语法：分支结构、循环、函数、类、异常处理
- 基本对象类型和数据结构：变量和对象、数字、字符串（正则表达式）、元组、列表、集合、字典
- 与 Bash 交互：`-c`，`sys.argv`，`os.system`，`subprocess.check_output`，标准输入输出重定向
- 文件和目录：目录遍历、临时文件
- 数据库：SqlAlchemy
- Web 客户端：requests、json
- 其它客户端：mail / ssh / office 等

##### 1.2.2.1 Python 安装和调试

参考：[Github](https://github.com/wu-wenxiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#111-%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7) 或 [Gitee](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/main/doc/kubernetes-best-practices.md#111-%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7)

> 作业：升级内核到 5.4，升级 Python 到 3.8

### 1.3 容器技术和自动化运维

[返回目录](#课程目录)

### 1.4 K8S 和自动化运维

[返回目录](#课程目录)

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
