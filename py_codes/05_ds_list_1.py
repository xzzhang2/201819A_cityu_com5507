# a demonstration data types

# lists: integers, strings, empty, and nested lists

list1 = [10, 20, 30, 40]
list2 = ['crunchy frog', 'ram bladder', 'lark vomit','harry potter', 'sun wu kong']
list3 = [] # important
list4 = [list1, 10, 20, 30, 'abc', 'def', ['n1, n2'] ]

print(list1, list2, list3, list4)
print(list4) # a nested list

# Lists are mutable
list2[2] = 'another guy not lark vomit'


# checking the list
# how long is the list? len()
print("### checking the list ###")
print(len(list2))
print(range(len(list4)))

# concatenating
list_1_2 = list1 + list2
print(list_1_2)
