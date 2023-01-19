class Employee:
    # class variable
    raise_amount =1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        # self.pay = int(self.pay*1.04)
        # self.pay = int(self.pay * raise_amount) -> Error

        self.pay = int(self.pay * self.raise_amount)




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


# Accessinf Employee class variable

print(emp1.__dict__)
print(Employee.__dict__)

'''

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

'''

'''
# changes raise amount for all instances
Employee.raise_amount = 1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__)
print(Employee.__dict__)

'''

'''
# changes raise amount for only emp1 instances
emp1.raise_amount = 1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__)
print(Employee.__dict__)
'''


emp1.apply_raise()
print(emp1.pay)


