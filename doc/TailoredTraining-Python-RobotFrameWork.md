# Python Training in 2 Days

## Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 课前准备 | N/A | [lab-00 Python Environment](lab-00-python-environment) | [Python Installation](python-installation) |
| | | | [IDE Configuration](ide-configuration) |
| 第 1 天 | 上午 | [lab-01 Python Basic](lab-01-python-basic) | [Quick Start](quick-start) |
| | | | [Data Structure](data-structure) |
| | | | [Functions](functions) |
| | | [lab-02 Common Usage Modules](lab-02-common-usage-modules) | [OS/SYS](os/sys) |
| | 下午 | | [I/O](i/o) |
| | | [lab-03 Object Oriented](lab-03-object-oriented) | [Class & Instance](class--instance) |
| | | | [Operator Overloading](operator-overloading) |
| | | | [Inheritance & Composition](inheritance--composition) |
| 第 2 天 | 上午 | [lab-04 Scientific Computation Modules](lab-04-scientific-computation-modules) | [Numpy & Pandas](numpy--pandas) |
| | | | [Scipy & SkLearn](scipy--sklearn) |
| | | | [Matplotlib](matplotlib) |
| | | [lab-05 Pythonic Code Style](lab-05-pythonic-code-style) | [Functional Programming](functional-programming) |
| | | | [Iterator & Generator](iterator--generator) |
| | | | [PEP8](pep8) |
| | 下午 | [lab-06 Other Categories](lab-06-other-categories) | [Parallel Process](parallel-process) |
| | | | [Debug](debug) |
| | | | [Decorator](decorator) |
| | | | [Memory Management](memory-management) |
| | | | [Timeme & Space Complexity](timeme--space-complexity) |
| | | [lab-07 RobotFrameWork](lab-07-robotframework) | [Quick Start](quick-start) |
| | | | [Demo](demo) |

    import re
    reCmp=re.compile('^\s*#+\s+(.+)$')
    aList = [reCmp.search(i).groups()[0].strip() for i in aStr.split('\n') if reCmp.search(i)]
    bList = [(i, '-'.join(i.split()).lower().replace('&','')) for i in aList]
    template = '| | | | [%s](%s) |'
    print('\n'.join(template % i for i in bList))

## lab-00 Python Environment

### Python Installation
- **推荐**：[单独安装 Python](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Python.md)，3.7 版本
- 其它选项：
    - [Anacoda（ 包含Python ）](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Anaconda.md)，3.7 版本

### IDE Configuration
- **推荐**：[Eclipse+Pydev](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-Eclipse-Pydev.md)
- 其它选项：
    - [VS Code](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-VSCode.md)
    - [PyCharm](https://github.com/wu-wenxiang/Training-Python-Public/blob/master/doc/Installation-PyCharm.md)

## lab-01 Python Basic

### Quick Start

### Data Structure

### Functions

## lab-02 Common Usage Modules

### OS/SYS

### I/O

## lab-03 Object Oriented

### Class & Instance

### Operator Overloading

### Inheritance & Composition

## lab-04 Scientific Computation Modules

### Numpy & Pandas

### Scipy & SkLearn

### Matplotlib

## lab-05 Pythonic Code Style

### Functional Programming

### Iterator & Generator

### PEP8

## lab-06 Other Categories

### Parallel Process

### Debug

### Decorator

### Memory Management

### Timeme & Space Complexity

## lab-07 RobotFrameWork

### Quick Start

### Demo