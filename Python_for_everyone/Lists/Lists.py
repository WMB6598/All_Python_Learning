#Lists are a way of assinging multiple values to a single variable
example_list = [1,2,3,4,5,6]
print(example_list)

#List can be made up of multiple types 
example_list = ['red', 14, 34.2]
print(example_list)

#Lists can cointain lists
example_list = ['red', [5, 10], 14, 34.2]
print(example_list)

#Lists can also be empty
example_list = []
print(example_list)

#for statements use lists
for count in [5, 4 , 3 , 2 , 1] :
    print(count)
print('blastoff!')

#We can use index to look within lists
example_list = ['red', 14, 34.2]
print(example_list[1])

#you are able to change lists (They are mutable)
example_list = ['red', 14, 34.2]
example_list[1] = 'boobs'
print(example_list)

#you can use the len function to see how many items are in the list
example_list = ['red', 14, 34.2]
print(len(example_list))