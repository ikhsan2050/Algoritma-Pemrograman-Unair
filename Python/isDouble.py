n = int(input('input n = '))

def isDouble(n):
    digit = 0
    z = n
    kembar = 0
    x = []
    while z>0:
        digit=digit+1
        y = z%10
        z = (z-y)/10
    for i in range(0,digit):
        y = n%10
        n = (n-y)/10
        x.insert(i,y)
    for j in range(0,digit-1):
        for k in range(1,digit):
            if x[j]==x[k]:
                kembar = kembar + 1
    if kembar>0:
        return True
    else :
        return False
        
m = isDouble(n)
print ('Apakah terdapat digit kembar? ')
print (m)
