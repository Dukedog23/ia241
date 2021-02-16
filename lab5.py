"""
lab5 if statement
"""

#3.1

alien_color= 'red'

if alien_color == 'red':
    print('player earned 5 points')

#3.2

if alien_color == 'green':
    print('player just earned 5 points')
else:
    print('player just earned 10 points')
    
#3.3

favorite_fruits= ['apple', 'strawberry', 'orange']

if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'orange' in favorite_fruits:
    print('You really like oranges!')
    
#3.4

age=31
if age<10:
    print('you are a kid')
elif age<20:
    print('you are a teenager')
else:
    print('you are an adult')
if age >65:
    print('you are an elder')