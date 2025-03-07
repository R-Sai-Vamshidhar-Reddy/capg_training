#using apppend method -it append the new data to the previous data
file1=open("sample.csv","a")
file1.write("id, name, age\n")
with open("sample.csv","a") as file:
    n=int(input("Enter number of inputs: "))
    for i in range(n):
        id,name,age=input("Enter id, name , age: ").split()
        file.write(f"{id}, {name}, {age}\n")