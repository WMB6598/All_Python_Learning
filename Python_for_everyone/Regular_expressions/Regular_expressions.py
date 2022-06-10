import re


import re # Regular expressions arent in the default python library
hand = open('Course_assets\intro.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)