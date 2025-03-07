s1=set() #empty set
print("Empty set: ",s1)


s2={"goa,pondi","delhi"}
print("Set with elements: ",s2)

print("Addding element in s2 :s2.add(\"island\"):",s2.add("island"))
print(s2)
print("removing element in s2 :s2.remove(\"island\"): ",s2.remove("island"))
print(s2)

set_1={1,2,3}
set_2={3,4,5}

Union=set_1|set_2
print("Union of set_1 and set_2: ",Union)

Intersection=set_1 & set_2
print("Intersection of set_1 and set_2: ",Intersection)

difference=set_1-set_2
print("Difference of set_1 and set_1: ",difference)

symatic_diff=set_1^set_2
print("symatic_ifference of set_1 and set_1: ",symatic_diff)