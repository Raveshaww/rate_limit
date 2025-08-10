import requests


status_code = 0
while status_code != 429:
    response = requests.get("http://127.0.0.1:8000")

    print(f"Status code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    status_code = response.status_code