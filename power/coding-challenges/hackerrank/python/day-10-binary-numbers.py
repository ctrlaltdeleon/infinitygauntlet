print(len(max(bin(int(input("Input an integer: ").strip()))[2:].split('0'))))

"""
Input an integer: 500
5
"""

"""
int(input().strip())
take the input and strip any unneeded characters from beginning or end
13

bin()
take the input and transform to binary output
0b1101

max([2:].split('0'))
starting from the 2nd index and onward (we don't want the '0b') --> max('1101'.split('0'))
remove all '0' in the string --> max('11','1')
max looks for the biggest value which is '11' --> '11'

len('11')
the length of the string is '2' so we print out --> 2
"""
