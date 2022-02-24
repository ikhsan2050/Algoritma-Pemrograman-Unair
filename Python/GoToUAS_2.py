n = int(input('input tahun = '))
jumlah = 1
populasi = [1, 2, 4]

def hasil(populasi, jumlah):
    if n>=3:
        for i in range(3,n+1):
            populasi.insert(i,(populasi[i-1])+(populasi[i-2]))
        return populasi

if n<3:
    m = populasi
else:
    m = hasil(populasi, jumlah)
print('populasi rumpun pada tahun ke -',n,':',m[n])

# pola yang didapatkan mulai dari tahun ke-3 adalah barisan bilangan Fibonaci
# sehingga kita input manual data tahun ke-0, ke-1, dan ke-2,
