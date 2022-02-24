a = int (input('input a = '))
b = int (input('input b = '))

# SOAL 1
# function untuk menghapus digit yang sama (menampilkan digit yang berbeda)
def deleteDigit(a,b):
    digitA = []         # List digit a
    digitB = []         # List digit b
    digitNew = digitA   # List digit a yang elemennya berisi 0 jika sama dengan elemen b b
    digitLast = []      # List digit a yang digitnya berbeda dengan b
    
    i = 0
    while a>0:
        x = a%10
        digitA.insert(i,x)
        i = i+1
        a = (a - x)/10
    i = 0
    while b>0:
        x = b%10
        digitB.insert(i,x)
        i = i+1
        b = (b - x)/10

    n = 0
    for i in range(0, len(digitA)):
        for j in range(0, len(digitB)):
            if digitA[i] == digitB[j]:
                digitNew[i] = 0
    for i in range(0, len(digitA)):
        if digitNew[i] != 0:
            digitLast.insert(i,digitNew[i])

    # mengubah list menjadi bilangan
    n = 0
    kali = 1
    for i in range(0, len(digitLast)):
        n = n + digitLast[i]*kali
        kali = kali*10
    return int(n)

y = deleteDigit(a,b)
print('digit pada a yang berbeda dengan b =',y)


# SOAL 2
# function untuk menghapus digit yang berbeda (menampilkan digit yang sama)
def deleteDigitNew(a,b):
    digitA = []         # List digit a
    digitB = []         # List digit b
    digitLast = []      # List digit a yang digitnya sama dengan b

    i = 0
    while a>0:
        x = a%10
        digitA.insert(i,x)
        i = i+1
        a = (a - x)/10
    i = 0
    while b>0:
        x = b%10
        digitB.insert(i,x)
        i = i+1
        b = (b - x)/10
        
    n = 0
    for i in range(0, len(digitA)):
        for j in range(0, len(digitB)):
            if digitA[i] == digitB[j]:
                digitLast.insert(i,digitA[i])

    # mengubah list menjadi bilangan
    n = 0
    kali = 1
    for i in range(0, len(digitLast)):
        n = n + digitLast[i]*kali
        kali = kali*10
    return int(n)

z = deleteDigitNew(a,b)
print('digit yang sama =',z)
