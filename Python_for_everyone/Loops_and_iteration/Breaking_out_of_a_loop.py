#This would be an infinite loop, if the break function hadnt been added
#once you have done a break, the loop is exited completely

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done')
