#Append the new string in middle of the gven string
l="SivaDurgarao"
s="python"
a=int(len(l)/2)
n=""
for i in range(len(l)):
    if i<a:
        n=n+l[i]
    elif i==a:
        n=n+s
    if i>=a:
        n=n+l[i]
print(n)