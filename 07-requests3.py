import requests

url = "http://172.107.178.62:3000/server/"

serv_name = input("Enter server name: ")

res = requests.get(
    url + serv_name,
    headers={"Accept": "application/json"},
)

data = res.json()

print(data[0]['server_name'], data[0]['prim_appl_info'])
#print(data["results"])

# print(data["joke"])
# print(f"status: {data['status']}")

