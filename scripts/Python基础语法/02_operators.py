"""
02_operators.py —— Python 运算符学习材料

学习目标：
    1. 掌握 Python 七大类运算符的用法与区别
    2. 理解 / 与 // 的区别、% 的常见用途
    3. 理解 is 与 == 的区别、逻辑运算符的短路求值
    4. 了解运算符优先级，养成加括号的好习惯

大纲：
    一、算术运算符
    二、比较运算符（含链式比较）
    三、逻辑运算符（含短路求值）
    四、赋值运算符
    五、身份运算符（is 与 ==）
    六、成员运算符
    七、位运算符
    八、运算符优先级
    九、动手练习

运行方式：python 02_operators.py
"""

# ===== 一、算术运算符 =====
print("===== 一、算术运算符 =====")
# + 加、- 减、* 乘、/ 除（结果一定是 float）、// 整除（向下取整）、% 取余、** 幂

print(f"10 + 3 = {10 + 3}")     # 加法
print(f"10 - 3 = {10 - 3}")     # 减法
print(f"10 * 3 = {10 * 3}")     # 乘法
print(f"10 / 3 = {10 / 3}")     # 真除法：结果是 float，即使能整除也是 4.0
print(f"10 // 3 = {10 // 3}")   # 整除：舍去小数部分（向下取整，负数时注意）
print(f"-7 // 2 = {-7 // 2}")   # -3.5 向下取整是 -4，不是 -3！
print(f"10 % 3 = {10 % 3}")     # 取余：10 = 3*3 + 1，余 1
print(f"2 ** 10 = {2 ** 10}")   # 幂：2 的 10 次方

# / 与 // 的区别小结：
# / 永远返回 float（7 / 2 = 3.5）；// 返回整数商（向下取整，7 // 2 = 3）

# % 取余的常见用途 1：判断奇偶
num = 17
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")

# % 取余的常见用途 2：循环分组（编号轮换）
for i in range(1, 6):
    group = i % 3  # 编号 1~5 轮流分到第 0、1、2 组
    print(f"编号 {i} -> 第 {group} 组")

# ===== 二、比较运算符 =====
print("===== 二、比较运算符 =====")
# == 等于、!= 不等于、> < >= <=，比较结果都是布尔值 True / False

x = 5
print(f"x = {x}")
print(f"x == 5 -> {x == 5}")
print(f"x != 5 -> {x != 5}")
print(f"x > 10 -> {x > 10}")
print(f"x <= 5 -> {x <= 5}")

# 链式比较：Python 独有的写法，等价于 (1 < x) and (x < 10)
print(f"1 < x < 10 -> {1 < x < 10}")
print(f"1 < x < 4  -> {1 < x < 4}")

# ===== 三、逻辑运算符 =====
print("===== 三、逻辑运算符 =====")
# and：两者都真才真；or：有一个真就真；not：取反
# 重要特性：and / or 返回的是参与运算的值本身，不一定是布尔值！

a, b = 0, "hello"
print(f"a = {a}, b = {b!r}")
print(f"a and b -> {a and b!r}")   # a 为假，直接返回 a（0）
print(f"a or b  -> {a or b!r}")    # a 为假，继续看 b，返回 b
print(f"not a   -> {not a}")       # not 一定返回布尔值

# 短路求值：左边能确定结果时，右边根本不会执行
def touch():
    print("（右边表达式被执行了！）")
    return True

print("-- 演示短路 --")
False and touch()   # 左边已确定为 False，touch() 不会执行
True or touch()     # 左边已确定为 True，touch() 不会执行
print("上面两行没有触发 touch()，说明发生了短路")

# 实用技巧：用 or 提供默认值
name = ""
display = name or "匿名用户"
print(f"name 为空时，name or '匿名用户' -> {display}")

# ===== 四、赋值运算符 =====
print("===== 四、赋值运算符 =====")
# = 赋值；+= -= *= /= //= %= **= 等复合赋值，相当于自更新

score = 100
score += 20   # 等价于 score = score + 20
print(f"score += 20 -> {score}")
score -= 50
print(f"score -= 50 -> {score}")
score *= 2
print(f"score *= 2  -> {score}")
score //= 3
print(f"score //= 3 -> {score}")
score %= 7
print(f"score %= 7  -> {score}")

# ===== 五、身份运算符 =====
print("===== 五、身份运算符 =====")
# is 比较两个变量的 id（是否是同一个对象），== 比较值是否相等
# 判断 None 的标准写法是 if x is None

m = [1, 2, 3]
n = [1, 2, 3]
print(f"m == n -> {m == n}")        # 值相等，True
print(f"m is n -> {m is n}")        # 两个不同的列表对象，False
print(f"id(m) = {id(m)}, id(n) = {id(n)}")

p = m
print(f"p = m 之后，p is m -> {p is m}")  # 同一个对象，True

