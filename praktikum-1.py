#contoh implementasi function
#dengan python
#algoritma berbeda

# menghitung jumlah digit gasal pada bilangan n

def numOfOdd(n):
    r = 0
    while n>0:
        digit = n%10
        if digit%2 != 0 :
            r += 1
        n = n//10
    return r


# menghitung jumlah digit gasal dan genap pada bilangan n
# memanfaatkan fasilitas list
# logikanya jadi berbeda denganfunction di atas

def numOfOddEven(n):
    x = []
    while n>0 :
        digit = n%10
        x.append(digit)
        n = n//10
    odd = [1,3,5,7,9]
    even = [0,2,4,6,8]
    cOdd = 0
    cEven = 0
    for i in odd:
        cOdd += x.count(i)
    
    for i in even:
        cEven += x.count(i)
    return cOdd, cEven
        

print(numOfOdd(1234))
print(numOfOddEven(12346))
        
