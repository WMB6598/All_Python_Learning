print(ord('H')) # This will show the numerical ASCII value of a character
print(ord('a'))
print(ord('\n'))

#As ASCII only had 128 characters, we now use Unicode, as this has an exponentially larger pool of characters
#Best practice moving characters across the internet it to use UTF-8
#UTF-8 has dynamic length, so each character is 1-4 bytes. If it is 1 byte, it is compatible with ASCII
#In python 3, all strings are unicode
#This is the reason that we used .encode and .decode when talking to the sockets
