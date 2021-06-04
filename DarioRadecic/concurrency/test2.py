import time
import requests
import concurrent.futures

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_single(url: str) -> None:
    
    print("fetching ...")
    requests.get(url)
    print("Fetched!")
    
time_start = time.time()

with concurrent.futures.ThreadPoolExecutor() as tpe:
    
    results = [tpe.submit(fetch_single, url) for _ in range(100)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    
time_end = time.time()
print(f'\nAll done! took {round(time_end - time_start, 2)}, seconds')