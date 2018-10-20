# creating functions by ourself

temp = input('please enter the F temp:  ')
temp = int(temp)

def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

print("the C temp is: " ,  fahr_to_celsius(temp))
