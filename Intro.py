print('hello, I Love You')
x = 12
y = 10
z = input('input z = ')         #menghasilkan string
zz= int (input('input zz = '))  #menghasilkan int
a = 1+2
b = 3-3
c = 10/3
d = 10//3
e = 2*3
f = 2**3
print ('x =',x)
print ('y =',y)
print ('z =',z)
print ('zz =',zz)
print ('a =',a)
print ('b =',b)
print ('c =',c)
print ('d =',d)
print ('e =',e)
print ('f =',f)

m = [2, 'saya', True, 5]
print ('m =',m)
print ('z[0] =',z[0])

xx = 7
if xx<5:
    print('bilangan kurang dari 5, yaitu ', xx)
else:
    print('bilangan lebih dari 5, yaitu ', xx)

for i in range(5):
    print('nilai i = ',i)

yy = int(input('nilai yy = '))
if yy<5:
	print('bilangan kecil')
	print('nilai yy = ',yy)
	yy = yy*2
else:
	print('bilangan besar')
	print('nilai yy = ',yy)
	yy = yy*10
	
print('nilai yy di luar if = ',yy)

for i in range(5):
    print('nilai i = ',i)

for i in range(2,5):
    print('nilai i = ',i)

aa = [30, 35,70,100,200]
print(aa)

for i in aa:
    print('nilai i = ',i)

cc = 0
while cc<5:
    print('nilai cc = ',cc)
    cc = cc+1

print('nilai cc di luar while = ',cc)
