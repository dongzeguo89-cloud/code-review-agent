import requests

SYSTEM_PROMPT = """你是资深代码审查工程师。请基于 diff 给出中文审查结果，包含：
1) 总结
2) 问题清单（Severity: High/Medium/Low，原因，修复建议）
3) 建议补充测试
输出 markdown。"""

FINAL_PROMPT = """请把多个 chunk 审查结果汇总成最终报告，输出：
## AI Code Review Report
### Overall Risk
### Summary
### Key Findings
### Suggested Fixes
### Suggested Tests
### Notes
中文，markdown。"""

def chunk_text(text, max_chars=12000):
    if len(text) <= max_chars:
        return [text]
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

class CodeReviewAgent:
    def __init__(self, llm, max_diff_chars=12000):
        self.llm = llm
        self.max_diff_chars = max_diff_chars

    def review(self, diff_text, pr_title="", pr_body=""):
        if not diff_text.strip():
            return "## AI Code Review Report\n\n### Overall Risk\nLow\n\n### Summary\n无 diff。"
        chunks = chunk_text(diff_text, self.max_diff_chars)
        reviews = []
        for i, c in enumerate(chunks, 1):
            user = f"PR标题: {pr_title}\nPR描述: {pr_body}\n第{i}/{len(chunks)}段diff：\n```diff\n{c}\n```"
            reviews.append(self.llm.chat([
                {"role":"system","content":SYSTEM_PROMPT},
                {"role":"user","content":user}
            ]))
        merged = "\n\n---\n\n".join(reviews)
        return self.llm.chat([
            {"role":"system","content":FINAL_PROMPT},
            {"role":"user","content":f"PR标题:{pr_title}\nPR描述:{pr_body}\n以下是分段审查：\n{merged}"}
        ])
