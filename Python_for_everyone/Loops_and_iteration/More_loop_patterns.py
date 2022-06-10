#for in can be used to count the how many values are in the list
from cgitb import small
from types import NoneType


count = 0
print(count)
for number in [13, 23, 42, 10, 5, 64, 33] :
    count = count + 1
    print(count, number)
print('Total', count)

#It can also be used to add all the numbers in a list
total = 0
print(total)
for thing in [13, 23, 42, 10, 5, 64, 33] :
    total = total + thing
    print(total)
print('Final total number is', total)

#And also to find the average
count = 0
total = 0
for number in [13, 23, 42, 10, 5, 64, 33] :
    total = total + number
    count = count + 1
    print(count, total)
average = total / count
print('The average of', total, 'is', int(average))

#And to filter out certain values, for example numbers bigger than 20
for number in [13, 23, 42, 10, 5, 64, 33] :
    if number > 20:
        print(number, 'is bigger than 20')
print('All numbers larger than 20 found')

#Can be used to find specific values
for number in [13, 23, 42, 10, 5, 64, 33] :
    count = count + 1
    if number == 42 :
        print('Value number', count, 'is equal to', number)
    else :
        print('Value number', count, 'is not equal to', number)
print('found all values equal to 42')

#or to see if it was included in the list at all
found = False
for number in [13, 23, 42, 10, 5, 64, 33] :
    if number == 7 :
        found = True
        break
if found == True :
    print('Number has been found')
else:
    print('Number has not been found')

#find smallest value so far, using a None value
smallest_so_far = None
for number in [13, 23, 42, 10, 5, 64, 33]:
    if smallest_so_far is None:
        smallest_so_far = number
    elif number < smallest_so_far :
        smallest_so_far = number
    print(smallest_so_far)
print('Smallest number is', smallest_so_far)
