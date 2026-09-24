"""变量主题学习材料（01_variables.py）

学习目标：
1. 理解 Python 变量的本质：变量是"名字绑定对象"，而不是存值的盒子。
2. 掌握各种赋值方式：单赋值、多变量赋值、链式赋值、解包赋值。
3. 掌握命名规则与 snake_case 风格，认识常量约定（全大写）。
4. 理解动态类型，会用 type() 和 isinstance() 查看类型。
5. 初步了解 id()、可变/不可变对象、del 删除变量、作用域概念。
6. 学会在 f-string 中使用变量输出信息。

内容大纲：
  第一节 变量的本质：名字绑定对象
  第二节 基础赋值语句
  第三节 多变量赋值 / 链式赋值 / 解包赋值
  第四节 命名规则与命名风格
  第五节 动态类型与 type() / isinstance()
  第六节 id() 与可变 / 不可变对象
  第七节 常量约定
  第八节 del 删除变量
  第九节 变量作用域初步
  第十节 f-string 中使用变量
  动手练习
"""

# ===== 第一节 变量的本质：名字绑定对象 =====
print("===== 第一节 变量的本质 =====")
# Python 的变量不是"装值的盒子"，而是贴在对象上的"名字标签"。
# 赋值语句 x = 10 的含义是：创建整数对象 10，然后把名字 x 绑定到它上面。
# 同一个对象可以有多个名字，就像一件行李可以挂多张行李牌。
x = 10
y = x          # y 和 x 绑定到同一个对象 10
print(f"x = {x}, y = {y}，它们指向同一个对象：{x is y}")

# ===== 第二节 基础赋值语句 =====
print("===== 第二节 基础赋值语句 =====")
# 赋值用等号 =，左边是变量名，右边是表达式。先算右边，再绑定名字。
age = 18
name = "小明"
height = 1.75
print(f"姓名：{name}，年龄：{age}，身高：{height} 米")
# 赋值可以随时用旧值算新值（右侧先用旧值求值）
age = age + 1
print(f"过完生日，age 变成 {age}")
# 复合赋值运算符是 age = age + 1 的简写
age += 2
print(f"再过两年，age 变成 {age}")

# ===== 第三节 多变量赋值 / 链式赋值 / 解包赋值 =====
print("===== 第三节 多变量赋值 =====")
# 1. 多变量赋值：等号两边数量对应，右侧先整体求值再同时绑定
a, b = 1, 2
print(f"a = {a}, b = {b}")
# 利用"先求右边"的特点可以不借助临时变量交换两个变量
a, b = b, a
print(f"交换后：a = {a}, b = {b}")
# 2. 链式赋值：三个名字绑定到同一个对象
p = q = r = 100
print(f"p = {p}, q = {q}, r = {r}")
# 3. 解包赋值：把序列里的元素依次解给多个变量
point = (3, 5)
px, py = point
print(f"点的横坐标 px = {px}，纵坐标 py = {py}")

# ===== 第四节 命名规则与命名风格 =====
print("===== 第四节 命名规则与风格 =====")
# 规则（硬性要求）：
#   只能含字母、数字、下划线；不能以数字开头；区分大小写；不能用关键字。
# 风格（社区约定）：Python 推荐 snake_case（小写单词 + 下划线）。
student_name = "小红"      # 推荐：snake_case
total_score = 95
print(f"学生 {student_name} 的总分是 {total_score}")
# 反例（仅供注释说明，不要照写）：
# 2name = "错"      # 不能以数字开头
# my-name = "错"    # 不能用连字符
# class = "错"      # class 是关键字
import keyword
print(f"关键字举例：{keyword.kwlist[:6]} ...（共 {len(keyword.kwlist)} 个，都不能作变量名）")

# ===== 第五节 动态类型与 type() / isinstance() =====
print("===== 第五节 动态类型 =====")
# 变量没有固定类型，类型属于它绑定的对象；重新赋值可以换类型，这就是"动态类型"。
value = 42
print(f"value = {value}，类型是 {type(value).__name__}")
value = "现在变成字符串了"
print(f"value = {value}，类型是 {type(value).__name__}")
# isinstance(obj, 类型) 判断对象是否属于某类型，比比较 type() 更常用
n = 3.14
print(f"n = {n}，它是浮点数吗？{isinstance(n, float)}")

