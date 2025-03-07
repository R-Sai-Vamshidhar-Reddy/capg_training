#reading a file(r)
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#2nd method -by below it will automatically closed after reading
with open("sample.txt","r") as file:
    print(file.read())

#reading line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())