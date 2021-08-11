# Python 自动化测试

- 授课时长：
    - 上午：9:00 至 12:00
    - 下午：13:30 至 17:30
- Prerequisite
    - 有计算机语言编程基础
    - 了解 API 测试的基本概念
    - 掌握一种 IDE，比如 VSCode（Remote Plugin）

## 1. 基本概念

### 1.1 软件测试分几类？

- 白盒测试：
    - 单元测试
    - 数据库测试
- 黑盒测试：
    - 功能测试
        - 接口测试（功能测试 / 集成测试）
        - E2E 测试（UI 界面）
    - 非功能测试
        - 压力测试
        - 可靠性 / 恢复测试 
        - 伸缩性测试
        - 安全测试

### 1.2 敏捷开发为测试带来了什么挑战？

- 为什么敏捷开发（FullStack）的测试是不够的？敏捷的原则是：功能刚好够用 + 快速迭代 => 随时可交付
- [测试应该在什么阶段介入？]((https://www.softwaretestinghelp.com/maximizing-quality-beyond-full-stack-testing/))

    ![](images/testing-stages.png)

## 2. 单元测试

[Python 单元测试](http://blog.wuwenxiang.net/Python-Unittest)

- Unittest & Green：反射、固件测试、Mock
- Pytest & allure：Assert Error

## 3. 数据库操作

[Demo](python-exec-public.py)：

- DB Driver
- SqlAlchemy ORM 模型
- Pandas 快速处理

## 4. 接口测试

### 4.1 基本概念

- [什么是 Restful API 设计？](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
    - 客户端-服务器约束：用户界面问题与数据存储分开
    - 无状态约束：会话状态完全保留在客户端
    - [统一接口约束](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_2)
- [如何判断服务是否以正确的值响应？](https://restfulapi.net/http-status-codes/)
    - 200 / 201 / 204
    - 400 / 401 / 403 / 419
    - 500 / 503
- Restful API 和 GRPC 接口的自动化测试有哪些异同？gRPC 提供了许多优势，但它有一个主要障碍：浏览器兼容性低。因此，gRPC 的用例一般局限在内部/私有系统

    ![](images/testing-gRPC-vs-RestAPI.jpeg)

- Rest API Demo：[Github](https://github.com/wu-wenxiang/rest_api_demo) & [Gitee](https://gitee.com/wu-wen-xiang/rest_api_demo)，对象s + CRUD    

### 4.2 常见工具

- Netmon / Wireshark / tcpdump
- Fiddler
- Postman

### 4.3 Requests

### 4.4 Pytest & Requests

### 4.5 Tempest

### 4.6 RobotFramwork

[Github](https://github.com/wu-wenxiang/training-python-public/blob/master/doc/TailoredTraining-Python-RobotFrameWork.md#lab-07-robotframework) 或 [Gitee](https://gitee.com/wu-wen-xiang/training-python/blob/master/doc/TailoredTraining-Python-RobotFrameWork.md#lab-07-robotframework)

## 5. E2E 测试

### 5.1 Python & Selenium

### 5.2 Cypress

## 6. 压力测试

检测指标

- 并发数
- 响应时间：3 秒 - 30 秒

### 6.1 工具 JMeter

### 6.2 Rally

## 7. 容错测试

## 8. CI/CD

### 8.1 Jenkins

### 8.2 Zuul

### 8.3 Gitlab

### 8.4 Gerrit
