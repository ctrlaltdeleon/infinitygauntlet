def unique_chars_in_string(input_string):
    return len(set(input_string)) == len(input_string)

input_string = str(input("Input a string: "))
print("unique_chars_in_string():", unique_chars_in_string(input_string))

"""
Input a string: hello
unique_chars_in_string(): False
"""