#A collection is like a variable with multiple pieces of information in it 
#Lists are a linear collectio of values sthat stay in order
#A Dictionary is a lot messier, there is no real sense of order, but you use a key to pull specific items out
#Keys are like a label that you stick to the value when putting it into a dictionary
#Dictionaries are python's most powerful data collection

#Dictionaries have no order
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#You can use curly brackets rather than dict()

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)