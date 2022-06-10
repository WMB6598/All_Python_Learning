#You can use the range function in conjuction with lists, to get a numerical value 
print(range(4))

#Length of list
example_list = [12, 'red', 44, 'titties']
print(len(example_list))

#Range of list
print(range(len(example_list)))

#This can be used to construct for loops
friends = ['Greg', 'Bob', 'Gertrude', 'Sylvester']
for friend in friends :
    print('Happy new year', friend)

#using a range can allow you more control over how you move through the list
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy new year', friend)