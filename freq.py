str="Hello hello hi hello hi who" #input("enter string:")
str=str.lower()
words=str.split(" ")
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
        
    counts[word] += 1
    
print(counts)