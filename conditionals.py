driving_age = "16"
user_age = input("How old are you? ")
print(int(user_age))

if (user_age >= driving_age):
    print("You are legally able to drive!")
else:
    print("You are not old enough to drive yet.")

#Task2: Random Number
import random
number = random.randint(0,11)
print(number)

if number <= 2:
    print("0 or 1 or 2")
elif number in range(3,5):
    print("3 or 4 or 5")
elif number in range(6,8):
    print("6 or 7 or 8")
else:
    print("9 or 10")

#Task3: NFL Teams
user_team = input("Name your favorite NFL team ")
print(user_team)

if user_team == "Bears":
    print("Quarterback much?")
elif user_team == "Vikings":
    print("Loud Noises!")
elif user_team == "Lions":
    print("LOL! They bad!")
elif user_team == ("Packers"):
    print("Best team in the world! Actually the universe!")
else:
    print("Who are they?!")
    