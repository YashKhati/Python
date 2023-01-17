nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = list()
# for i in nums:
#    my_list.append(i)
# print(my_list)

my_list = [n for n in nums]
print(my_list)

# square_list=list()
# for n in nums :
#    square_list.append(n*n)
# print(square_list)

square_list = [n * n for n in nums]
print(square_list)

# even_list=list()
# for n in nums:
#    if n%2 == 0:
#        even_list.append(n)
# print(even_list)

even_list = [n for n in nums if n % 2 == 0]
print(even_list)

# tuple_list=list()
# for letter in 'abcd':
#    for n in range(4):
#        tuple_list.append((letter, n))
# print(tuple_list)

tuple_list = [(letter, num) for letter in 'abcd' for num in nums]
print(tuple_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_dict = dict()
# for name,hero in zip(names,heros):
#    my_dict[name]=hero
# print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

nums = [1, 1, 2, 1, 3, 4, 5, 5, 5, 6, 7, 4, 7, 8, 9, 9]

# my_set = set()
# for n in nums:
#    my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)


