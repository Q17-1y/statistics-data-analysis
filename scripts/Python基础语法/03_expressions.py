"""本文件学习目标：理解 Python「表达式」的概念与常见用法。

学习大纲：
1. 表达式 vs 语句
2. 表达式的求值与返回值
3. 算术 / 比较 / 逻辑组合表达式，bool 参与运算
4. 条件表达式（三元表达式）与嵌套可读性
5. f-string 内嵌表达式、字符串拼接与重复
6. 链式比较与布尔代数化简
7. 推导式（列表 / 集合 / 字典 / 生成器表达式）
8. eval 的危险性提醒
9. 海象运算符 :=（Python 3.8+）
10. 动手练习（含参考答案）

运行方式：python 03_expressions.py
"""


# ===== 1. 表达式 vs 语句 =====
print("===== 1. 表达式 vs 语句 =====")
# 表达式（expression）：一段会被求值、产生一个"值"的代码。
# 语句（statement）：一条"做事情"的指令，比如赋值、if、for。
# 关键区别：表达式有值，语句描述动作。
# 例如 x = 3 + 4 是一条赋值语句，其中的 3 + 4 是表达式，值为 7。
x = 3 + 4          # 整条是语句；3 + 4 是表达式
print("x = 3 + 4 中，表达式 3 + 4 的值是:", x)
print("表达式可以有值，但单独的赋值语句没有值，不能放进 print。")
# print(x = 5) 会报错，因为赋值不是表达式（Python 没有 C 风格的赋值表达式，
# 但 3.8+ 引入了专门的 := 海象运算符，见第 9 节）。

# ===== 2. 表达式的求值与返回值 =====
print("\n===== 2. 表达式的求值与返回值 =====")
# 一切表达式都可以放进 print() 里，验证它求值后的结果。
print("2 + 3 * 4 ->", 2 + 3 * 4)          # 乘法优先，14
print("'py' + 'thon' ->", "py" + "thon")  # 字符串拼接表达式
print("len('hello') > 3 ->", len("hello") > 3)  # 函数调用+比较，True
print("[1, 2] == [1, 2] ->", [1, 2] == [1, 2])  # 列表比较，True
print("结论：不确定就 print 一下，眼见为实。")

