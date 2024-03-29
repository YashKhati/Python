def square(x):
    return x * x


def cube(x):
    return x * x * x


'''
f=square(5)
print(5)
print(f)
'''

f = square

# now we can terat f as square() function
print(f)
print(square)

print(f(5))
print(square(5))

'''
Higher Order fun : A fun that accepts other functions as agruments or returns
other fun as result
'''


# taking  function as argument
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append((func(i)))
    return result


squares_arr = my_map(square, [1, 2, 3, 4, 5])
print(squares_arr)

cubes_arr = my_map(cube, [1, 2, 3, 4, 5])
print(cubes_arr)

# returning function from another function

def logger(msg):
    def log_message():
        print('Log:',msg)
    return  log_message


log_hi = logger('Hi!')  # logger fun returns log_message function
log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
