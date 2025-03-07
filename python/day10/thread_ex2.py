import threading
import time
 
print("Main thread Started")

def even_odd(n):
    
    for i in range(1,n+1):
        if(i%2==0):
            print(f"{i} is even")
            time.sleep(1)
        else:
            print(f"{i} is odd")
            time.sleep(1)
n=int(input("Enter number of iterations: "))
thread=threading.Thread(target=even_odd(n))
thread.start()
thread.join()           #If we don't use join(), the main thread will get executed without completion of sub task
print("Main thread execution completed")