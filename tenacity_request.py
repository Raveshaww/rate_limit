import requests
from tenacity import retry
from tenacity.wait import wait_exponential

# Exponential backoff starting after four seconds, ending at 60 seconds
@retry(wait=wait_exponential(multiplier=1, min=4, max=60))
def request_wrapper(url : str) -> None:
    response = requests.get(url)
    print(f"\nStatus code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    response.raise_for_status()  # Raise an error for bad responses

print("We expect the first request to be successful")
request_wrapper("http://127.0.0.1:8000")


print("We expect the second request to be rate limited, but tenacity will attempt to retry it.")
request_wrapper("http://127.0.0.1:8000")

print("\nUseful stats:")
print(f"start_time: {request_wrapper.statistics['start_time']}")
print(f"attempt_number: {request_wrapper.statistics['attempt_number']}")
print(f"idle_for: {request_wrapper.statistics['idle_for']}")
print(f"delay_since_first_attempt: {request_wrapper.statistics['delay_since_first_attempt']}")