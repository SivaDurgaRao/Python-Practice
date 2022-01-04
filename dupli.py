string ="hello hi hello hi who" 
string = string.lower() 
words = string.split(" ")  
   
print("Duplicate words in a given string : ") 
for i in range(0, len(words)):  
    count = 1;  
    for j in range(i+1, len(words)):  
        if(words[i] == (words[j])):
            print(words[i])
            break;0