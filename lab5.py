'''
lab5 what if statement
'''
#3.1
alien_color = 'pink'
if alien_color == 'pink' :
    print('you just earned 5 points')
#3.2
alien_color = 'blue'
if alien_color == 'pink' :
    print('you just earned 5 points')
else: 
    print('you just earned 10 points')
#3.3
favorite_fruits = ['mango','strawberry','peach']
if 'mango' in favorite_fruits:
    print('you really like mango')
if 'kiwi' in favorite_fruits:
    print('you really like kiwi')
if 'apple' in favorite_fruits:
    print('you really like apple')
#3.4
age = 21
#if age < 10:
#    print('you are a kid')
#elif age < 20:
#    print('you are a teenager')
#else:
#    print('you are an adult')
#    if age > 65:
#        print('you are an elder')
if age >= 20:
    print('you are an adult')
    if age > 65:
        print('you are an elder')
elif age > 10:
    print('you are a teenager')
else:
    print('you are a kid')

