#Counting Pattern
#This takes an input string, splits it into words, and counts how many of each word there is
'''
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words :
    counts[word] = counts.get(word,0) +1
print('Counts', counts)
'''
#You can write a for loop that will loop through every key

counts = {'chuck' :1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])

#Different ways of retieving lists of keys and values
counts = {'chuck' :1, 'fred' : 42, 'jan' : 100}
print(list(counts))
print(counts.keys()) # Prints the labels (keys)
print(counts.values()) # Prints the values in the dictionary
print(counts.items()) #Prints both the keys and values (this is a tuple). Called the items

#You can use two iteration variables to get both values from a dictionary
counts = {'chuck' :1, 'fred' : 42, 'jan' : 100}
for a, b in counts.items() : # Have to use .items() to do this
    print(a , b)