"""04_control_flow.py —— Python 流程控制入门

学习目标：
    1. 理解 Python 用缩进表示代码块的规则，避免 IndentationError；
    2. 掌握 if / elif / else 分支结构与真值测试；
    3. 了解 Python 3.10+ 的 match-case 语法；
    4. 掌握 while / for 循环、break / continue / pass 及循环-else 语义；
    5. 能独立写出九九乘法表和猜数字小游戏。

文件大纲：
    一、代码块与缩进
    二、if / elif / else 分支
    三、真值测试：哪些值是"假"的
    四、match-case 结构（3.10+）
    五、while 循环
    六、for 循环
    七、break / continue / pass 对比
    八、循环 + else 的语义
    九、嵌套循环：九九乘法表
    十、综合小案例：猜数字
    十一、动手练习（含参考答案）
"""
import sys

print("=== 04 流程控制：学习开始 ===")

# ===== 一、代码块与缩进 =====
# Python 不用大括号 {}，而是用缩进表示代码块，惯例是 4 个空格。
# 同一代码块的缩进必须一致，否则会报 IndentationError。
#
# 错误写法示例（请勿取消注释，会直接报错）：
# if 1 > 0:
# print("缺少缩进")        # IndentationError: expected an indented block
#
# if 1 > 0:
#     print(" ok")
#   print("缩进不一致")     # IndentationError: unindent does not match

score = 85
if score >= 60:
    print("及格了")            # 这两行属于同一个 if 块
    print("继续保持")
print("这行在块外，无论是否及格都会执行")

# ===== 二、if / elif / else 分支 =====
# 单分支：只判断一种情况；多分支：elif 可以有多个，else 兜底。
# 多个条件可以用 and / or / not 合并。

age = 20
if age >= 18:                                  # 单分支
    print("[分支] 已成年")

temperature = 35
if temperature > 35:                           # 多分支，从上到下只会命中一个
    print("[分支] 高温预警")
elif temperature > 28:
    print("[分支] 天气炎热")
elif temperature > 15:
    print("[分支] 天气舒适")
else:
    print("[分支] 有点冷")

hour = 9
if 6 <= hour < 12 and not hour > 11:           # 条件合并：and / or / not
    print("[分支] 现在是上午")
else:
    print("[分支] 现在不是上午")

# 嵌套：分支里再写分支，注意每层都要缩进
num = 7
if num > 0:
    if num % 2 == 0:
        print("[分支] 正偶数")
    else:
        print("[分支] 正奇数")

# ===== 三、真值测试：哪些值是"假"的 =====
# if 后面不一定要写比较表达式，任何值都有"真/假"属性。
# 常见假值：0, 0.0, ""（空字符串）, []（空列表）, {}（空字典）,
#           None, ()（空元组）, set()（空集合）；其余基本都是真值。

fake_values = [0, 0.0, "", [], {}, None, (), 42, "hi", [1], -1]
for v in fake_values:
    print("[真值]", repr(v), "->", bool(v))

# 实用技巧：用真值测试判断容器是否为空
todo = []
if not todo:
    print("[真值] 待办列表为空，可以休息了")

# ===== 四、match-case 结构（Python 3.10+） =====
# match-case 是结构化模式匹配，类似其他语言的 switch，但更强大。
# 下划线 _ 是兜底分支，相当于 default。

if sys.version_info >= (3, 10):
    command = "help"
    match command:
        case "start":
            print("[match] 启动程序")
        case "stop":
            print("[match] 停止程序")
        case "help":
            print("[match] 显示帮助信息")
        case _:
            print("[match] 未知命令:", command)

    # 也可以匹配多个值（用 | 连接）
    key = "q"
    match key:
        case "q" | "quit":
            print("[match] 退出程序")
        case _:
            print("[match] 继续运行")
else:
    print("[match] 当前 Python 版本低于 3.10，跳过本节")

# ===== 五、while 循环 =====
# while 在条件为真时反复执行，条件要能变化，否则会死循环。
#
# 死循环示例（危险，请勿运行）：
# while True:
#     print("永远停不下来")   # 条件永远为真，程序卡死

count = 3
while count > 0:                    # 基本结构：条件 -> 循环体
    print("[while] 倒计时:", count)
    count -= 1                      # 修改条件变量，让循环能结束

# while-else：循环正常结束（没有被 break 打断）时执行 else 块
n = 1
while n <= 3:
    print("[while-else] 第", n, "轮")
    n += 1
else:
    print("[while-else] 循环正常结束，执行 else")

# ===== 六、for 循环 =====
# for 用来遍历可迭代对象：range、字符串、列表、字典等。

for i in range(1, 4):               # range(起, 止)：含头不含尾
    print("[for-range] i =", i)

for ch in "abc":                    # 遍历字符串
    print("[for-字符串] 字符:", ch)

fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:                # 遍历列表
    print("[for-列表] 水果:", fruit)