# ===== 第六节 id() 与可变 / 不可变对象 =====
print("===== 第六节 id() 与可变性 =====")
# id() 返回对象的唯一标识（在 CPython 里通常是内存地址）。
# 不可变对象（int、str、tuple 等）不能原地修改；可变对象（list、dict 等）可以。
m = 1000
print(f"修改前 m 的 id：{id(m)}")
m = m + 1                 # 不可变对象：实际是绑定了新对象
print(f"修改后 m 的 id：{id(m)}（变了，说明绑定了新对象）")
my_list = [1, 2, 3]
print(f"修改前列表的 id：{id(my_list)}")
my_list.append(4)         # 可变对象：原地修改，id 不变
print(f"修改后列表的 id：{id(my_list)}（没变，说明是同一个对象）")

# ===== 第七节 常量约定 =====
print("===== 第七节 常量约定 =====")
# Python 没有真正的常量，约定用"全大写 + 下划线"命名表示"请不要修改它"。
MAX_RETRY = 3
PI_APPROX = 3.14159
print(f"最大重试次数 MAX_RETRY = {MAX_RETRY}")
print(f"圆周率近似值 PI_APPROX = {PI_APPROX}")

# ===== 第八节 del 删除变量 =====
print("===== 第八节 del 删除变量 =====")
# del 删除的是"名字绑定"，不是对象本身；对象没有名字引用后会被自动回收。
temp = "我会被删除"
print(f"删除前：temp = {temp}")
del temp
# 再访问 temp 会报 NameError，这里用 try 捕获避免程序崩溃
try:
    print(temp)
except NameError:
    print("删除后再访问 temp 报错：NameError（名字已不存在）")

# ===== 第九节 变量作用域初步 =====
print("===== 第九节 作用域初步 =====")
# 在函数里赋值的变量是"局部变量"，只在函数内有效；
# 在模块顶层赋值的是"全局变量"，全文件都能读。
global_var = "我是全局变量"

def demo_scope():
    local_var = "我是局部变量"
    print(global_var)      # 函数内可以读取全局变量
    print(local_var)       # 局部变量在函数内使用

demo_scope()
print(f"函数外能读全局变量：{global_var}")
# print(local_var)  # 如果取消注释会报 NameError：函数外访问不到局部变量

# ===== 第十节 f-string 中使用变量 =====
print("===== 第十节 f-string =====")
# 字符串前加 f，就能在大括号 {} 里直接嵌入变量甚至表达式。
city = "北京"
temperature = 23.6
print(f"今天 {city} 的气温是 {temperature} 度")
print(f"气温四舍五入：{round(temperature)} 度")
print(f"一行代码里也能做计算：{city} 明年 GDP 排名不知道，但 1 + 1 = {1 + 1}")

# ===== 动手练习 =====
# 题目 1：创建两个变量 num1、num2，交换它们的值并打印交换前后结果。
# 题目 2：用一条赋值语句把 (7, 8, 9) 解包给 x、y、z，并打印三者之和。
# 题目 3：定义常量 GRAVITY = 9.8，已知下落时间 t = 3 秒，用公式 h = 0.5 * GRAVITY * t ** 2 求下落高度。
# 题目 4：变量 s = "hello"，先打印它的 id，再执行 s = s + " world" 并再次打印 id，观察是否变化。
# 题目 5：写一个函数 make_greeting(name)，内部用局部变量拼出问候语并返回，在函数外打印返回值。

def exercises():
    """练习答案演示：逐题运行并打印结果。"""
    print("===== 动手练习 =====")

    # 答案 1：交换两个变量
    num1, num2 = 10, 20
    print(f"练习1 交换前：num1 = {num1}, num2 = {num2}")
    num1, num2 = num2, num1
    print(f"练习1 交换后：num1 = {num1}, num2 = {num2}")

    # 答案 2：解包赋值并求和
    x, y, z = (7, 8, 9)
    print(f"练习2 x={x}, y={y}, z={z}，三者之和 = {x + y + z}")

    # 答案 3：常量参与计算
    GRAVITY = 9.8
    t = 3
    h = 0.5 * GRAVITY * t ** 2
    print(f"练习3 下落 {t} 秒，高度 = {h} 米")

    # 答案 4：观察字符串（不可变对象）的 id 变化
    s = "hello"
    id_before = id(s)
    s = s + " world"
    id_after = id(s)
    print(f"练习4 修改前 id：{id_before}，修改后 id：{id_after}，"
          f"id 变化了吗？{id_before != id_after}（字符串不可变，会绑定新对象）")

    # 答案 5：局部变量与返回值
    def make_greeting(name):
        greeting = f"你好，{name}！欢迎学习 Python 变量。"  # greeting 是局部变量
        return greeting

    print(f"练习5 {make_greeting('小刚')}")

if __name__ == "__main__":
    exercises()
