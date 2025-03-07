import threading
import time
 
print("Main thread Started")

def single_task():
    print("sub Task started")
    time.sleep(2)
    print("Sub task completed")

def single_task2():
    print("Sub task2 is started")
    time.sleep(3)
    print("sub task2 is completed")

thread=threading.Thread(target=single_task)
# thread2=threading.Thread(target=single_task2)
thread.start()
thread.join()           #If we don't use join(), the main thread will get executed without completion of sub task
# thread2.start()
# thread2.join() 
print("Main thread execution completed")