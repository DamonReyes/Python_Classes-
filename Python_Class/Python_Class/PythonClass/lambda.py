# identificador   argumento   expresion
palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))


# WHITHOUT FILTER
my_list = [1,4,5,6,9,13,19,21]
odd = [i for i in my_list if i %2 != 0]
print(odd)
# WHIT FILTER
my_list = [1,4,5,6,9,13,19,21]
#                  recibe una funcion y un iterable
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)

# WHITHOUT MAP
my_list = [1,2,3,4,5]
squares = [i**2 for i in my_list]
print(squares)
# WHIT MAP
my_list = [1,2,3,4,5]
squares = list(filter(lambda x: x%2 != 0, my_list))
print(squares)

# WHITHOUT REDUCE
my_list = [2,2,2,2,2]
all_mult = 1
for i in my_list:
    all_mult = all_mult * i
print(all_mult)
# WHIT REDUCE
from functools import reduce
my_list = [2,2,2,2,2]
all_mult = reduce(lambda a, b: a * b, my_list)
print(all_mult)