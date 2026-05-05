import requests
class LLMClient:
def **init**(self, api_key: str, base_url: str, model: str):
self.api_key = api_key
self.base_url = base_url.rstrip("/")
self.model = model
def chat(self, messages, temperature=0.2):
r = requests.post(
f"{self.base_url}/chat/completions",
headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
json={"model": self.model, "messages": messages, "temperature": temperature},
timeout=120
)
if r.status_code -ge 400:
raise RuntimeError(f"LLM error {r.status_code}: {r.text[:500]}")
return r.json()["choices"][0]["message"]["content"]
