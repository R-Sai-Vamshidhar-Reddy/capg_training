import threading
import time
import queue

def producer(q):
    for i in range(5):
        item=f"Item {i}"
        print(f"Producing {item}")
        q.put(item)
        time.sleep(1)
def consumer(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(f"consuming {item}")
        q.task_done()

q=queue.Queue()
producer_thread=threading.Thread(target=producer,args=(q,))
consumer_thread=threading.Thread(target=consumer,args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
producer_thread.join()

print("All threads have finished.")