import requests
from pprint import pprint
import subprocess

txt = open("/Users/mredd/Misc/token.txt", "r")
url = "https://api.github.com/user/repos"
payload = '{"name": "teest", "private": "true"}'
token = txt.read()
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "token " + token,
}
#if __name__ == "__main__":
#    r = requests.post(url, data=payload, headers=headers)
subprocess.run("cd /Users/mredd")
#pprint(r.json())

#testing