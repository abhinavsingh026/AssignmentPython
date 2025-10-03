text = input('Enter a String to check Frequency of words: ')
freq = {}
words = text.split()
for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print('Word Frequency:-')
for word,count in freq.items():
    print(word,':',count)