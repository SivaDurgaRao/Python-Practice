l=[12,1,23,34,65,79]
m=0
sm=0
for i in l:
    if m<i:
        sm=m
        m=i
    elif sm<i:
        sm=i
print(m)
print(sm)