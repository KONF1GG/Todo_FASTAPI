import requests

responese = requests.get('http://localhost:8000/hello_world')
print(responese.json())
print(responese.status_code)