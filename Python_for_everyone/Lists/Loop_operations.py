#You can concatenate lists with +
a = [1, 2, 3]
b = [4, 5, 6,]
c = a + b
print(c)

#Lists can also be sliced
list = [1, 45, 34, 15, 6, 31, 6, 43]
print(list[1:4])
print(list[:7])
print(list[1:])

#Can use dir to find out the available methods
print(dir(list))

#You can start with an empty list, and build on it using append
stuff = []
stuff.append('Bread')
print(stuff)
stuff.append('Horse')
print(stuff)
stuff.append('laser Juice')
print(stuff)

#Can use in operator to check if somehting is in the list
print('Horse' in stuff)
print('Toe jam' in stuff)

#Lists can be sorted using the .sort
stuff = [3, 54, 34, 23, 5, 7, 3, 67, 2]
stuff.sort()
print(stuff)

#There are multiple different functions for lists
print(len(stuff))
print(max(stuff))
print(min(stuff))
print(sum(stuff))
print(sum(stuff)/len(stuff))

#This will take totals and find the average, until done is typed
numlist = []
while True :
    inp = input('Type a number, slut ')
    try:
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)
        if len(numlist) == 10 : # Stops at 10 numbers
            break
    except:
        print('Not a number, idiot')
        continue
average = sum(numlist) / len(numlist)
print('The average of the input numbers is:', average)