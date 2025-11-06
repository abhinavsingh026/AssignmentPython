start = int(input("Enter Start of range: "))
end = int(input("Enter End of range: "))
num = int(input("Enter the No. to check divisibility: "))
print(f"Numbers Divisible by {num} between {start} and {end} are:")
for i in range(start, end+1):
    if i % num == 0:
        print(i)