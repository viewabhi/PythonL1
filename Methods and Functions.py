mylist = [1,2,3,4,5,6,7,8]

mylist.append(9)

print(mylist)

mylist.pop()

print(mylist)

#functions

def say_hello(name='Name'):
    """
    :return:this function will print hello...just that nothing else...this is a stupid function..this is for
    people who does not understand my code
    """
    return 'hello ' +name
#you can use both print and return the result using return to you later in the code
result = say_hello('Trishla')
print(result)

def adding(a,b):
    """
    :param a:can be any number
    :param b:this can also be any number
    :return:the sub of both
    """
    return a+b

result = adding(1.32,4.33)

print(result)

print('Pig Latin')

def pig_latin(word):
    """
    :param word: can be any word. if start with vovel add 'ay' to the end, if does not start with vovel
    add first letter to the end and add 'ay' after that
    :return:Funny!!
    """
    if word[0] in 'aeiou':
        pig_word = word+'ay'
    else:
        pig_word = word[1:]+word[0]+'ay'
    result = pig_word
    print(result)

pig_latin('abhishek')
pig_latin('trishla')
pig_latin('asha')
pig_latin('akshat')
pig_latin('bhanu')

print('*args and *kwargs')
#Arguments and Keyword Arguments


#*args return a Tuple
def myfunc(*args): #you can use any word in place of args
    return sum(args) * 3.75

myfunc(10,20,30,40,50)
print(result)

#**kwards return a dictionary
def myfunc2(**kwargs):#you can use any work in place of kwargs
    print(kwargs)

myfunc2(fruit='apple',veggie='Lettuce',game='Basketball')

#We can use args and kwargs in combination also

def myfunc3(*args,**kwargs  ):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[1],kwargs['food']))

myfunc3(10,20,30,food='Pizza',fruit='I like only Juice',meat='chorizo')

#We can use any number of variables without defining in advance


def myfunc4(name):
    res = ''
    for i in range(len(name)):
        if not i % 2:
            res = res + name[i].upper()
        else:
            res = res + name[i].lower()
        print(res)
#how to print only once ?? Need to check

myfunc4('Abhishek')







