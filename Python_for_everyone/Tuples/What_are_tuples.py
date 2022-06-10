#Tuples are another kind of sequence that functions much like  a list
x = (1, 34, 'chicken', False) #Tuples use normal brackets instead of square brackets
print(x[2])

#Normal list functions also work in Tuples
for v in x :
    print(v)

#The difference with Tuples is that they are immutable. Once a value is assigned, it cannot be changed
#Trying to append or change a value within a tuple will cause a traceback
#This is done for effiency, as tuples take up less storage and are quicker to access

t = tuple()
print(dir(t)) # You can see here that the only functions available on a tuple is count and index

#Tuples are good for temporary values that arent going to need to be changed
#You can assign two Tuples at once
(x, y) = (4, 'Cheese')
print(x)
print(y)

#Can also be used with dictionaries
d = dict()
d['Cwen'] = 4
d['Ctun'] = 16
for (k, v) in d.items() :
    print(k, v)

#Tuples are comparable
#Starts from the left, until it finds a value that confirms the answer. so even though there is a value that is bigger, 
#as it is on the right, the tuple has already made its decision
print((0, 1, 2) < (3, 4, 5))
print((0, 1, 2000) < (3, 4, 5))