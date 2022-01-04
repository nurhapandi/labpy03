max = 0
try:
    while True:
        a=int(input("Masukkan Bilangan: "))
        if max < a:
            max = a
        if a == 0:
            break
        print("\nBilangan Terbesar Adalah :", max)

except:
    print ("Masukkan Tipe Data Integer!")
