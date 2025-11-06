string = input("Enter a string: ")
string = string.lower()
words = string.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(" Word Frequency:- ")
for word, count in frequency.items():
    print(word, ":", count)
