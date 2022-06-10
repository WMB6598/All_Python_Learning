fname = input('Enter filepath: ')
if len(fname) < 1 : fname = 'Dictionaries\Clown.txt' # So you can hit enter to default to the clown.txt
handle = open(fname)

''' This is a slow way of doing a dictionary counter
di = dict()
for lin in handle :
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds :
        if w in di :
            di[w] = di[w] + 1
        else : 
            di[w] = 1
        print(w, di[w])
print(di)
'''
''' Slow way of using get function
di = dict()
for lin in handle : 
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        oldcount = di.get(w, 0) #If word hasnt been seen before, assign its value to 0
        print(w, 'old', oldcount)
        newcount = oldcount + 1 #If we see a word again, add 1 to its value
        di[w] = newcount
        print(w, 'new', newcount)
'''

di = dict()
for lin in handle : 
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds : 
        di[w] = di.get( w, 0) +1 #Get statement in a single line
        #print(w, di[w])
#print(di)

#Now we want to find the most common word
largest = -1 #We can use this as we know all the counters are positive
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k #Captures and remembers the largest key
print(largest, theword)

#We have to generate the values in the dictionaries to go along with the key, which is why we have to run the lin in handle script first