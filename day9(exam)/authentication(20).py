from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def login(self):
        return f"\n{self.username} logged in using Google."

    def logout(self):
        return "Logged out from Google account.\n"

class FacebookAuth(UserAuthentication):
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def login(self):
        return f"{self.username} logged in using Facebook."

    def logout(self):
        return "Logged out from Facebook account."

# Example usage
user_name=input("Enter user name: ")
password=input("Enter the password: ")
google_auth = GoogleAuth(user_name,password)
facebook_auth = FacebookAuth(user_name,password)

print(google_auth.login())
print(google_auth.logout())
print(facebook_auth.login())
print(facebook_auth.logout())