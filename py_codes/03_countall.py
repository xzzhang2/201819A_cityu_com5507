# code modified from https://stackoverflow.com/questions/38401099/how-to-count-one-specific-word-in-python/38401167

import re

filename = input('Enter file:') # you can input any .txt file here. you need to type the path to the file.
# you can try the file in this folder: text_diamond.txt

handle = open(filename, 'r')
counts = dict()

for word in handle.read().split():
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

print(counts)

# print only the count for my_word instead of iterating over entire dictionary
#my_word = "Shine"
# print(my_word, counts[my_word])
