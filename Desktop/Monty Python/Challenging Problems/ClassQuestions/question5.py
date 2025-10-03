elements = [12,15,17,20]
X = bytearray(elements)
print('Your Elemets Are: ')
for i in X:
    print(i)
X[0] = 99
X[1] = 88
print('After Change Your Elemets Are: ')
for i in X:
    print(i)