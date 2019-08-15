"""
@author: acfromspace
"""


def timeConversion(s):
    h, m, sec = map(int, s[:-2].split(':'))
    ending = s[-2:]
    h = h % 12 + (ending.upper() == 'PM') * 12
    return ('%02d:%02d:%02d') % (h, m, sec)


s = "07:56:05PM"
print("timeConversion():", timeConversion(s))
