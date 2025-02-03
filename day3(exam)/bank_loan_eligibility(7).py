def check_eligibility_salary(s):
    if(s>=15000):
        return True
    else:
        print("Your loan is rejected as your salary is less than 15000")

def check_eligibility_age(a):
    if(a>=21):
        return True
    else:
        print("Your loan is rejected as you are under age")
def check_eligibility_credit_score(c):
    if(c>=700):
        return True
    else:
        print("Your loan is rejected as your credit score is low")
def main():
    print("Please enter the details below")
    salary=float(input("Enter the salary of your's: "))
    age=int(input("enter your age: "))
    credit_src=float(input("Enter the credit score out of 1000: "))
    if(check_eligibility_salary(salary) and check_eligibility_age(age) and check_eligibility_credit_score(credit_src)):
        print("Your loan is approved as it meet all our condition")
main()