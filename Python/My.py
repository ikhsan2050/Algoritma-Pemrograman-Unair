
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

def commonFactor(m,n):
    faktorSekutu = []
    y = primeFactor(m)
    z = primeFactor(n)
    for i in range (0,len(z)):
        if m%z[i] == 0:
            faktorSekutu.append(z[i])
    return faktorSekutu

print ('Menu : 1. Faktor Prima')
print ('       2. Faktor Prima Persektuan')
print ('       3. Keluar')
pilih = int(input('pilihan :'))

while pilih == 1:
    print ()
    print ('Faktor Prima')
    n = int(input('input n = '))
    z = primeFactor(n)
    print ('Faktor prima dari',n,'adalah',z)
    print ()
    print ('Menu : 1. Faktor Prima')
    print ('       2. FPB')
    print ('       3. Keluar')
    pilih = int(input('pilihan :'))
    print ()
    
while pilih == 2:
    print ()
    print ('Faktor Persekutuan')
    m = int(input('input m = '))
    n = int(input('input n = '))
    z = commonFactor(m,n)
    print ('Faktor Persekutuan dari',m,'dan',n,'adalah',z)
    print ()
    print ('Menu : 1. Faktor Prima')
    print ('       2. FPB')
    print ('       3. Keluar')
    pilih = int(input('pilihan :'))
    print ()
