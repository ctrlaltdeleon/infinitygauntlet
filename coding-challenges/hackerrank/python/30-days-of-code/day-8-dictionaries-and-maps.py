"""
@author: acfromspace
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    queries = int(input("Input amount of queries: "))

    # take the input of each string and split into keys and values
    name_phone = [input("Input key and value seperated by a space: ").split() for _ in range(queries)]
    # apply the keys and values to a dictionary
    # dictionaries have no order
    phone_book = {k: v for k,v in name_phone}

    # go through the phone_book with checks depending if the user wants to keep checking
    while True:
        try:
            checkingName = str(input("Name you would like to check? "))
            if checkingName in phone_book:
                # this is the format for getting specific key, value from a dict
                print("%s=%s" % (checkingName, phone_book[checkingName]))
            else:
                print("Not found")
        except:
            break