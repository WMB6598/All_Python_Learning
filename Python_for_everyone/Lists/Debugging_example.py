#Code to find the third word in every sentence that starts with From
'''
file = open('Lists\Example Text Email.txt')

for line in file:
    kube = line.rstrip()
    words = line.split()
    if words[0] != 'From' :
        continue
    print(words[2])
'''
#Above code will return the value once, then traceback. Can toruble shoot by adding some print statements
#With the print statements, we can see that it is failing becauise of a blank line
'''
file = open('Lists\Example Text Email.txt')

for line in file:
    line = line.rstrip()
    words = line.split()
    print('Line: ', line)
    print(words)
    if words[0] != 'From' :
        print('Ignore: ')
        continue
    print(words[2])
'''

#Can add a function to check if the line is blank, the skip it 
'''
file = open('Lists\Example Text Email.txt')

for line in file:
    line = line.rstrip()
    words = line.split()
    #print('Line: ', line)
    #print(words)
    #The below line is called a guardian pattern
    if len(words) < 1 :
        continue
    if words[0] != 'From' :
        #print('Ignore: ')
        continue
    print(words[2])
'''

#this can also be done with an or statement
file = open('Lists\Example Text Email.txt')

for line in file:
    kube = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    print(words[2])