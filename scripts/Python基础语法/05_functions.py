"""Python 初学者教程 —— 函数（Functions）

学习目标：
  1. 理解为什么需要函数（复用、抽象、测试）
  2. 掌握 def 定义函数、参数（位置/关键字/默认参数/*args/**kwargs）
  3. 理解返回值、作用域（LEGB）、lambda、类型提示
  4. 认识常见错误，并通过综合案例与练习巩固

大纲：
  1. 为什么需要函数          6. 函数是一等公民
  2. 定义与调用              7. lambda 表达式
  3. 参数详解                8. 类型提示
  4. 返回值                  9. 常见错误
  5. 文档字符串与作用域     10. 综合案例 + 动手练习
"""

import math  # 仅用于演示（标准库）


# ===== 1. 为什么需要函数 =====
# 没有函数时，同样的逻辑要复制粘贴多遍；出错要改多处。
# 函数的好处：
#   复用：写一次，处处调用
#   抽象：调用者只需知道"做什么"，不必关心"怎么做"
#   测试：功能独立，可以单独验证对错
print("===== 1. 为什么需要函数 =====")

# 反例：重复代码
print("欢迎 张三 学习 Python！")
print("欢迎 李四 学习 Python！")
# 正例：用函数复用（greet 定义在下方，Python 从上到下执行，定义之后才能调用）
def greet(name):
    """返回欢迎语。"""
    return "欢迎 " + name + " 学习 Python！"


print(greet("张三"))
print(greet("李四"))


# ===== 2. def 定义函数、命名规范、调用 =====
# 语法：def 函数名(参数): 然后缩进写函数体
# 命名规范：全小写，单词用下划线分隔（snake_case），见名知意，避免和内置函数重名
print("\n===== 2. 定义与调用 =====")


def say_hello():
    """无参数函数：定义后不会自动执行，必须调用才执行。"""
    print("你好！")


say_hello()  # 调用：函数名 + 括号


def square(x):
    return x * x


print("square(5) =", square(5))


# ===== 3. 参数：位置、关键字、默认参数、*args/**kwargs =====
print("\n===== 3. 参数详解 =====")


def introduce(name, age):
    print("姓名:", name, "年龄:", age)


# 位置参数：按顺序对应
introduce("小明", 18)
# 关键字参数：用 参数名=值，顺序可以打乱
introduce(age=20, name="小红")


# 默认参数：调用时可以不传，使用默认值
def power(base, exp=2):
    return base ** exp


print("power(3) =", power(3))        # 使用默认 exp=2
print("power(3, 3) =", power(3, 3))  # 传入 exp=3


# 【陷阱】可变默认值：默认值在函数定义时只创建一次！
# 反例：多个调用共享同一个列表，结果不断累积
def bad_append(item, box=[]):  # 不要这样写！
    box.append(item)
    return box


print("可变默认值陷阱:", bad_append(1), bad_append(2))  # [1, 2] 而不是 [1], [2]

