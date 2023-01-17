import my_module as mm
# from my_module import find_index        -> only import find_index function
# from my_module import find_index,test    -> only import find_index function and test variable

courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Physics')
print(index)
