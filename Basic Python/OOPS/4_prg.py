class Employee:
    # class variable
    raise_amount =1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # here it is not self.num_of_employee because it will increase
        # the num_of_employee for that instance only which does not make sense
        # Employee.num_of_employee will increment class variable value whenever
        # employee instance is created
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




print(Employee.num_of_emps)

emp1 = Employee('Yash','Khati',50000)
emp2 = Employee('Test','Case',60000)

print(Employee.num_of_emps)

