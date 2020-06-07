print('Python Statements Class!')

loc = 'Aguascalientes'
if loc == ('Canada'):
    print('It is very cold here!')
elif loc == ('New York'):
    print('Why is there so much ice!')
else:
    print('What a pleasent Climate!')
# How to use if, elif and else
print('IF ELSE ELIF SOLUTION')

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist2 = ['q','w','e','r','t','y','u','i','o','p']
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
d = {'k1': 'Abhishek', 'k2': 'Trishla', 'k3': 'Akshat'}

for _ in mylist1:
    print('I will learn Python!')
# _ can be used in place of variable names
print('LIST PRINTING SOLUTION')

list_sum = 0
for num in mylist1:
    list_sum = list_sum + num

print(list_sum)
# printing the sum of a list
print('LIST SUM PRINTING SOLUTION')

for num in mylist1:
    if num % 2 == 0:
        print(f'even num: {num}')
    else:
        print(f'odd num: {num}')
# indentation is very important
# f string literal can ve used with it to add additional text
print('F STRING LITERAL USAGE')

for a, b in mylist:
    print(a)
# tuple unpacking
print('TUPLE UNPACKING')
for key, value in d.items():
    print(value)
# dictionary unpacking
# dictionaries are technically unordered

x = 0

while x < 5:
    print(x)
    x = x + 1
    if x == 3:
        # break is used to break of the current loop
        continue  # is used to continue with the same condition
else:
    pass  # keyword used if you do not have a else condition
    # print('List sum is greater than 40')
print('HOW TO USE BREAK CONTINUE AND PASS')

for num in range(3,10,3):
    print(num)
print('HOW TO USE RANGE FUNCTION')

list(range(3,10,3))
#how to move range to a list

alpha_list = 'qwerty'
index_count = 0
for _ in enumerate(alpha_list):
    #print('At index count {} the letter is {}'.format(index_count,_))
    print(_)
    #index_count += 1
print('ENUMERATE IS USED TO PRINT ANY ITERABLE OBJECT AND ITS INDEX COUNTER')

for item in zip(mylist,mylist1,mylist2):
    print(item)
print('HOW TO USE THE ZIP FUNCTION TO ADD 2 LISTS, CAN BE DONE WITH MORE THAN 2 LISTS')

print(max(mylist1))
print(min(mylist1))
print(1 in mylist1)
print('q' in mylist2)
print('k3' in d)
print('Abhishek' in d.values())

print('HOW TO USE MIN, MAX, IN ON LIST,DICT AND TUPE')

from random import shuffle
shuffle(mylist2)
print(mylist2)
shuffle(mylist2)
print(mylist2)

from random import randint
result = randint(0,100)
print(result)
print('HOW TO IMPORT LIBRARY')

#how to take user input
name = str(input('What is your name?'))
print(name)
print(type(name))
DOB = int(input('What is your date of birth (DDMMYYYY)?'))
print(DOB)
print(type(DOB))


print('LIST COMPREHENSION')

mylist3 = [x for x in name]
print(mylist3)
#this is also called flattened out for loop

mylist4 = [y**2 for y in range(1,11) if y%2==1]
print(mylist4)

clecius = [10,20,40,60,100]
fahrenheit = [((9/5)*temp + 32) for temp in clecius]
print(fahrenheit)

mylist5 = [x*y for x in [2,3,4] for y in [5,6,7]]
print(mylist5)

#if and else can be used in list comprehemsion

mylist5 = []
for x in clecius:
    for y in mylist1:
        mylist5.append(x*y)
print(mylist5)
# some pattern can be created with this when using print in same loop as for :)




