"""
print("hello bitches")
print("o----")
print(" ||||")
print("_" _ 10) # this is called an expression, a statement that evaluates to some value, so 10 stars in this case
is_published = True # variables must be snakecase, booleans must be capitalized

# Exercise:

name = "John Smith"
age = 20
is_new_patients = False

# Exercise:

name = input("Name: ")
color = input("Color: ")
print(name, "likes", color)

birth_year = input("Birth year: ")
print(2022 - int(birth_year)) # `birth_year` comes as a string and must be converted to evaluate

# Exercise:

user_weight = input("What is your weight in lbs: ")
lbs_to_kg = float(user_weight) / 0.453592
print("You weigh", "{:.2f}".format(lbs_to_kg), "in kg!") # format the decimal with 2 precision

# if wanting a one liner of initiating a variable in the same line, can do this

# the `lbs_to_kg` is listed as red because it's dangerous and may crash

print("You weigh", "{lbs_to_kg:.2f}".format(lbs_to_kg=(float(user_weight) / 0.453592)), "in kg!")

course = 'Python for Beginners'
print(course[-2]) # "r"
print(course[1:]) # "ython for Beginners"
print(course[0:5]) # "Pytho"
print(course[1:-1]) # "ython for Beginner"

first = "jotaro"
last = "kujo"
message = f'{first} {last} is a stand user!'
print(message)

name = "joseph the stand user"
print(len(name)) # functions are general usage, for strings, ints, almost anything
name.upper() # methods are for specific usage, this one in particular, for strings
print(name.title()) # "Joseph The Stand User"
print(name.find("o")) # "1"
print(name.find("y")) # "-1"
print(name.replace("joseph", "jojo")) # "jojo"
print("jo" in name) # True

import math
number = -5
print(math.fabs(number)) # "5.0"

price = 1000000
buyer_has_good_credit = False
if buyer_has_good_credit:
price = price _ 0.9
else:
price = price _ 0.8
print("down payment is:", "${:.2f}".format(price)) # down payment is: $800000.00

name = "captain marvel"
if len(name) < 3:
print("name must be more than 3 characters")
elif len(name) > 50:
print("name must be less than 50 characters")
else:
print("name is good")

weight_type = input("(L)bs or (K)g: ")
weight = float(input("Weight: "))
lb_to_kg = 0.453592
kg_to_lb = 2.20462
if weight_type.upper() == "L":
print(f'You are {weight _ lb_to_kg:.1f} kilograms')
elif weight_type.upper() == "K":
print(f"You are {weight _ kg_to_lb:.1f} pounds")

secret = 9
tries_limit = 3
tries = 0
while tries < tries_limit:
guess = int(input(f"You have {tries_limit - tries} tries left! Guess the number: "))
tries += 1
if guess == secret:
print("You won!")
break
else:
print("You lost, sorry!")

user_input = ""
car_started = False
while True: # no need to put `user_input != "quit"` since the only way to break out is by quiting
user_input = input(">")
if user_input == "start":
if not car_started:
print("car started...ready to go!")
else:
print("car already is on!")
car_started = True
elif user_input == "stop":
if car_started:
print("car stopped")
else:
print("car already stopped!")
car_started = False
elif user_input == "quit":
break
elif user_input == "help":
print("start - to start the car\nstop - to stop the car\nquit - to exit")
else:
print("I don't understand that...")

BOOKMARK 1:42:49

"""
