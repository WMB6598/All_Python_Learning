print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

#script to find the larget number in a loop
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [1, 45, 34, 65, 234, 6] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)