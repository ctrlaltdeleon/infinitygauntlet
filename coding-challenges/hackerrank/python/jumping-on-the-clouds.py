"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def jumping_on_clouds(c):
    journey = ''.join(c)
    return journey.count('00') + journey.count('1')


if __name__ == '__main__':
    c = input("Input thunder (1) VS cumulus (0): ")
    print("jumping_on_clouds():", jumping_on_clouds(c))
