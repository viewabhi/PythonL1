#lambda expressions are functions that are named one time and used once and not used again
#map and filter are built into python

print('Learning about map function now')

def square_num(num):
    return num**2


my_nums = [1,2,3,4,5]

for item in map(square_num,my_nums):
    print(item)

my_nums = [1,2,3,4,5,6,7,8,9]

list(map(square_num,my_nums)) #another way to do this

def splicer(name):
    if len(name)%2==0:
        return 'even'
    else:
        return name[0]

names = ['Abhishek','Trishla','Bhanu','Asha','Akshat']

print(list(map(splicer,names)))

#so we do not execute the function insisde map because map eventually executes them#
#function itself is passed as an argument in map

print ('Learning about filter function now')

def check_even(num):
    return num % 2 == 0

my_nums1 = [1,2,3,4,5,6]
print(list(filter(check_even,my_nums1)))

for n in filter(check_even,my_nums1):
    print(n)


print('Learning lamba expression now')

#so if you know that you want to use a function only once and so them it is not required to use a def keyword
#what you can do is use the lambda keyword in place of def and function name

# This is how lambda function is written = square = lambda num: print(num ** 2)

print(list(map(lambda num:num**2,my_nums1)))

print(list(filter(lambda num:num%2==0,my_nums1)))

print(list(map(lambda name:name[0],names)))

print(list(map(lambda name:name[::-1],names)))

print(list(map(lambda name:name[::-2],names)))
