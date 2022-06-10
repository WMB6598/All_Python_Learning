fname = input('Enter filepath: ')
if len(fname) < 1 : fname = 'Tuples\Clown.txt' # So you can hit enter to default to the clown.txt
handle = open(fname)

di = dict()
for lin in handle : 
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds : 
        di[w] = di.get( w, 0) +1

'''print(di)

x = di.items() #This gives you the key value pairs
print('List:', x)

x = sorted(di.items())
print('sorted:', x[:5])'''

tmp = []
for k, v in di.items() : 
    newtup = (v, k) # Swaps key and value
    tmp.append(newtup)
#print(tmp)

tmp = sorted(tmp, reverse = True)
#print(tmp[:5])
for v, k in tmp[:5] :
    print(v, k)