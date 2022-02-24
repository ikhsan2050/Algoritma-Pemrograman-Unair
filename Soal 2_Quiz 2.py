# No 1
a = int(input('input a = '))

def primeFactor(a):
    faktor = []         # List faktor dari n
    faktorPrima = []    # List faktor prima dari n
    for i in range(1,a+1):
        if a%i == 0:
            isi = int (i)
            faktor.insert(i,isi)
    
    for i in range(0,len(faktor)):
        prima = 0
        for j in range(1,faktor[i]+1):
            if faktor[i]%j == 0:
                prima = prima+1
        if prima == 2:
            faktorPrima.insert(i,faktor[i])
    return faktorPrima

z = primeFactor(a)
print('faktor prima dari',a,'adalah',z)


# No 2
m = int(input('input m = '))
n = int(input('input n = '))

def commonFactor(m,n):
    faktorSekutu = []
    y = primeFactor(m)
    z = primeFactor(n)
    for i in range (0,len(z)):
        if m%z[i] == 0:
            faktorSekutu.append(z[i])
    return faktorSekutu
    
new = commonFactor(m,n)
print ('Faktor Persekutuan dari',m,'dan',n,'adalah',new)
