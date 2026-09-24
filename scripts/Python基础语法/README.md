# Python 核心语法学习资料

本套资料面向 Python 初学者，共 5 个可直接运行的 `.py` 文件，建议按编号顺序学习。
每个文件既是**教程**（中文注释讲解）也是**可运行脚本**（边看输出边理解）。

## 学习路线

| 顺序 | 文件 | 主题 | 核心内容 |
|------|------|------|----------|
| 1 | `01_variables.py` | 变量 | 赋值、命名规则、动态类型、可变/不可变、作用域初步 |
| 2 | `02_operators.py` | 运算符 | 算术/比较/逻辑/赋值/身份/成员/位运算、优先级 |
| 3 | `03_expressions.py` | 表达式 | 表达式 vs 语句、三元表达式、推导式、海象运算符 |
| 4 | `04_control_flow.py` | 流程控制 | if/elif/else、match-case、while、for、break/continue |
| 5 | `05_functions.py` | 函数 | 参数与返回值、作用域、lambda、类型提示 |

## 在 VSCode 中如何运行

1. 用 VSCode 打开 `python-basics` 文件夹（File → Open Folder）。
2. 确保已安装 Python 3.10+ 和官方 Python 扩展（ms-python.python）。
3. 打开任意一个文件，点击右上角 ▶️ 运行按钮；
   或在终端（Ctrl + `）中执行：

   ```bash
   python 01_variables.py
   python 02_operators.py
   python 03_expressions.py
   python 04_control_flow.py
   python 05_functions.py
   ```

4. 建议边跑边改：改一个数字、换一个条件，再运行一次，观察输出变化。

## 每个文件的结构

- 顶部 docstring：本讲学习目标与大纲
- 中间：分节讲解 + 演示代码（每节标题会打印到终端）
- 结尾：5 道动手练习（题目为注释，参考答案在 `exercises()` 函数中）

## 建议的学习方式

1. 先通读注释，再运行文件，把输出和代码一一对应。
2. 每个文件跑完后，尝试独立完成练习（不看答案）。
3. 遇到不确定的地方，用 `print()` 把中间值打出来验证。
4. 全部学完后，试着把 5 个文件里的知识点组合起来写一个小项目
   （例如：命令行计算器 = 变量 + 运算符 + 流程控制 + 函数）。
