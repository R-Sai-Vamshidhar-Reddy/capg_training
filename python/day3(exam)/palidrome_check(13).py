def display(ans):
    if(ans):
        print("The given input is a palindrome")
    else:
        print("The given input is not a palindrome")
def check_palindrome(text):
    rev_text=text[::-1]
    if(text==rev_text):
        return True
    else:
        return False
def main():
    n=int(input("Enter the number of inputs: "))
    if(n<=0):
        print("The inputs should be greater than 0")
    else:
        for i in range(n):
            text=input("Enter the string or number: ")
            ans=check_palindrome(text)
            display(ans)
main()