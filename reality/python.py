"""
# introduction
print("hello bitches")
print("o----")
print(" ||||")
print("_" * 10) # this is called an expression, a statement that evaluates to some value, so 10 stars in this case
is_published = True # variables must be snake_case, booleans must be capitalized

# establish variables
name = "John Smith"
age = 20
is_new_patients = False

# connecting input and output
name = input("Name: ")
color = input("Color: ")
print(name, "likes", color)

# calculate someone's age using birth year
birth_year = input("Birth year: ")
print(2022 - int(birth_year)) # `birth_year` comes as a string and must be converted to evaluate

# convert lbs to kg
user_weight = input("What is your weight in lbs: ")
lbs_to_kg = float(user_weight) / 0.453592
print("You weigh", "{:.2f}".format(lbs_to_kg), "in kg!") # format the decimal with 2 precision

# if wanting a one liner of initiating a variable in the same line, can do this
# the `lbs_to_kg` is listed as red because it's dangerous and may crash
print("You weigh", "{lbs_to_kg:.2f}".format(lbs_to_kg=(float(user_weight) / 0.453592)), "in kg!")

# manipulation of a list
course = 'Python for Beginners'
print(course[-2]) # "r"
print(course[1:]) # "ython for Beginners"
print(course[0:5]) # "Pytho"
print(course[1:-1]) # "ython for Beginner"

# formatting a string with variables
first = "jotaro"
last = "kujo"
message = f'{first} {last} is a stand user!'
print(message)

# methods to string
name = "joseph the stand user"
print(len(name)) # functions are general usage, for strings, ints, almost anything
name.upper() # methods are for specific usage, this one in particular, for strings
print(name.title()) # "Joseph The Stand User"
print(name.find("o")) # "1"
print(name.find("y")) # "-1"
print(name.replace("joseph", "jojo")) # "jojo"
print("jo" in name) # True

# importing a package and utilizing its methods
import math
number = -5
print(math.fabs(number)) # "5.0"

# if else statements part 1
price = 1000000
buyer_has_good_credit = False
if buyer_has_good_credit:
    price = price * 0.9
else:
    price = price * 0.8
print("down payment is:", "${:.2f}".format(price)) # down payment is: $800000.00

# if else statements part 2
name = "captain marvel"
if len(name) < 3:
    print("name must be more than 3 characters")
elif len(name) > 50:
    print("name must be less than 50 characters")
else:
    print("name is good")

# converting weight type depending on user input
weight_type = input("(L)bs or (K)g: ")
weight = float(input("Weight: "))
lb_to_kg = 0.453592
kg_to_lb = 2.20462
if weight_type.upper() == "L":
    print(f'You are {weight * lb_to_kg:.1f} kilograms')
elif weight_type.upper() == "K":
    print(f"You are {weight * kg_to_lb:.1f} pounds")

# number guessing game
secret = 9
tries_limit = 3
tries = 0
while tries < tries_limit:
    guess = int(
        input(f"You have {tries_limit - tries} tries left! Guess the number: "))
    tries += 1
    if guess == secret:
        print("You won!")
        break
else:
    print("You lost, sorry!")

# car program
user_input = ""
car_started = False
while True:  # no need to put `user_input != "quit"` since the only way to break out is by quiting
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

# how a for loop parses through different data structures
for item in 'Python':
    print(item)  # each letter, each a new line
for item in ["Anakin", "Obiwan", "Yoda"]:
    print(item)  # all names, each a new line
for item in range(10):
    print(item)  # 1 through 9, each a new line
for item in range(5, 10, 2):
    print(item)  # same as above, but, 5, 7, 9

# summation of prices using for loop
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# printing coordinates
for x in range(4):  # 0, 1, 2, 3
    for y in range(3):  # 0, 1, 2
        print(f"({x}, {y})")

# printing the letter "f"
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("x" * number)
for number in numbers:
    total_string = ""
    for x in range(number):
        total_string += "x"
    print(total_string)

# find largest number in a list
numbers = [-1, 5, 2, 3, 100, 90, 99, -2]
maximum = 0
for number in numbers:
    maximum = max(maximum, number)
print(f"Maximum number: {maximum}")

# list methods
numbers = [5, 2, 1, 7, 4]
numbers.insert(2, 10)
print(numbers)  # "[5, 2, 10, 1, 7, 4]"
print(numbers.index(2))  # "1"
numbers.pop()
print(numbers)  # "[5, 2, 10, 1, 7]"
numbers.append(5)
print(numbers)  # "[5, 2, 10, 1, 7, 5]"
print(numbers.count(5))  # "2"
numbers.sort()
print(numbers)  # "[1, 2, 5, 5, 7, 10]"
numbers.reverse()
print(numbers)  # "[10, 7, 5, 5, 2, 1]"
numbers.clear()
print(numbers)  # "[]"
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)  # "[5, 2, 1, 7, 4]"

# remove duplicates in a list
numbers = [4, 5, 2, 10, 1, 7, 5, 0, 10, 1, 7]
no_duplicates_numbers = []
for number in numbers:
    if number not in no_duplicates_numbers:
        no_duplicates_numbers.append(number)
print(numbers)
print(no_duplicates_numbers)

# tuples are immutable, but may unpack to separate variables to manipulate
coordinates = (1, 2, 3)
x, y, z = coordinates
x = x + 1
print(x)

# dictionaries
customer = {
    "name": "irene",
    "age": 31,
    "is_verified": True
}
print(customer.get("birthdate"))  # "None"
print(customer.get("birthdate",  "March 29 1991"))  # "March 29 1991", default
print(customer["Name"])  # "KeyError: 'Name'", must have same case and spelling

# print phone number in text instead of numbers
phone_number = input("Phone: ")
phone_text = ""
phone_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
for number in phone_number:
    if number in phone_mapping:
        phone_text += phone_mapping.get(number, "!") + " "
print(phone_text)

# emoji inserter
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😃",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)  # i love stranger things 😃

# functions
# parameters are placeholders while arguments are the actual values
def greet_user(first_name: str, last_name: str) -> None:
    print(f"Hello there {first_name} {last_name}")
greet_user("Renekton", "Sands")  # positional argument
greet_user(first_name="Renekton", last_name="Sands")  # keyword argument
# positional arguments must be ahead of keyword arguments
greet_user("Renekton", last_name="Sands")

# return statement
def square(number: int) -> int:
    return number * number
print(square(3))

# emoji inserter reusable function
def emoji_converter(message: str) -> str:
    words = message.split(" ")
    emojis = {
        ":)": "😃",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input(">")
result = emoji_converter(message)
print(result)

# exceptions
try:
    age = int(input("Age: "))
    income = 200000
    risk = income / age
    print(f"{risk:.2f}")
except ZeroDivisionError:
    print("Age can not be 0!")
except ValueError:
    print("Invalid value!")

# comments should always explain why and how, not just why
# too much of a good thing is a bad thing

# classes are CamelCase
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
# this allows "point1.x" to be "10" and "point1.y" to be "20"
point1 = Point(10, 20)
point1.draw()  # the reason for "self" is because "point1.draw()" is internally converted as "Point.draw(point1)" so it knows which object you want

# constructors
class Person:
    def __init__(self, name) -> None:
        self.name = name
    def talk(self) -> None:
        print(f"Hi, I am {self.name}")
jarvan = Person("Jarvan")
jarvan.talk()

# inheritance
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bork(self):
        print("i'm borking")
class Cat(Mammal):
    def be_annoying(self):
        print("i'm annoying")
hehe = Dog()
hehe.walk()
hehe.bork()
hoho = Cat()
hoho.walk()
hoho.be_annoying()

# modules, aka separate files
# can either import a whole module via "import utils" or a specific function "from utils import test_function"
from utils import test_function
# if whole module "utils.test_function()"
test_function()
# utils.py
def test_function() -> None:
    print("Testing the module if it works.")

# module exercise
import utils
numbers = [10, 3, 6, 2, 420, 100, -50, -500]
print(utils.find_maximum_number(numbers=numbers))
# utils.py
def find_maximum_number(numbers: list) -> int:
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

BOOKMARK 3:31:20 MUST USE PYCHARM
"""
