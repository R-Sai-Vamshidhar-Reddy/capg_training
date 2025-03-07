def display(name,t_marks,percent,grade):
    print(f"total marks out of 500 are: {t_marks}")
    print(f"Total percentage is: {percent} %")
    print(f"grade of {name} is: {grade}")
def grade(m):
    if(m>=90):
        return "A"
    elif(75<=m<90):
        return "B"
    elif(60<=m<75):
        return "C"
    elif(40<=m<60):
        return "D"
    else:
        return "Fail"
def percentage(t_marks):
    per=(t_marks/500)*100
    return round(per,2)
def calcu(marks):
    sm=0
    for i in marks:
        sm+=i
    return sm
def main():
    name=input("Enter the student name: ")
    marks=list(map(int,input(f"Enter the 5 subject marks of the {name}:\n").split()))
    t_marks=calcu(marks)
    percent=percentage(t_marks)
    grad=grade(percent)
    display(name,t_marks,percent,grad)
main()