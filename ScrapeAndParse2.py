import requests

start_id = 1
end_id = 1000

base_url = "https://jsonplaceholder.typicode.com/todos/"

for todo_id in range(start_id, end_id + 1):
    url = f"{base_url}{start_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        print(f"ID: {data['id']}")
        print("Data:", data)  # Print the entire JSON data
        start_id = start_id +1
