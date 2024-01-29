a=[2,3,5,2,4,2,3,8,4,7,5,7,6,9,5,4,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)