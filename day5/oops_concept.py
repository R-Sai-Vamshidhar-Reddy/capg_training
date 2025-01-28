# class employee():


#     def employee_login(emp_id,login_time):

#     def employee_logout(emp_id,logout_time):

#     def employee_details(emp_id,emp_name,emp_age,emp_department,dept_id):

#     def employee_payout(emp_id,salary,bonus):

    
##Encapculation
    
class Employee:
    def __init__(self,name,salary):
        self._name=name                 #use _ for private key
        self._salary=salary
    
    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
    
emp=Employee("Sai",20000)
print("Salary before update: ",emp.get_salary())
emp.set_salary(input("Enter the salary: "))
print("Salary after update: ",emp.get_salary())
    



