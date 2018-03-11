"""
Created 3/7/2018

@author: acfromspace
"""

if __name__ == '__main__':
    n = int(input())
    list_holder = []
    
    for counter in range(n):
        s = input().split(' ')
        # command is put as the first word
        command = s[0]
        if command == 'print':
            print(list_holder)
            continue

        # second word and onward and converted to ints
        args = map(int, s[1:])
        # data structure, command, number of arguments to be passed, heavily reliant on the command itself
        # this is for preventing multiple pointers and just using a function
        getattr(list_holder, command)(*args)
