#prints out the txt file. Need to use relative path
'''
fhand = open('Course_assets\Example Text Email.txt')
for cheese  in fhand:
    print(cheese)
'''

#Ths will find the number of lines in a file
from ast import excepthandler


fhand = open('Course_assets\Example Text Email.txt')
count = 0
for line in fhand :
    count = count + 1
print('line count:', count)

#This will find how many characters
fhand = open('Course_assets\Example Text Email.txt')
inp = fhand.read()
print(len(inp))

#Search for specific lines
fhand = open('Course_assets\Example Text Email.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

#use strip to get rid of extra line breaks
fhand = open('Course_assets\Example Text Email.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#another way of doing this with a continue statement
fhand = open('Course_assets\Example Text Email.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

#using in to select lines
fhand = open('Course_assets\Example Text Email.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)
'''
#Can ask for a file name as input
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand :
    count = count + 1
print('There are:', count, 'lines in this file')
'''
#Can add a try except incase the file name is not valid
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Cant open', fname)
    quit()
count = 0
for line in fhand :
    count = count + 1
print('There are:', count, 'lines in this file')