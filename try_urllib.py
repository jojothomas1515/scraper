import urllib3

http = urllib3.PoolManager()

req = http.request("GET", "https://www.google.com/search?q=donald+trump")
print(req.status)

with open("index.html", "w") as index:
    index.write(str(req.data))