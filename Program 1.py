print(' ')
print('-------Menghitung laba seorang pengusaha-------')
a=100000000
sum=0
b=0
laba=[int(0),int(0),int(a)*.1,int(a)*.1,int(a)*.5,int(a)*.5,int(a)*.5,int(a)*.2]

print('')
print('Modal seorang pengusaha       :',a)
print(' ')

for i in laba:
    sum=sum+i
    b+=1
    print('Laba Bulan ke -',b,'Sebesar     :',i)

print(' ')
print('Total laba yang didapat pengusaha :', sum)