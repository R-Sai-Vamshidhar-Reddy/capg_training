import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running..")
        time.sleep(1)

daemon_thread=threading.Thread(target=daemon_task,daemon=True)
daemon_thread.start()
time.sleep(3)           #until the main thread is running the deamon thread wil also
                            #run if sleep time is 0 then deamon thread will not get executed
print("Main thread exiting")