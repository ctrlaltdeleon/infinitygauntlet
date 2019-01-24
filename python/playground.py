class Solution:

    def counting(self, number):
        for i in range(1, number+1):
            print(i)


# create object from class solution
test_object = Solution()

number = 10

test_object.counting(number)

n = int(input("Please input number of rows: "))
o = int(input("Please input number of columns: "))

main_list = []

for i in range(n):
    temp_list = []
    for j in range(o):
        temp_list.append(input("Element [{0}][{1}]: ".format(i, j)))
    main_list.append(temp_list)

print(main_list)
