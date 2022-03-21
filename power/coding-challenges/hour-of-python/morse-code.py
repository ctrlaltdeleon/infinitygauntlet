"""
Make a function morsify that, given an uppercase string, returns that
string in morse code. Morse.py contains a dictionary called `code`
mapping capital letters to morse code, which we've already imported for you.

>>>> morsify("TRINKET)
-.-...-.-.-.-
>>>> morsify("Z")
--..
"""

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    " ": "" # Ignore spaces
}

def morsify(string):
    solution = ""
    for index in string:
        for letter, code in morse_code.items():
            if letter == index:
                solution += code
    return solution

# Add more print statements to test what your function does:
print(morsify("TRINKET"))
print(morsify("YEET"))

"""
-.-...-.-.-.-
-.--..-
"""