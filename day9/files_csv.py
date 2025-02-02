with open("sample.csv","w") as file:
    file.write("id, name, age\n")
    n=int(input("Enter number of inputs: "))
    for i in range(n):
        id,name,age=input("Enter id, name , age: ").split()
        file.write(f"{id}, {name}, {age}\n")


    