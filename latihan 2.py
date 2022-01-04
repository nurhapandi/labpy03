print(' ')
print('-----Program Menampilkan bilangan terbesar-----')
print(' ')


max = 0


while True:
    a = int(input('Masukkan bilangan:'))
    if a >= max:
        max = a
    if a == 0:
        break


print('Nilai terbesarnya adalah :',max)
print(' ')
print('--------------------SELESAI--------------------')
