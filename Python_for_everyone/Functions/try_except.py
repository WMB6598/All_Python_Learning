#Try and except can be used to avoid a traceback if part of the code goes wrong, so the rest
#of your code can run

#astr is a string, so cant be converted to int, so prompts except
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

#astr here can be converted to an integer, so runs the try and ignores the except
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)