def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

print("mutate_string():", mutate_string("zimzalabim", 5, "!"))

"""
mutate_string(): zimza!abim
"""