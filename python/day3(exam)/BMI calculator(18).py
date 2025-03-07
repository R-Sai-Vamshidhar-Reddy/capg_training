def display(ans):
    print(f"accourding to given weight and height you are {ans}")
def calculate(w,h):
    val=w/(h*h)
    if(val<18.5):
        return "Underweight"
    elif(val>=18.5 and val<=24.9):
        return "Normal"
    elif(val>=25 and val<=29.9):
        return "Overweight"
    elif(val>=30 and val<=34.9):
        return "Obese"
    else:
        return "Extreme Obese"
def main():
    print("Enter the below details")
    weight=int(input("Enter the weight in kg: "))
    height=float(input("ENter the height in meters: "))
    ans=calculate(weight,height)
    display(ans)
main()