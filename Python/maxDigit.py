n = int(input('input n = '))

def maxDigit(n):
    digit = 0
    z = n
    maks = 0
    while z>0:
        digit=digit+1
        y = z%10
        z = (z-y)/10
    for j in range(0,digit):
        y = n%10
        n = (n-y)/10
        if y>maks:
            maks=y
    return maks

terbesar = maxDigit(n)
print ('digit terbesar = ',terbesar)