# 小整数缓存现象：Python 对 -5 ~ 256 的整数做了缓存，
# 范围内的整数指向同一个对象，所以 is 会返回 True；
# 超出范围的整数每次创建新对象，is 通常返回 False
# （下面用变量运算得到 1000，避免解释器把相同字面量合并成同一对象）
c = 100
d = 100
t = 999
e = 1000
f = t + 1  # 运行时算出 1000，是新创建的对象
print(f"c is d (100)   -> {c is d}")   # True：命中缓存
print(f"e is f (1000)  -> {e is f}")   # False：超出缓存范围
# 注意：这是解释器的实现细节，日常判断数值相等请用 ==，不要用 is

# ===== 六、成员运算符 =====
print("===== 六、成员运算符 =====")
# in / not in：判断某个元素是否存在于序列或集合中

s = "python"
print(f"'py' in 'python'     -> {'py' in s}")
print(f"'java' not in 'python' -> {'java' not in s}")

lst = [10, 20, 30]
print(f"20 in [10, 20, 30]  -> {20 in lst}")
print(f"40 in [10, 20, 30]  -> {40 in lst}")

d = {"name": "小明", "age": 18}
print(f"'name' in 字典      -> {'name' in d}")   # 字典判断的是「键」
print(f"'小明' in 字典      -> {'小明' in d}")   # 值不在判断范围内

# ===== 七、位运算符 =====
print("===== 七、位运算符 =====")
# & 按位与、| 按位或、^ 按位异或、~ 按位取反、<< 左移、>> 右移
# 先用 bin() 看二进制，再对照结果

x1, x2 = 0b1100, 0b1010  # 12 和 10
print(f"bin(12) = {bin(x1)}, bin(10) = {bin(x2)}")
print(f"12 & 10 = {x1 & x2}  -> {bin(x1 & x2)}")   # 同 1 才是 1：1000
print(f"12 | 10 = {x1 | x2}  -> {bin(x1 | x2)}")   # 有 1 就是 1：1110
print(f"12 ^ 10 = {x1 ^ x2}  -> {bin(x1 ^ x2)}")   # 不同才是 1：0110
print(f"~12     = {~x1}  （-(12)-1）")              # 按位取反：~n = -n-1
print(f"1 << 4  = {1 << 4}   （相当于 *2**4）")
print(f"16 >> 2 = {16 >> 2}  （相当于 //2**2）")

# ===== 八、运算符优先级 =====
print("===== 八、运算符优先级 =====")
# 速记口诀（从高到低）：
#   括号最高，幂运算次之；
#   一元加减取反跟在后；
#   乘除余整平级，加减随后；
#   移位插在中间站；
#   位与、位异、位或，依次排；
#   比较运算不会算，链式随便连；
#   not 高于 and，and 高于 or；
#   最后才轮到赋值 = 。

# 示例：不加括号 vs 加括号，结果完全不同
result1 = 2 + 3 * 4 ** 2       # 先算 4**2=16，再 3*16=48，最后 +2
result2 = (2 + 3) * 4 ** 2     # 先算括号 5，再 5*16
result3 = (2 + 3 * 4) ** 2     # 先算括号 14，再平方
print(f"2 + 3 * 4 ** 2     = {result1}")
print(f"(2 + 3) * 4 ** 2   = {result2}")
print(f"(2 + 3 * 4) ** 2   = {result3}")
print("结论：优先级记不清时，直接加括号，代码更清晰！")

# ===== 九、动手练习 =====
print("===== 九、动手练习 =====")

# 练习 1：给定秒数 total_seconds，用 // 和 % 换算成「x 分 y 秒」
# 练习 2：判断年份 year 是否为闰年（能被 4 整除且不能被 100 整除，
#         或能被 400 整除），用逻辑运算符实现
# 练习 3：一个数对 3 取余为 0、对 5 取余为 0，则能被 15 整除，
#         试试分别用 % 与 & 写出两种判断方式并验证 30
# 练习 4：用位运算符交换两个整数 a、b 的值（不用第三个变量）
# 练习 5：用 or 短路特性，把空字符串 name 变成默认值「访客」

def exercises():
    """练习答案演示"""
    print("练习 1：")
    total_seconds = 250
    minutes, seconds = total_seconds // 60, total_seconds % 60
    print(f"  {total_seconds} 秒 = {minutes} 分 {seconds} 秒")

    print("练习 2：")
    year = 2024
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(f"  {year} 年是闰年吗？{is_leap}")

    print("练习 3：")
    n = 30
    print(f"  {n} % 15 == 0 -> {n % 15 == 0}")
    print(f"  {n} % 3 == 0 and {n} % 5 == 0 -> {n % 3 == 0 and n % 5 == 0}")

    print("练习 4：")
    a, b = 3, 9
    a, b = b, a  # Python 更推荐的多重赋值写法
    print(f"  交换后 a = {a}, b = {b}")

    print("练习 5：")
    name = ""
    print(f"  name or '访客' -> {name or '访客'}")


exercises()
print("全部演示完成，试着修改上面的数字，重新运行观察变化吧！")
