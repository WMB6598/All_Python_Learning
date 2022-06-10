#you can convert a dictionary to tuple to sort it
#will sort by key first. If there are duplicates, then it will sort by value
'''d = {'a' : 10, 'f': 32, 'c' : 1}
print(d.items())
print(sorted(d.items()))

for k, v in sorted(d.items()) :
    print(k, v)'''

#you can create a data structure to sort by value instead
'''d = {'a' : 10, 'f': 32, 'c' : 1}
tmp = []
for k, v in d.items() :
    tmp.append( (v, k) )#This appends a tuple in value, then key order, so flips the order of each tuple
print(tmp)
tmp = sorted(tmp, reverse = True)#Sorts in reverse order
print(tmp)'''

#find the top 10 most common words
fhand = open('Tuples\Romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
#This part is the standard way of counting words in dict (Histogram)

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)
#Creates a new Tupple, and puts the value before the key

lst = sorted(lst, reverse = True)
#sorts and reverses the order, so biggest nueber is first

for val, key in lst[:10] :
    print(key, val)
#Prints the top 10 

#This is a mre advanced way of doing it all in one go
d = {'a' : 10, 'f': 32, 'c' : 1}
print( sorted( [(v,k) for k,v in d.items() ] ) )
#This creates a dynamic list. creates a list using v, k for all items in the dicitonary. 