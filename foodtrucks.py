import requests

url = "https://data.sfgov.org/resource/bbb8-hzi6.json"
response = requests.get(url)
if response.status_code == 200:
    print response.text
