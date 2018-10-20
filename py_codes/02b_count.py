# to demonstrate the structure of a program
# Code modified from: http://www.py4e.com/code3/words.py

name = input('Enter file:') # you can input any .txt file here. you need to type the path to the file.
# you can try the file in this folder: text_diamond.txt

handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
