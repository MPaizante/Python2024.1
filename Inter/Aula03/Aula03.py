import requests

r = requests.get("https://api.datamuse.com/words", params={"rel_rhy": "funny"})
print(r.text)
print(r.url)

print('------------------------------------------------------------------------------')
