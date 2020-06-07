print(" LEGB Rule \n L - Local - Names assigned in any way within a function (def or lambda) and not declared global in that function \n E - Enclosing and function local - Names in the local scope of any and all enclosing functions (def or lambda), from innner to outer \n G - Global  - Names assigned in the top of a module file or declared as global in in def within the file \n B - Built in - Names pre assigned in the built in names module like open, range, SyntaxError")

#lambda num:num**2
#So num is a local function

#This is a global
name = 'Global String'

def greet():
    #This is a enclosing
    name = 'sammy'

    def hello():
        #This is a local
        name = 'I am local'
        print('Hello' +name)

        hello()

greet()

#Using the GLOBAL keywork you can change the value of a global variable inside a function
#GLOBAL keyword has to be used with caution as it affects the value of a variable ona  global level

print(' \n \n \n \n \n Now we are going to do the assignment')

def volume_sphere(rad):
    """
    volume of sphere is 4/3 pir r to the power 3
    :return: volume of sphere
    """
    volume = 4/3 * 3.14 * rad**3
    print("%.2f" % round(volume, 2))

volume_sphere(3)
volume_sphere(10)

def num_check(num,high,low):
    """
    check if the num if between high and low and return boolean
    :param num: num
    :param high: high range
    :param low: low range
    :return: boolean
    """
    if num<=high and num>=low:
        #print('Yes' + num + 'is in the range')
        print(True)
    else:
        #print('No' + num + 'is not in the range')
        print(False)


num_check(2,3,1)

statement = 'Hello Mr. Rodgers, How are you this fine Tuesday?'

def up_low_check():
    u = 0
    l = 0
    for i in statement:
        if (i>='a' and i<='z'):
            l = l + 1
        if (i>='A' and i<='Z'):
            u = u + 1
    print('Number of lower case letters is' ,l)
    print('Number of upper case letters is' , u)

up_low_check()

import collections

c = collections.Counter('upper' if x.isupper() else 'lower' if x.islower() else 'Space or symbols' for x in statement)
print(c)


#check how this can done by prod module from math
def multi_ply(a,b,c,d):
    multi_result = a*b*c*d
    print(multi_result)

multi_ply(1,2,3,-4)


def palindrome(str):
    str = str.lower()
    if str == str [::-1]:
        print('It is a Palindrome')
    else:
        print("Don't you know what is a Palindrome?")


palindrome('Helleh')
palindrome('Malayalam')

