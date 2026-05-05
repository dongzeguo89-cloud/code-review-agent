import requests

class GitHubClient:
    def __init__(self, token: str, api_url: str = "https://api.github.com"):
        self.api_url = api_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_pull_request(self, repo: str, pr_number: int) -> dict:
        r = requests.get(f"{self.api_url}/repos/{repo}/pulls/{pr_number}", headers=self.headers, timeout=30)
        r.raise_for_status()
        return r.json()

    def get_pull_request_diff(self, repo: str, pr_number: int) -> str:
        headers = dict(self.headers)
        headers["Accept"] = "application/vnd.github.v3.diff"
        r = requests.get(f"{self.api_url}/repos/{repo}/pulls/{pr_number}", headers=headers, timeout=60)
        r.raise_for_status()
        return r.text

    def create_issue_comment(self, repo: str, issue_number: int, body: str):
        r = requests.post(
            f"{self.api_url}/repos/{repo}/issues/{issue_number}/comments",
            headers=self.headers,
            json={"body": body},
            timeout=30
        )
        r.raise_for_status()
        return r.json()
