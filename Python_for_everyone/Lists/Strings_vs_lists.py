#You can use the .split method to seperate a string into a list
words = 'Writing a sentence with a fair few words so that I can see the affect better'
stuff = words.split()
print(stuff)
print(len(stuff))
print(stuff[3])

#It will only register one space
words = 'A lot of                      spaces'
stuff = words.split()
print(stuff)

#split splits by spaces to start with, but you can select something else to split with
words = 'This;is;a;sentence;using;semi-colons'
stuff = words.split()
print(stuff)
stuff = words.split(';')#still need quotes for string
print(stuff)

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words[2])

#Pull end part of email address
words = line.split()
email = words[1]
pieces = email.split('@')
final = pieces[1]
print(final)