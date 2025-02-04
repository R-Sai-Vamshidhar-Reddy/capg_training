import threading
def get_result(l):
    result=sum(l)
    print(f"result is {result}")
lists=[ 
        list(range(10)),     #data chunks
        list(range(10,20)),
        list(range(20,40))
]
threads=[]
for l in lists:
    thread=threading.Thread(target=get_result,args=(l,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()