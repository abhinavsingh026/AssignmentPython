string = input('Enter 3 Integers seperated by comma: ')
numstr = string.split(",")
numsum = 0
for i in numstr:
    numsum += int(i)
print('Sum of the Integers is: ',numsum)

list1 = list(map(int,input('Enter 3 Integers seperated by comma: ').split(',')))
print('Sum of 3 Integers is: ',sum(list1))