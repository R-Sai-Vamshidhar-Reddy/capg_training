import pandas as pd
class Details:
    def enter_details(self,id,name,age):
        with open("data.csv","a") as file:
            file.write(f" {id}, {name}, {age}\n")

file1=open("data.csv","w")
file1.write("id, name, age\n")
file1.close()
obj=Details()
n=int(input("Enter number of details you want to enter: "))
for i in range(n):
    id=int(input("\nEnter the id: "))
    name=input("Enter the name: ")
    age=input("Enter the age: ")
    obj.enter_details(id,name,age)

rd=pd.read_csv("data.csv")
df=pd.DataFrame(rd)
print(df)
