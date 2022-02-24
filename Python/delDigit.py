a = int (input('input a = '))
b = int (input('input b = '))

#function untuk menghapus digit yang sama (menampilkan digit yang berbeda)
def deleteDigit(a,b):
    digitA = []
    digitB = []
    digitNew = digitA
    digitLast = []

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

    n = 0
    kali = 1
    for i in range(0, len(digitLast)):
        n = n + digitLast[i]*kali
        kali = kali*10
    return int(n)

#function untuk menghapus digit yang berbeda (menampilkan digit yang sama)
def deleteDigitNew(a,b):
    digitA = []
    digitB = []
    digitNew = digitA
    digitLast = []

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

    n = 0
    kali = 1
    for i in range(0, len(digitLast)):
        n = n + digitLast[i]*kali
        kali = kali*10
    return int(n)

y = deleteDigit(a,b)
z = deleteDigitNew(a,b)
print('digit yang berbeda =',y)
print('digit yang sama =',z)
