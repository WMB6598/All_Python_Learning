import urllib.request, urllib.parse, urllib.error

#The below code does the same as the previous, but using urllib makesit much faster
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
    print(line.decode().strip()) # We still have to decode, even though we didnt encode

print()

#We can use urllib  to read webpages
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand : 
    print(line.decode().strip())

print()

counts = dict()
for line in fhand :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) +1
print(counts)