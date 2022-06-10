#index function can be used to pull part of a string
from stat import FILE_ATTRIBUTE_OFFLINE


fruit = 'banana'
letter = fruit[1]
print(letter)

#index starts at 0, so [1] is the second character
#Will get an error if you index past the end of a string
#fruit = 'banana'
#letter = fruit[11]

#can use a len function to find out the length of a string
fruit = 'banana'
print(len(fruit))

#can create iterations through strings
fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index +1

#for loops can also be used
fruit = 'banana'
for letter in fruit :
    print(letter)

#counting within loop
fruit = 'banana'
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print("the number of a's in banana is", count)

#simplify using in statement
for letter in 'banana' :
    print(letter)
