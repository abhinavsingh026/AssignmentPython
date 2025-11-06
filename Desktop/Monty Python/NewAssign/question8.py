length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
hypotenuse = float(input("Enter the hypotenuse: "))
if abs((length**2 + breadth**2) - (hypotenuse**2)) < 1e-9:
    print("It is a Right-Angled T-riangle.")
else:
    print("It is NOT a Right-Angled Triangle.")