scores = {"语文": 90, "数学": 95, "英语": 88}
for subject, score in scores.items():   # items() 同时拿到键和值
    print("[for-字典]", subject, "得分:", score)

for idx, fruit in enumerate(fruits, start=1):   # 带序号遍历
    print("[for-enumerate] 第", idx, "个:", fruit)

for fruit, price in zip(fruits, [5, 3, 4]):     # 两个序列并行遍历
    print("[for-zip]", fruit, "单价:", price, "元")

# ===== 七、break / continue / pass 对比 =====
# break：立即跳出整个循环；continue：跳过本次，进入下一轮；
# pass：什么都不做，仅作占位。用同一个例子对比三种效果。

print("[对比] break：遇到 3 就终止循环")
for i in range(1, 6):
    if i == 3:
        break
    print("        输出:", i)

print("[对比] continue：遇到 3 就跳过，继续后面的轮次")
for i in range(1, 6):
    if i == 3:
        continue
    print("        输出:", i)

print("[对比] pass：什么都不做，循环照常走完")
for i in range(1, 6):
    if i == 3:
        pass                # 占位，将来再补充逻辑
    print("        输出:", i)

# ===== 八、循环 + else 的语义 =====
# for-else：循环完整跑完（没被 break）才执行 else；
# 常用于"找东西"的场景：找到了就 break，找不到则走 else。

target = 4
for i in [1, 2, 3, 5]:
    if i == target:
        print("[循环else] 找到了", target)
        break
else:
    print("[循环else] 列表里没有", target, "（循环未被 break）")

# ===== 九、嵌套循环：九九乘法表 =====
# 外层循环控制行，内层循环控制列，是嵌套循环的经典例子。

print("[九九乘法表]")
for row in range(1, 10):
    for col in range(1, row + 1):
        print(f"{col}x{row}={row * col:2d}", end="  ")
    print()                             # 每行结束换行

# ===== 十、综合小案例：猜数字 =====
# 固定答案 + 逐个尝试列表，模拟猜数字过程，脚本可无人值守运行。

secret = 42
guesses = [10, 50, 30, 42]              # 模拟玩家的多次猜测
print("[猜数字] 我心里想了一个 1~100 的数，开始猜！")
attempts = 0
for guess in guesses:
    attempts += 1
    print("[猜数字] 第", attempts, "次猜:", guess)
    if guess == secret:
        print("[猜数字] 恭喜，猜对了！共用了", attempts, "次")
        break
    elif guess < secret:
        print("[猜数字] 小了")
    else:
        print("[猜数字] 大了")
else:
    print("[猜数字] 很遗憾，没猜中")

# ===== 十一、动手练习（题目 + 参考答案） =====
# 练习 1：判断一个数是正数、负数还是零（用 if / elif / else）。
# 练习 2：用 while 计算 1~100 中所有偶数的和。
# 练习 3：遍历列表，用 continue 只打印偶数，用 break 在遇到 9 时终止。
# 练习 4：FizzBuzz——1~15，能被 3 整除打 Fizz，被 5 整除打 Buzz，
#          能同时被 3 和 5 整除打 FizzBuzz，否则打印数字本身。
# 练习 5：遍历字典统计班级成绩，打印最高分科目。

def exercise_1(x):
    """练习 1 答案：判断正负零"""
    if x > 0:
        return "正数"
    elif x < 0:
        return "负数"
    else:
        return "零"

def exercise_2():
    """练习 2 答案：while 求 1~100 偶数之和"""
    total, i = 0, 2
    while i <= 100:
        total += i
        i += 2
    return total

def exercise_3(nums):
    """练习 3 答案：continue 打印偶数，break 遇 9 终止"""
    for n in nums:
        if n == 9:
            print("        遇到 9，终止")
            break
        if n % 2 != 0:
            continue
        print("        偶数:", n)

def exercise_4():
    """练习 4 答案：FizzBuzz"""
    for i in range(1, 16):
        if i % 15 == 0:
            print("        FizzBuzz")
        elif i % 3 == 0:
            print("        Fizz")
        elif i % 5 == 0:
            print("        Buzz")
        else:
            print("       ", i)

def exercise_5(class_scores):
    """练习 5 答案：找最高分科目"""
    best_subject, best_score = None, -1
    for subject, score in class_scores.items():
        if score > best_score:
            best_subject, best_score = subject, score
    print("        最高分科目:", best_subject, best_score, "分")

print("[练习演示] 练习1:", exercise_1(-7), "/", exercise_1(0), "/", exercise_1(9))
print("[练习演示] 练习2: 1~100 偶数之和 =", exercise_2())
print("[练习演示] 练习3:")
exercise_3([2, 5, 6, 9, 10])
print("[练习演示] 练习4:")
exercise_4()
print("[练习演示] 练习5:")
exercise_5({"语文": 90, "数学": 95, "英语": 88, "体育": 99})

print("=== 04 流程控制：学习结束，试着改改代码再运行吧 ===")