# ===== 3. 算术 / 比较 / 逻辑组合表达式，bool 参与运算 =====
print("\n===== 3. 算术 / 比较 / 逻辑组合表达式 =====")
a, b = 7, 3
# 算术运算符：+ - * / // % **
print("7 / 3 =", a / b, "| 7 // 3 =", a // b, "| 7 % 3 =", a % b, "| 2 ** 10 =", 2 ** 10)
# 比较运算符返回 bool：> < >= <= == !=
print("7 > 3 ->", a > b, "| 7 == 3 ->", a == b)
# 逻辑运算符：and or not，组合多个条件
age, has_ticket = 20, True
print("age >= 18 and has_ticket ->", age >= 18 and has_ticket)
# bool 是 int 的子类：True == 1，False == 0，因此可以参与算术
print("True == 1 ->", True == 1, "| False == 0 ->", False == 0)
print("True + True = ", True + True, "（等于 2，可用于计数）")
scores = [90, 60, 85]
print("及格人数:", sum(s >= 60 for s in scores))  # bool 求和即计数

# ===== 4. 条件表达式（三元表达式） =====
print("\n===== 4. 条件表达式（三元表达式） =====")
# 语法：值1 if 条件 else 值2 —— 条件为真取值1，否则取值2。
temperature = 35
label = "热" if temperature > 30 else "舒适"
print("temperature = 35 ->", label)
# 嵌套写法可以但会牺牲可读性，超过一层建议改用 if/elif 语句。
score = 85
grade = "优" if score >= 90 else ("良" if score >= 80 else "中")
print("score = 85 的等级:", grade)
# 等价的多行写法（语句版），更易读：
if score >= 90:
    grade2 = "优"
elif score >= 80:
    grade2 = "良"
else:
    grade2 = "中"
print("if/elif 版本结果一致:", grade2, "—— 嵌套多于一层请用语句。")

# ===== 5. 表达式风格的字符串处理 =====
print("\n===== 5. 表达式风格的字符串处理 =====")
name, price = "小明", 12.5
# f-string 中的 {} 可以放任意表达式，非常强大。
print(f"{name} 购买 3 件，总价 {price * 3:.2f} 元")
print(f"总价是否超过 30：{price * 3 > 30}")
print(f"名字大写：{name.upper()}，名字长度：{len(name)}")
# 字符串拼接（+ 要求两边都是字符串）与重复（* 数字次）
print("ab" + "cd" * 2)          # -> abcdcd
print("-" * 20)                 # 分隔线常用技巧
# 注意：拼接数字要先转 str，f-string 则无需手动转换
print("价格是 " + str(price))

# ===== 6. 链式比较与布尔代数化简 =====
print("\n===== 6. 链式比较与布尔代数化简 =====")
num = 55
# Python 支持数学写法的链式比较，等价于 0 <= num and num <= 100
print("0 <= 55 <= 100 ->", 0 <= num <= 100)
x = 3
print("1 < x < 5 ->", 1 < x < 5, "等价于", 1 < x and x < 5)
# 布尔代数化简：not (A or B) == (not A) and (not B)（德摩根定律）
flag = not (x < 0 or x > 10)
print("not (x < 0 or x > 10) ->", flag, "可化简为 0 <= x <= 10 ->", 0 <= x <= 10)
# 常见简化：`if x == True` 直接写 `if x`；`if len(s) > 0` 直接写 `if s`
s = "hi"
print("if s 等价于 len(s) > 0 ->", bool(s) == (len(s) > 0))

# ===== 7. 推导式作为表达式 =====
print("\n===== 7. 推导式作为表达式 =====")
# 推导式本身是表达式：它求值后返回一个新的序列/集合/字典/生成器。
nums = [1, 2, 3, 4, 5, 6]
# 列表推导式：[表达式 for 变量 in 可迭代对象 if 条件]
squares = [n * n for n in nums if n % 2 == 0]
print("偶数的平方:", squares)
# 集合推导式：自动去重
words = ["apple", "pear", "apple", "fig"]
uniq_len = {len(w) for w in words}
print("单词长度的集合:", uniq_len)
# 字典推导式：{键表达式: 值表达式 for ...}
len_map = {w: len(w) for w in words}
print("单词 -> 长度:", len_map)
# 生成器表达式：圆括号，惰性求值，不占中间内存，只能遍历一次
gen = (n * 2 for n in nums)
print("生成器表达式（惰性）:", gen, "| 求和 sum(...) ->", sum(gen))
print("推导式是表达式，因此可以直接作为函数参数：sum(n*2 for n in nums)")

# ===== 8. eval 的危险性 =====
print("\n===== 8. eval 的危险性 =====")
# 一句话提醒：eval 会把字符串当代码执行，绝不要对用户输入使用 eval，
# 否则恶意输入如 "__import__('os').system('...')" 会被直接执行，造成严重后果。
safe_expr = "2 + 3 * 4"
print("eval('2 + 3 * 4') =", eval(safe_expr), "（仅限自己写死的可信字符串，生产代码避免）")

# ===== 9. 海象运算符 := =====
print("\n===== 9. 海象运算符 :=（Python 3.8+） =====")
# := 在表达式内部完成赋值（求值并命名），避免重复计算。
data = [3, -1, 7, 0, 5]
# 传统写法：
filtered_old = [n for n in data if (m := n * 10) > 20]
print("海象运算符在推导式中：n*10 > 20 的结果 ->", filtered_old)
# 更常见的场景：while 循环中边读取边判断
raw = ["", "hello", "", "end", ""]
index = 0
while (chunk := raw[index]) != "end":
    index += 1
print(f"读取了 {index} 个元素才遇到 'end'，最后一个非空判断值是: {chunk!r}")
print("if (n := len(data)) > 3: 求值为", (n := len(data)) > 3, "（n 已被就地赋值为", n, "）")

# ===== 练习答案函数 =====
def parity_label(n):
    """练习1：用三元表达式判断奇偶。"""
    return "偶数" if n % 2 == 0 else "奇数"


def is_leap(year):
    """练习2：用逻辑组合表达式判断闰年。"""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def divisible_by_3_squares():
    """练习3：1~20 中能被 3 整除的数的平方（列表推导式）。"""
    return [n * n for n in range(1, 21) if n % 3 == 0]


def shopping_line(name, price, discount=0.8):
    """练习4：用 f-string 生成打折后的购物条目。"""
    return f"{name}：原价 {price} 元，折后 {price * discount:.1f} 元"


def count_before_negative(numbers):
    """练习5：用海象运算符统计第一个负数之前（不含）的元素个数。"""
    count = 0
    for n in numbers:
        if (is_neg := n < 0):  # 求值的同时把结果存入 is_neg
            break
        count += 1
    return count


# ===== 10. 动手练习 =====
print("\n===== 10. 动手练习 =====")
print("练习题目（答案在文件底部的函数中，运行后可见）：")
print("  1. 用三元表达式：给定整数 n，返回 '偶数' 或 '奇数'。")
print("  2. 判断年份 year 是否为闰年：能被4整除且不被100整除，或能被400整除（用链式/逻辑表达式）。")
print("  3. 用列表推导式生成 1~20 中所有能被 3 整除的数的平方。")
print("  4. 用 f-string 打印购物清单：商品名和打折后价格（打 8 折），保留 1 位小数。")
print("  5. 用海象运算符统计列表中第一个负数出现的下标之前的元素个数。")

print("\n--- 练习答案演示 ---")
print("练习1：n = 7 ->", parity_label(7))
print("练习2：2024 是闰年吗 ->", is_leap(2024), "| 1900 是闰年吗 ->", is_leap(1900))
print("练习3：", [n * n for n in range(1, 21) if n % 3 == 0])
print("练习4：", shopping_line("笔记本", 45.0))
print("练习5：[3, 5, -2, 8] 第一个负数前有", count_before_negative([3, 5, -2, 8]), "个元素")
