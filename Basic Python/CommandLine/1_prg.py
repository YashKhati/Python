from sys import argv
'''
print(type(argv))
print(argv)  # ['1_prg.py', '10', '20', '30']

print(argv[1:]) # print only inputted numbers
print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])

list = eval(input("Enter list of values : "))
print(type(list))

print("Number of command line arguments : ",len(argv))
print("List of command line arguments : ",argv)
print("Command line arguments one by one : ")

for x in argv:
    print("x = ",x," type(x) = ",type(x))

sum=0
args=argv[1:]
for x in args:
    n= int(x)
    sum += n
print("Sum of arguments : ",sum)
'''
'''

# taking command line argument as 1 element
# enclose element in double quotes ex :  py 1_prg.py "yash khati"
# or  py 1_prg.py "yash khati"
print(argv[1])

'''

'''

# py 1_prg.py 10 20
print(argv[1]+argv[2]) # output : 1020
print(int(argv[1])+int(argv[2])) # output : 30

'''
''' 

# py 1_prg.py 10 20
# print(argv[100]) # error
print((argv[20:100])) # no error

'''
