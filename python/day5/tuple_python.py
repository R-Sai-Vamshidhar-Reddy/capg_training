t1=() #for declaring tuple use () braces
print("Empty tuple t1: ",t1)


t2=(1,) #if you want to declare tuple with single element mandetorily use ","
print("Tuple with single element t2: ",t2)

t3=(1,"ni",1.2,3)
print("Tuple with multiple elements t3: ",t3)


t3_1=1, "ni", 3.2, 1
print("Tuple without braces t3_1:" ,t3_1) #giving elements separated by comma's will give output as tuple


t4=("hello",("hi","your_name"))
print("nested tuple t4: ",t4)

t5=tuple("vara")
print("convert other data type \"vara\" into tuple t5: ",t5)

print("retriving element from t5[1]: ",t5[1])
print("Retriving elemnt from nested tuple t4[1][1]",t4[1][1])

t6=(1,"hi",2,"hello")
print("tuple slicing of t6[1:3]",t6[1:3])

print("Getting length of tuple t6: ",len(t6))

print("repeating t6 2 times: ",t6*2)
