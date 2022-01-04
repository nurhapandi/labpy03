import random
try:
    n = int ( input ("Masukkan Jumlah n:"))
    a = 0
    for c in range (n):
        a+= 1
        b = random.uniform(.0,.5)
        print('Data Ke:',a,"==>", b)
        while a <= 5:
            c = random.random()
            break
except:
    print ("")
    print ("Masukkan Tipe Data Integer!")
