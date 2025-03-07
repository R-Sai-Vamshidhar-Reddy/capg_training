def display(ans):
    if(ans):
        print("Your password is strong")
    else:
        print("Your pasword is not strong please update with new one")
def length(n):
    if(len(n)>=8):
        return True
    else:
        return False
def upper(n):
    cnt=0
    for i in n:
        if(i.isupper()):
            cnt+=1
    if(cnt!=0):
        return True
    else:
        return False
    
def lower(n):
    cnt=0
    for i in n:
        if(i.islower()):
            cnt+=1
    if(cnt!=0):
        return True
    else:
        return False
def digits(n):
    cnt=0
    for i in n:
        if(i.isdigit()):
            cnt+=1
    if(cnt!=0):
        return True
    else:
        return False
def special_char(n):
    c=0
    for i in n:
        if(31<ord(i)<48) or (57<ord(i)<65 or (90<ord(i)<97) or (122<ord(i)<127)):
            c+=1
    if(c!=0):
        return True
    else:
        return False
def password_checker(n):
    if (length(n) and upper(n) and lower(n) and digits(n) and special_char(n)):
        return True
    else:
        return False
def main():
    n=input("Enter the password: ")
    ans=password_checker(n)
    display(ans)
main()