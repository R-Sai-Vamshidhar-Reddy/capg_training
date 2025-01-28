class Employee:
    def __init__(self,name,salary):
        self._name=name                 #use __ for private key and use _ protected 
        self._salary=salary
    def allowance(self,bonus,nyt_shifts,travel,food):
        self._salary=self._salary+bonus+nyt_shifts+travel+food
        return self._salary
    def deductions(self,gst,pf):
        self._salary=self._salary-pf
        self._salary=(self._salary*(gst/100))
        return self._salary

    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
    
emp=Employee("Sai",20000)
print("Salary before update: ",emp.get_salary())
bonus=float(input("enter bonus: "))
nyt_shifts=float(input("Enter nyt_shits allowances: "))
travel=float(input("Enter travel allowances:"))
food=float(input("Enter food allowances: "))
emp.allowance(bonus,nyt_shifts,food,travel)
gst=int(input("Enter the gst in %: "))
pf=float(input("Enter pf detuction amount: "))
emp.deductions(gst,pf)

print("Salary after update: ",emp.get_salary())