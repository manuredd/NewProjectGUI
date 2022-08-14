import requests
from pprint import pprint
import sys

url = "https://api.github.com/user/repos"
payload = '{"name": "teest", "private": "true"}'
token = "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"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "token " + token,
}
if __name__ == "__main__":
    r = requests.post(url, data=payload, headers=headers)

pprint(r.json())