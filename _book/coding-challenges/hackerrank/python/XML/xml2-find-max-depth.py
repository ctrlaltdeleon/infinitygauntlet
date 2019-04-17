"""
@author: acfromspace
"""

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


n = int(input("Input number of lines from XML"))
xml = ""
for i in range(n):
    xml = xml + input() + "\n"
tree = etree.ElementTree(etree.fromstring(xml))
depth(tree.getroot(), -1)
print(maxdepth)
