"""
@author: acfromspace
"""

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1
    # Update max depth
    if level >= maxdepth:
        maxdepth = level
    # Check all possible children to see the deepest level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input("Input number of lines from XML"))
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# Note: this shouldn't work without proper xml syntax and context
