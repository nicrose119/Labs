for number in range(5):
    print('Hello')

for number in range(0,11):
    print(number)

for number in range(10, -1, -1):
    print(number)

user_rates = input('On a scale of 1-10, how much do you love devCodeCamp? ')
print(user_rates)

for user_rates in range (int(user_rates)):
    print('devCodeCamp')

team = 'Packers'
for character in team:
    print(character)

for number in range(0, 100):
    if number % 3 == 0 and number % 5 == 0: 
        print('fizz buzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


hello = 0
while hello < 5:
    print('Hello')
    hello += 1
else:
    print('Heyyyy')


password = 'word!pass!7'
user_input = ('')

while user_input != password:
    user_input = input('Please enter your password ')
if user_input == password:
    print('User Validated')


