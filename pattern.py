n=5
f=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(f*j,end=' ')
    f=f+1
    print( )


#in pattern adding a increment the 2 values in particular sector
    
n=5
f=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(f*j,end=' ')
    
    f=f+1
    if f%3==0:
        f=f+1
    print( )