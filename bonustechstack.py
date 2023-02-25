import math 

#Task 1
for row in range(0,7):
    for column in range(0, row+1):
        print('#' ,end='')
    print()

print('')

#Task 2
for row in range(0,8):
    for column in range(0, 8):
        if (row % 2 == 0 and column % 2 == 0) or (column % 2 == 1 and row % 2 == 1):
            print('#', end =' ')
        else:
            print(' ', end = ' ')
    print()

print('')

#Task 3
user_number = input('Enter your favorite number ')
print(len(str(user_number)))

print('')

#Task 4
print(math.factorial(12))
print(math.factorial(7))
print(math.factorial(9))
print(math.factorial(8))
print(math.factorial(6))

print('')

#Task 5
import random
winning_number = (random.randint(1,20))
print(winning_number)

count_guess = 0

while count_guess < 6:
    user_guess = input('Guess a number between 1-20 ')
    if user_guess != winning_number:
        print(user_guess)
        count_guess = + 1
    else:
        print('You Win!!!')