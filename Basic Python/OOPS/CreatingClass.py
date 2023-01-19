class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)



'''
emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)

emp1.first = 'Yash'
emp1.last = 'Khati'
emp1.email = 'Yash.Khati@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'Case'
emp2.email = 'Test.Case@company.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.email)
'''
emp1 = Employee('Yash','Khati',50000)
emp2 = Employee('Test','Case',60000)
print(emp1)
print(emp2)

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

# Calling member function using class name
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
