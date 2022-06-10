# #madlibs using String Concatenation
# name = input("Name to subscribe to: ") #will amend this variable later

# # 3 ways to concatenate strings 
# # These all do the same thing, but the f statement is the easiest way
# print("Subscribe to " + name)
# print("subscribe to {}".format(name))
# print(f"subscribe to {name}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! it makes me so excited all the time becuse \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
