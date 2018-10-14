class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


test = MyClass()
test1 = MyClass()
# tests are objects

test1.variable = "BOI"

print(test.variable)
# blah
print(test.function())
# This is a message inside the class.
# None
test.function()
# This is a message inside the class.
print(test1.variable)
# BOI
