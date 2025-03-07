class Notification:
    def send(self):
        print("This is base class")

class EmailNotification(Notification):
    def send(self):
        print("This is Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("This is SMS Notification")


for msge in[EmailNotification(),SMSNotification()]:
    msge.send()