<<<<<<< HEAD
﻿# Code Review Agent
自动对 GitHub PR 做 AI 代码评审，并评论到 PR。
## 快速使用
1. 配置 GitHub Secrets：
   - OPENAI_API_KEY
   - （可选）OPENAI_BASE_URL
   - （可选）OPENAI_MODEL
2. 提交本项目到你的仓库后，创建 PR 即自动触发。
## 本地调试
```bash
pip install -r requirements.txt
set GITHUB_TOKEN=xxx
set OPENAI_API_KEY=xxx
python -m reviewer_agent.main --repo owner/repo --pr 1 --dry-run
=======
# code-review-agent
 我搭建了一个面向研发团队的代码评审 Agent，主要解决人工 CR 覆盖不全、风格不一致、低级 Bug 难以及时发现的问题。  Agent 会在开发者提交 PR 后自动拉取代码 diff，结合仓库规范、历史缺陷模式和接口变更影响范围进行多轮分析，识别潜在空指针、越权访问、性能隐患和重复实现。  在流程上，我设计了“代码理解 Agent + 规范检查 Agent + 风险评估 Agent + 修复建议 Agent”的多 Agent 协作机制：先解析业务上下文，再按规则和语义两层检查，最后生成可直接使用的 review comment 或修复 patch。对于高风险改动，还会触发单测生成和回归建议。
>>>>>>> 1622aa23ae2188bc1b3b7ed54763de01c2cc9da7
