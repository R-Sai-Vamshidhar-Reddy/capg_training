def c_f():
    c=float(input("Enter the input in Celsius: "))
    f=round((c*1.8)+32,2)
    print(f"{c} celsius = {f} fahrenheit")
def c_k():
    c=float(input("Enter the input in Celsius: "))
    k=round(c+273.15,2)
    print(f"{c} celsius = {k} Kelvin")
def f_c():
    f=float(input("Enter the input in FahrenHeit: "))
    c=round((f-32)/1.8,2)
    print(f"{f} fahrenheit = {c} celsius")
def f_k():
    f=float(input("Enter the input in FahrenHeit: "))
    k=round(((f-32)/1.8)+273.15,2)
    print(f"{f} fahrenheit = {k} kelvin")
def k_c():
    k=float(input("Enter the input in Kelvin: "))
    c=round(k-273.15,2)
    print(f"{k} Kelvin = {c} celsius")
def k_f():
    k=float(input("Enter the input in kelvin: "))
    f=round(((k-273.15)*1.8)+32,2)
    print(f"{k} Kelvin {f} fahrenheit")
def main():
    print("please enter number for what you want to convert")
    print("Enter 1 for celsius to fahrenheit")
    print("Enter 2 for celsius to Kelvin")
    print("Enter 3 for fahrenheit to Celsius")
    print("Enter 4 for fahrenheit to Kelvin")
    print("Enter 5 for Kelvin to fahrenheit")
    print("Enter 6 for Kelvin to celsius")
    n=int(input())
    if(n<1 or n>6):
        print("Invalid input")
    else:
        if(n==1):
            c_f()
        elif(n==2):
            c_k()
        elif(n==3):
            f_c()
        elif(n==4):
            f_k()
        elif(n==5):
            k_f()
        else:
            k_c()
main()