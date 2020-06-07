# If both numbers even, print the lower number
# If any of the numbers is odd, print the higher

def less_of_two(a, b):
    if a % 2 != 0 or b % 2 != 0:
        if a > b:
            print(a)
        else:
            print(b)
    else:
        if a > b:
            print(b)
        elif b > a:
            print(a)


less_of_two(3, 19)
less_of_two(2, 24)


# Take input as 2 word string
# True = both word begin with the same letter
# False = both word begin with different letter

def animal_crackers(text):
    first_word = text.upper().split()[0]
    second_word = text.upper().split()[1]
    if first_word[0] == second_word[0]:
        print(True)
        return True
    else:
        print(False)
        return False

animal_crackers('abhishek Sharma')
animal_crackers('Somitra Sanyal')

# Input 2 integers
# If sum is 20 or one of them is 20, return true
# else return false

def integer_check(a,b):
    if a==20 or b ==20 or a+b==20:
        print(True)
        return True
    else:
        print(False)
        return False

integer_check(10,10)
integer_check(20,1)
integer_check(7,4)

# Write a function that capitalize 1st and 4th letter of a name

def capi_onenfour(text):
    response = text[0].upper() + text[1:3] + text[3].upper() + text[4:]
    print(response)
# we can also use .capitalize by seperating first and second half and then concatinating them\

capi_onenfour('abhishek')
capi_onenfour('macdonalds')

# Given a scentence, return a scentence with the words reversed

def master_yoda(text):
    word_list = text.split()
    reversed_word = word_list[::-1]
    print(' '.join(reversed_word))

master_yoda('Abhishek Is A Good Boy')

#Give an integer n
#True if n is under 10 or 100 or 200
#Else False

def num_check(n):
    #if n in range(90,110) or n in range(190,210): #we can also use absolute value of the expression
        if (abs(100-n)<=10) or (abs(200-n)<=10):
            print(True)
            return True
        else:
            print(False)
            return False

num_check(88)

#Return true if in a list there are two 3's next to each other

def num_check(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and  nums[i+1]==3:
            print(True)
        else:
            print(False)

num_check([1,2,3,4,5,6,3,3])

#Paper Doll problem
#Input string every character should have 2 characters

def string_thrice(text):
    result=''
    for char in text:
        result+=char*3
    print(result)

string_thrice('Abhishek')


#Given 3 integers between 1 and 11
#If sum is less than == 21, return sum
#if sum is greater tha 21 and there is 11, reduce sum by 10
#if sum after adjustment is greater than 21, return 'BUST'

def blackjack(a,b,c):
    sum=a+b+c
    if sum<=21:
        print(sum)
    elif 11 in [a,b,c] and sum>=21:
        print(sum-10)
    else :
        print('BUST')

blackjack(110,11,1)

#Summer of 69
#return sum of numbers in an array
#ignore any patch starting with a 6 and ending with 9, every 6 is followed by at least one 9
#return 0 for no numbers

def summer_of_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)

summer_of_69([1,2,3,4,5,6,7,8,9,1])

#Write a function that taken in integers and check if 007 in consecutive order, if yes return true

def spy_check(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code = code.pop(0)

        return len(code) == 1

spy_check([1,0,0,7,5,7])

#Return number of primes that exist between a range and including the numbers
#complicated for now, need to find a simple way of writing it

def prime_check(num):
    #if number less than 2, as 0 and 1 are not prime, no the result will be 0
    if num<2:
        return 0
    #this is to store prime number
    primes = [2]
    #this is a counter
    x = 3
    while x <= num:
        #x is going through every number from x up to the last number and skipping the even numbers
        #to check if it is prime
        for y in range(3,x,2):
            if x%y==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

prime_check(30)
prime_check(100)








