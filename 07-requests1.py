import requests
url = "https://icanhazdadjoke.com"

# accepts only the plain text portion of the response:  
# plain test
res = requests.get(url, headers={"Accept": "text/plain"})

# other types are "text/html", "application/json"
# html
#res = requests.get(url, headers={"Accept": "text/html"})

#json
res = requests.get(url, headers={"Accept": "application/json"})

#print(f"your request to {url} returned a status code of {res.status_code}")

# output the response - print plain text and html
print(res.text)

# output the response in json format
data = res.json()

print(data)

print(data["joke"])
