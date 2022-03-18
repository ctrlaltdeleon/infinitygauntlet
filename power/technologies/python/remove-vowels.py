

def removeVowels1(string):
    solution = []
    for character in string:
        if character in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
            continue
        solution.append(character)
    return "".join(solution)


def removeVowels2(string):
    for character in string:
        if character in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
            string = string.replace(character, "")
    return string


string = "acfromspace"
print("removeVowels1():", removeVowels1(string))
print("removeVowels2():", removeVowels2(string))
