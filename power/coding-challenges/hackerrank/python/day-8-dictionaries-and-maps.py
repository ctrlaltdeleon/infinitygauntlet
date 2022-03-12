"""
@author: acfromspace
"""

queries = int(input("Input amount of queries: "))
name_phone = [input("Input key (name) and value (phone number) seperated by a space: ").split()
              for _ in range(queries)]
phone_book = {k: v for k, v in name_phone}
while True:
    try:
        checkingName = str(input("Name you would like to check? "))
        if checkingName in phone_book:
            # This is the format for getting specific key, value from a dict.
            print("%s=%s" % (checkingName, phone_book[checkingName]))
        else:
            print("Not found")
    except:
        break
