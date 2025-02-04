import threading
import time
class ticket_booking:
    def __init__(self,available_tickets):
        self.available_tickets=available_tickets
    def booking(self,name,lock):
        with lock:
            if(self.available_tickets>=1):
                print(f"Ticket is booked for {name}")
                self.available_tickets-=1
                time.sleep(1)

            else:
                print(f"Tickets are not available for {name}")

                
ticket=ticket_booking(2)
lock=threading.Lock()
lst=["Vara","Sai","vaishu"]

threads=[]
for name in lst:
    thread=threading.Thread(target=ticket.booking,args=(name,lock))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()