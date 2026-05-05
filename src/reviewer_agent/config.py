import os
class Config:
def **init**(self):
self.github_token = os.getenv("GITHUB_TOKEN", "")
self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
self.openai_base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
self.max_diff_chars = int(os.getenv("MAX_DIFF_CHARS", "12000"))
self.github_api_url = os.getenv("GITHUB_API_URL", "https://api.github.com")
def validate(self):
missing = []
if not self.github_token:
missing.append("GITHUB_TOKEN")
if not self.openai_api_key:
missing.append("OPENAI_API_KEY")
if missing:
raise RuntimeError("Missing env vars: " + ", ".join(missing))
