class Employee:
    def __init__ (self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender


    def employee_details(self):
        print("Name of employee is", self.name)
        print("Age of employee is ",self.age)
        print("Salary of employee is", self.salary)
        print("Gender of employee", self.gender)

e1=Employee("Same",32,85000,"Male")

e1.employee_details()
