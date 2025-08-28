---
layout: docs_page
title: Python基础
category: 学习笔记
description: Python编程语言的基础知识和学习笔记
date: 2024-01-01
permalink: /docs/学习笔记/Python基础/
---

# Python基础学习笔记

## 变量和数据类型

### 基本数据类型
- **整数 (int)**: `42`, `-17`
- **浮点数 (float)**: `3.14`, `-0.001`
- **字符串 (str)**: `"Hello World"`, `'Python'`
- **布尔值 (bool)**: `True`, `False`

### 变量命名规则
- 只能包含字母、数字和下划线
- 不能以数字开头
- 区分大小写
- 不能使用Python关键字

## 控制流

### if语句
```python
if condition:
    # 执行代码
elif another_condition:
    # 执行代码
else:
    # 执行代码
```

### 循环
```python
# for循环
for item in items:
    print(item)

# while循环
while condition:
    # 执行代码
```

## 函数

### 定义函数
```python
def greet(name):
    return f"Hello, {name}!"
```

### 参数类型
- 位置参数
- 关键字参数
- 默认参数
- 可变参数

## 数据结构

### 列表 (List)
```python
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
```

### 字典 (Dictionary)
```python
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
```

### 元组 (Tuple)
```python
coordinates = (10, 20)
```

### 集合 (Set)
```python
unique_numbers = {1, 2, 3, 4, 5}
```

## 文件操作

### 读取文件
```python
with open('file.txt', 'r') as file:
    content = file.read()
```

### 写入文件
```python
with open('file.txt', 'w') as file:
    file.write('Hello World')
```

## 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    print("总是执行")
```

## 模块和包

### 导入模块
```python
import math
from datetime import datetime
import pandas as pd
```

### 创建自己的模块
```python
# mymodule.py
def my_function():
    return "Hello from my module"
```

## 面向对象编程

### 类定义
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
```

### 继承
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

## 常用内置函数

- `len()` - 获取长度
- `type()` - 获取类型
- `print()` - 打印输出
- `input()` - 获取用户输入
- `range()` - 生成数字序列
- `enumerate()` - 枚举
- `zip()` - 合并序列

## 列表推导式

```python
# 传统方式
squares = []
for i in range(10):
    squares.append(i**2)

# 列表推导式
squares = [i**2 for i in range(10)]
```

## 装饰器

```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
```

---

*最后更新: 2024-01-20*
