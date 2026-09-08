# 统计与数据分析学习仓库

本仓库用于《统计与数据分析》课程的学习，同时包含 AI 概念学习作业：一个自制的「概念学习资料生成 Skill」及用它产出的三份概念学习资料。

## 目录结构

```
├── README.md                              # 本文件
├── .gitignore                             # 忽略规则（含敏感信息排除）
├── .workbuddy/
│   └── skills/
│       └── concept-origin-study/          # 项目级 Skill
│           ├── SKILL.md
│           └── assets/
│               └── concept-study-template.html
├── learning-materials/                    # 概念学习资料
│   ├── agent.html                         # Agent（智能体）
│   ├── llm-context.html                   # 大模型的上下文
│   ├── skill.html                         # Skill（智能体技能）
│   └── concept-relationship.md            # 三概念关系说明（含 Mermaid 图）
├── notes/                                 # 课程学习笔记
├── code/                                  # 课程练习代码
└── data/                                  # 课程数据集
```

## 概念学习 Skill：concept-origin-study

### 用途

从任意概念的**原始出处**（官方公告、原始论文、正式规范）检索一手资料，生成一份可视化、低认知负荷的单文件 HTML 学习资料：以图代文、单一强调色、出处可点击验证、附 5 道递增难度测试题。

### 存放路径

`.workbuddy/skills/concept-origin-study/SKILL.md`（项目级 Skill，仅在本仓库内生效）

### 如何调用

在 WorkBuddy 中打开本仓库后，直接说：

- 「帮我学习 ×× 概念，从源头查资料生成可视化学习资料」
- 「用 concept-origin-study 学一下 ××」

Skill 会自动执行四步：追溯源头（WebSearch/WebFetch 一手文献）→ 提炼核心 → 用模板生成 HTML → 交付与自检。

### 已生成的学习资料

| 资料 | 主题 | 一手来源举例 |
|------|------|-------------|
| [agent.html](learning-materials/agent.html) | Agent（智能体） | Lilian Weng（2023）、Anthropic《Building Effective Agents》（2024） |
| [llm-context.html](learning-materials/llm-context.html) | 大模型的上下文 | 《Attention Is All You Need》（2017）、《Lost in the Middle》（2023） |
| [skill.html](learning-materials/skill.html) | Skill（智能体技能） | Anthropic Agent Skills 公告与工程博客（2025）、agentskills.io 规范 |
| [concept-relationship.md](learning-materials/concept-relationship.md) | 三概念的关系 | 汇总以上来源 |

每份资料均包含：个人解释初稿、核心机制图解、具体应用场景、易混淆问题与使用边界、可核查的来源链接、5 道递增难度测试题。

## 人工核查说明

以下内容在使用 AI 生成后经过了人工阅读与核查：

1. **来源真实性**：页内所有链接均逐一访问验证（抓取原文核对），无伪造 URL
2. **技术断言**：定义、数字（如 name ≤64 字符、U 形利用率曲线）、结论均与原文比对；来源间无冲突
3. **需要继续人工完成的部分**：每份资料中的「个人解释」目前为 AI 起草的初稿，已明确标注，需用自己的话改写后再作为最终版本——这是刻意保留的人工环节
4. **测试题**：答案与解析均回链到原文相应位置，可点击验证

## 统计与数据分析课程学习

### 学习目标

- 掌握描述性统计：集中趋势、离散程度、数据分布
- 理解概率基础与常见分布（二项、泊松、正态分布）
- 学会假设检验、置信区间、相关性分析
- 熟练使用 Python（pandas / matplotlib / scipy）进行数据分析

### 学习计划

| 阶段 | 内容 | 状态 |
|------|------|------|
| 第 1 周 | 课程导论、数据类型与数据来源 | ⬜ |
| 第 2 周 | 描述性统计与数据可视化 | ⬜ |
| 第 3 周 | 概率基础 | ⬜ |
| 第 4 周 | 常见概率分布 | ⬜ |
| 第 5 周 | 抽样与参数估计 | ⬜ |
| 第 6 周 | 假设检验 | ⬜ |
| 第 7 周 | 相关与回归分析 | ⬜ |
| 第 8 周 | 综合数据分析项目 | ⬜ |

### 学习方式

- 每周在 `notes/` 中记录学习笔记
- 在 `code/` 中完成课堂练习与课后作业
- 随时提交（commit），保持更新习惯
