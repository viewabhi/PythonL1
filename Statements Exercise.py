print('new exercise')

#print all the words start with s using for, split and if
st = 'Print only the words that start with s in this scentence'
for word in st.split():
    if word[0] == 's':
        print(word)

#range to print even number from 1 to 10
for num in range(1,11):
    if num%2==0:
        print(num)

#using list comprehension print all numbers between 1 to 50 which are divisble by 3
oddnum = [x for x in range(1,50) if x%3==0]
print(oddnum)

#print even if the length of the word is even
text = 'print every word in this scentence that has an even number of letters'
for word in text.split():
    if len(word) % 2 == 0:
        print(word)



#write program to print integers from 1 to 100, for multiple of 3 print fizz, for mutilpe of 5 print buzz
#and for multiple of both 3 and 5 print fizzbuzz
for x in range(1,100):
    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(x)

#use list comprehension to create a list of the first letter of every word in the string
st = 'create a list of the first letters of every word in this string'
ste = [x[0] for x in st.split()]
print(ste)
