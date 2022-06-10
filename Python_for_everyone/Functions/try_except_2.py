#Asks for an input, and checks if it is a number by trying to convert it to int

rawstr = input('Enter an number ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
elif ival <= 0:
    print('Nice Work')
else:
    print('Not a number')