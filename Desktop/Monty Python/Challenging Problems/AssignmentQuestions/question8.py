length = int(input('Enter Length of Triangle: ').strip())
breadth = int(input('Enter Breadth of Triangle: ').strip())
hypo = int(input('Enter Hypotenuse of Triangle: ').strip())
if abs((length**2+breadth**2) == hypo**2):
    print("Yes! Triangle is Right Angle Triangle")
else:
    print("No! Triangle is Not Right Angle Triangle")
