n = int(input('input tahun = '))
faktor = []         # List faktor dari n
faktorPrima = []    # List faktor prima dari n

def primeFactor(n):
    for i in range(1,n+1):
        if n%i == 0:
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

z = primeFactor(n)
print('faktor prima dari',n,'adalah',z)

