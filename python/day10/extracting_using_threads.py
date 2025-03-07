import threading
import requests
def find_url(url,results):
    response=requests.get(url)
    html_content=response.text
    results.append(f"Fetched {url}:\n{html_content}")
urls=["https://example.com"]

threads=[]
results=[]
for url in urls:
    thread=threading.Thread(target=find_url,args=(url,results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for result in results:
    print(result)

print("All url's fetched")