#script to find the most common name using a dictionary

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts : #This adds the name to the dictionary if it is not already there
        counts[name] = 1
    else : 
        counts[name] = counts[name] + 1 #Adds 1 to the name count
print(counts)

#You can use a get function to simplify this
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) +1 #use 0 as the default value, if the name isnt there
print(counts)