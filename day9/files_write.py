#writing a file(w)
#when we use "w" the content which is present before it will we get erased and new content will be added
file=open("sample.txt","w")
file.write("hello, this is a sample text!\nhello this is second line")
file.close()

#2nd method -by below it will automatically closed after writing
with open("sample.txt","w") as file:
    file.write("this is the second line")
