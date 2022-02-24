#introduction to Python

x = int(input('nilai x = '))
if x<5:
	print('bilangan kecil')
	print('nilai x = ',x)
	x = x*2
else:
	print('bilangan besar')
	print('nilai x = ',x)
	x = x*10
	
print('nilai x di luar if = ',x)

for i in range(5):
    print('nilai i = ',i)

for i in range(2,5):
    print('nilai i = ',i)

x = [30, 35,70,100,200]
print(x)

for i in x:
    print('nilai i = ',i)

c = 0
while c<5:
    print('nilai c = ',c)
    c = c+1

print('nilai c di luar while = ',c)

#function
def add(a,b):
    r = a+b
    return r

x = add(5,10)
print('nilai x = ',x)
print('nilai function = ',add(add(7,3),3))

def f(a,b):
    r1 = a+b
    r2 = a*b
    return r1,r2

x,y = f(5,10)
print(x,y)

def fact(n):
    r = 1
    for i in range(1,n+1):
        r = r*i
    return r

x = fact(3)
print('nilai x = ',x)

def factr(n):
    if n==0:
        return 1
    else :
        r = n * factr(n-1)
        return r

x = factr(3)
print('nilai x rekursif = ',x)