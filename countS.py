  #Accept string from user and print number of digits, number of alphabets and number of special characters of the string.

s=input("Enter String:")
lcount=0
dcount=0
scount=0
for j in s:
    if j>='A' and j<='Z' or j>='a' and j<='z' :
        lcount=lcount+1
    elif j>='0' and j<='9':
        dcount=dcount+1
    else:
        scount=scount+1
print("Aplhabets :",lcount)
print("Numbers :",dcount)
print("Special Sym :",scount)
