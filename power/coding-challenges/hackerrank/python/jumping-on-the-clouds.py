def jumping_on_clouds(c):
    journey = ''.join(c)
    return journey.count('00') + journey.count('1')

if __name__ == '__main__':
    c = input("Input thunder (1) VS cumulus (0): ")
    print("jumping_on_clouds():", jumping_on_clouds(c))

"""
Input thunder (1) VS cumulus (0): 1 0 0 1
jumping_on_clouds(): 2
"""