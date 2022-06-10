#continue ends the current iteration and jumps to the top of the loop and starts the next iteration
#break ends loop, continue goes to the start of the loop

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')