import time
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_single(url: str) -> None:
    
    print("fetching ...")
    requests.get(url)
    print("Fetched!")
    
time_start = time.time()

for _ in range(100):
    fetch_single(url)
    
time_end = time.time()
print(f'\nAll done! took {round(time_end - time_start, 2)}, seconds')