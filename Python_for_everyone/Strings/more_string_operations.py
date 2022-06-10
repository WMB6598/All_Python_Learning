#slicing strings can be done with a colon in the index operator
#funciton is up to and not including the last number
name = 'Monty Python'
print(name[0:3])
print(name[2:7])
print(name[0:12])

#can leave it blank, so it goes to start/end
print(name[:3])
print(name[2:])
print(name[:])

#in function can be used as a logical operator
fruit = 'banana'
'n' in fruit # This is True
'm' in fruit # This is False
if 'a' in fruit :
    print('Found it')

#You can compare strings
'''
word = input('Input a word ')
if word == 'banana' :
    print('All right, bananas')

if word < 'banana' :
    print('Your word,', word, 'comes before banana')
elif word > 'banana' :
    print('Your word,', word, 'comes after banana')
else :
    print('All right, bananas')
'''
#string library has some built in functions that return a new string that has been altered
name = 'Will'
print(name)
print(name.lower())

#you can use dir to find all the methods available
word = 'word'
print(type(word))
print(dir(word))

#find function can search for a substring within a string
#will return -1 if it is not found
fruit = 'banana'
pos = fruit.find('na')
print(pos)
pos = fruit.find('z')
print(pos)

#the replace functiopn will search and replace all occurances of the string
greet = 'Hello Bob'
print(greet)
greet = greet.replace('Bob', 'Jane')
print(greet)
greet = greet.replace('l', 'x')
print(greet)

#you can use lstrip() or rstrip() to strip whitespace to left or right
#or use strip() to remove both beginning and ending space
greet = ' Hello Bob '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#can check prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

#can extract data from longer lines
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos) #,atpos makes it search after the @
print(sppos)
host = data[atpos + 1 : sppos]
print(host)