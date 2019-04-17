def find_range(input_list, input_number):
    search = []
    number_range = []
    for index in range(1, len(input_list)):
        if input_list[index] == input_number:
            search.append(index)
        if input_list[index] > input_number:
            break
    number_range.append(search[0])
    number_range.append(search[-1])
    return number_range
    # return Range(search[0], search[-1])


input_list = [1, 2, 5, 5, 8, 8, 10]
input_number = 8
print("find_range():", find_range(input_list, input_number))
input_number = 2
print("find_range():", find_range(input_list, input_number))

"""
class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]

def find_range(input_list,input_number):
    first = 0
    lower_bound = -1
    upper_bound = -1
    last = len(input_list) - 1
    while first < last:
        mid = (first+last)/2
        if input_list[mid] < input_number:
            first = mid + 1
        else:
            last = mid

    if input_list[first] != input_number:
        return Range()
    else:
        lower_bound = first
    first = 0
    last = len(input_list) - 1
    while first < last:
        mid = (first + last)/2
        if (input_list[mid] < input_number + 1):
            first = mid + 1
        else:
            last = mid

    if(input_list[first] == input_number):
        upper_bound = first
    else:
        upper_bound = first-1
    return Range(lower_bound,upper_bound)
"""

"""
def bisect(input_list, input_number, f):
    left, right = 0, len(input_list)
    
    while left < right:
        mid = left + (right - left)/2
        if f(input_list[mid], input_number): left  = mid + 1
        else:               right = mid
    
    return left

bisect_left  = lambda input_list,input_number: bisect(input_list, input_number, lambda x,y: x<y)
bisect_right = lambda input_list,input_number: bisect(input_list, input_number, lambda x,y: x<=y)

def find_range(input_list, input_number):
    start = bisect_left(input_list, input_number)
    end   = bisect_right(input_list, input_number) - 1
    return Range(start, end)
"""
