# Code Review Agent
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
