import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
userId = data["userId"]
id = data["id"]
title = data["title"]
completed = data["completed"]

print(f"userId: {userId}")
print(f"id: {id}")
print(f"title: {title}")
print(f"completed: {completed}")
