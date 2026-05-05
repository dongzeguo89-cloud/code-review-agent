import argparse
import json
import os
import sys

from .config import Config
from .github_client import GitHubClient
from .llm_client import LLMClient
from .reviewer import CodeReviewAgent

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--repo")
    p.add_argument("--pr", type=int)
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()

def event_repo_pr():
    repo = os.getenv("GITHUB_REPOSITORY")
    path = os.getenv("GITHUB_EVENT_PATH")
    if not repo or not path:
        raise RuntimeError("GITHUB_REPOSITORY / GITHUB_EVENT_PATH not set")
    with open(path, "r", encoding="utf-8") as f:
        ev = json.load(f)
    return repo, int(ev["pull_request"]["number"])

def main():
    args = parse_args()
    cfg = Config()
    cfg.validate()
    if args.repo and args.pr:
        repo, pr = args.repo, args.pr
    else:
        repo, pr = event_repo_pr()
    gh = GitHubClient(cfg.github_token, cfg.github_api_url)
    llm = LLMClient(cfg.openai_api_key, cfg.openai_base_url, cfg.openai_model)
    agent = CodeReviewAgent(llm, cfg.max_diff_chars)
    pr_info = gh.get_pull_request(repo, pr)
    diff = gh.get_pull_request_diff(repo, pr)
    report = agent.review(diff, pr_info.get("title",""), pr_info.get("body",""))
    body = "<!-- ai-code-review-agent -->\n\n" + report
    if args.dry_run:
        print(body)
        return
    gh.create_issue_comment(repo, pr, body)
    print("Comment posted.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
        sys.exit(1)