# 正确写法：默认值用 None，函数内部再创建新列表
def good_append(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box


print("正确写法:", good_append(1), good_append(2))  # [1], [2]


# *args：接收任意多个位置参数，打包成元组
# **kwargs：接收任意多个关键字参数，打包成字典
def total(*args, **kwargs):
    print("位置参数元组:", args)
    print("关键字参数字典:", kwargs)


total(1, 2, 3, a=10, b=20)


# ===== 4. 返回值：return、多返回值、无 return =====
print("\n===== 4. 返回值 =====")


def min_max(nums):
    """同时返回最小值和最大值（其实是返回一个元组，可解包）。"""
    return min(nums), max(nums)


low, high = min_max([3, 1, 4, 1, 5])  # 元组解包
print("最小值:", low, "最大值:", high)


def no_return():
    x = 1  # 没有 return 语句


result = no_return()
print("没有 return 的函数返回:", result)  # None


# ===== 5. 文档字符串 docstring 与作用域 =====
print("\n===== 5. 文档字符串与作用域 =====")


def circle_area(r):
    """计算圆的面积。

    参数:
        r: 半径（必须大于 0）
    返回:
        圆的面积
    """
    return math.pi * r ** 2


help(circle_area)           # help() 会显示 docstring
print(".__doc__ 内容:", circle_area.__doc__.splitlines()[0])

# 作用域 LEGB：查找变量的顺序
#   L(Local 局部) -> E(Enclosing 外层函数) -> G(Global 全局) -> B(Built-in 内置)
x = "全局变量"


def outer():
    y = "外层函数变量"

    def inner():
        z = "局部变量"
        print("inner 内访问:", z, "|", y, "|", x)

    inner()


outer()
print("全局访问:", x)

# global：在函数内修改全局变量（能用但不推荐，容易让程序难维护）
count = 0


def increase():
    global count  # 声明要修改的是全局变量
    count += 1


increase()
increase()
print("global 修改后的 count =", count, "（提醒：尽量避免使用 global）")


# ===== 6. 函数是一等公民 =====
# 函数和数字、字符串一样，可以赋值给变量、当参数传递、放进列表/字典
print("\n===== 6. 函数是一等公民 =====")


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


f = add            # 赋值给变量
print("f(2, 3) =", f(2, 3))


def apply(func, a, b):  # 函数作为参数
    return func(a, b)


print("apply(add, 2, 3) =", apply(add, 2, 3))
print("apply(mul, 2, 3) =", apply(mul, 2, 3))

ops = {"加": add, "乘": mul}  # 放进字典
print("ops['加'](4, 5) =", ops["加"](4, 5))


# ===== 7. lambda 表达式 =====
# lambda 参数: 表达式 —— 用来写"一次性"的小函数，常配合 sorted(key=...) 使用
print("\n===== 7. lambda 表达式 =====")

students = [("小明", 88), ("小红", 95), ("小刚", 76)]
# 按成绩从高到低排序：key 接收一个函数，lambda 提取每个元组的第 2 项
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print("按成绩排序:", by_score)

words = ["banana", "apple", "cherry"]
print("按长度排序:", sorted(words, key=lambda w: len(w)))


# ===== 8. 类型提示（type hints）=====
# 类型提示只是"标注"，Python 不会强制检查，但能提高可读性，配合工具可查错
print("\n===== 8. 类型提示 =====")


def add_tip(a: int, b: int) -> int:
    """把两个整数相加并返回整数。"""
    return a + b


print("add_tip(1, 2) =", add_tip(1, 2))


def describe(name: str, score: float = 0.0) -> str:
    return f"{name} 的分数是 {score}"


print(describe("小明", 92.5))


# ===== 9. 常见错误 =====
print("\n===== 9. 常见错误 =====")
# 错误 1：先调用后定义 -> NameError: name 'xxx' is not defined
#   my_func()        # 如果写在这里会报错，因为 my_func 还没定义
#   def my_func(): ...
# 正确：先定义，后调用
def my_func():
    print("先定义，后调用，才能成功执行")


my_func()

# 错误 2：函数体忘记缩进 -> IndentationError: expected an indented block
#   def broken():
#   print("忘记缩进")   # 报缩进错误
# 错误 3：缩进不一致（混用空格和 Tab）也会报错，统一用 4 个空格
print("提示：函数体必须缩进（约定 4 个空格），且先定义后调用")


# ===== 10. 综合案例：温度转换函数组 =====
print("\n===== 10. 综合案例：温度转换 =====")


def celsius_to_fahrenheit(c: float) -> float:
    """摄氏度 -> 华氏度：F = C * 9 / 5 + 32"""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """华氏度 -> 摄氏度：C = (F - 32) * 5 / 9"""
    return (f - 32) * 5 / 9


def convert(value: float, to_f: bool) -> float:
    """根据 to_f 选择转换方向，并保留 1 位小数。"""
    result = celsius_to_fahrenheit(value) if to_f else fahrenheit_to_celsius(value)
    return round(result, 1)


for c in [0, 25, 37, 100]:
    print(f"{c}°C = {convert(c, to_f=True)}°F")
for f in [32, 98.6, 212]:
    print(f"{f}°F = {convert(f, to_f=False)}°C")


# ===== 动手练习 =====
# 练习 1：写函数 is_even(n)，判断 n 是否为偶数，返回 True/False。
# 练习 2：写函数 count_vowels(s)，统计字符串 s 中元音字母（aeiou，不区分大小写）的个数。
# 练习 3：写函数 average(*args)，接收任意多个数字，返回平均值；无参数时返回 0。
# 练习 4：写函数 make_counter()，每次调用返回值加 1（提示：用可变默认值或闭包）。
# 练习 5：用 lambda + sorted 把 students 按姓名排序。

# --- 以下是参考答案 ---

print("\n===== 动手练习：参考答案演示 =====")


def is_even(n: int) -> bool:
    """练习 1：判断偶数。"""
    return n % 2 == 0


def count_vowels(s: str) -> int:
    """练习 2：统计元音字母个数。"""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def average(*args) -> float:
    """练习 3：求平均值，无参数返回 0。"""
    return sum(args) / len(args) if args else 0


def make_counter(start=[0]):  # 这里反用"可变默认值"实现记忆，工程中建议用类或闭包
    """练习 4：每次调用计数加 1。"""
    start[0] += 1
    return start[0]


print("练习 1: is_even(10) =", is_even(10), ", is_even(7) =", is_even(7))
print("练习 2: count_vowels('Hello World') =", count_vowels("Hello World"))
print("练习 3: average(1, 2, 3, 4) =", average(1, 2, 3, 4), ", average() =", average())
print("练习 4: 计数器连续调用:", make_counter(), make_counter(), make_counter())
print("练习 5: 按姓名排序:", sorted(students, key=lambda s: s[0]))

print("\n全部小节演示完毕！建议修改代码、多试几次，观察输出变化。")
