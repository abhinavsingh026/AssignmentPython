string = input("Enter 3 Numbers in same Line: ")
numstr = string.split()
numsum = 0
for i in numstr:
    numsum += int(i)
print('Sum of the Numbers is: ',numsum)
list1 = list(map(int,input('Enter 3 Numbers in same Line: ').split()))
print('Sum of 3 Numbers is: ',sum(list1))