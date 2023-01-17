"""
# pass keyword to define function later
def hello_fun():
    pass
"""


def hello_fun():
    print('hello yash')


hello_fun()


def hello_fun1():
    return "Hello yash"


hello_fun1()
print(hello_fun1())


def hello_fun2(greeting, name='Yash'):
    return '{}, {}'.format(greeting, name)


print(hello_fun2('hello'))
print(hello_fun2('hello', 'ayush'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Yash', age=22)

courses = ['Maths', 'Science']
info = {'name': 'Yash', 'Age': 22}

student_info(courses,info)
student_info(*courses, **info)

