# Labpy03

# PENJELASAN LOOPING

  **LOOPING** pada program python **LOOPING** sendiri artinya perulangan,dalam bahasa pemrograman merupakan suatu pernyataan untuk 
menguntruksi komputer agar melakukan sesuatu secara berulang.
Terdapat 2 jenis perulangan dalam bahasa pemrograman *python* ,yaitu perulangan **for** & **while** .
Dan seperti inilah contoh dari program looping pada python.


# Soal Latihan 1

- Tampilkan n bilangan acak yang lebih kecil dari 0.5
-  Nilai n pada saat runtime
- Anda bisa menggunakan while atau for untuk menyelesaikannya
- Gunakan fungsi random () yang dapat di'import terlebih dahulu

- Kita mulai cara membuat program diatas 👆


**FLOWCHART LATIHAN 1**

![Image are easy](https://user-images.githubusercontent.com/46926758/53193448-8e52a380-3643-11e9-9f3e-82b74718a6aa.png)


- Sebelum memulainya pastikan anda punya aplikasi **PYTHON** 
- jika belum punya silahkan [link ini](https://filehippo.com/download_python/)
- Jika Sudah seperti biasa mendownload Apk lainnya hanya klik next - next - lalu finish :smiley:
- Buka aplikasi python tersebut 
- Lalu pilih menu file - New File atau juga bisa tekan **CTRL + N**
- contoh nya seperti ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/menu%20nex%20file.PNG)


- Jika sudah lakukan kodingan seperti gambar di bawah ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/kodingan%20latihan1.PNG)


- Jika sudah kalian bisa save program kalian dengan tekan **CTRL+S** atau mengklik menu file - save as dan beri nama pada program kalian
- lalu menjalankan program kalian dengan menekan **f5** atau mengklik menu **RUN**
- Perhatikan gambar dibawah ini !

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/save%20as%20dan%20run.png)



- Jika gagal silahkan cek kembali apakah kodingan kalian sudah seperti gambar diatas 👆
- Dan jika berhasil maka tampilan pada program python anda akan seperti ini 👇


![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/Hasil%20Latihan1.PNG)


- Berikut penjelasan dari program diatas

print ('Masukkan nilai N: 5')

import random

jumlah = 5

a = 0

for x in range(jumlah):

i = random.uniform(.0,.5)

a+=1

print('data ke:',a,'==>', i)

print ('selesai')

"print"  : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.

"import" : fungsi lanjut yang dipanggil oleh statement import.

"random" : untuk menentukan suatu pilihan. 

"range"  : merupakan fungsi yang menghasilkan list. Fungsi ini akan menciptakan sebuah list baru dengan rentang nilai tertentu. 

"uniform": digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.


# Alur Algoritma Latihan2.py

**SOAL**

- Buat program untuk menampilkan bilangan *terbesar* dari *n* buah data yang di'inputkan
- Dan masukkan angka nol untuk berhenti

- Kita mulai cara membuat program diatas 👆

**FLOWCHART**)


![Image are easy](https://user-images.githubusercontent.com/46926758/53195549-73366280-3648-11e9-9741-4b5eba27802d.png)


- Sebelum memulainya pastikan anda punya aplikasi **PYTHON** 
- jika belum punya silahkan [link ini](https://filehippo.com/download_python/)
- Jika Sudah seperti biasa mendownload Apk lainnya hanya klik next - next - lalu finish :smiley:
- Buka aplikasi python tersebut 
- Lalu pilih menu file - New File atau juga bisa tekan **CTRL + N**
- contoh nya seperti ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/menu%20nex%20file.PNG)


- Jika sudah lakukan kodingan seperti gambar di bawah ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/kodingan%20latihan%202.PNG)


- Jika sudah kalian bisa save program kalian dengan tekan **CTRL+S** atau mengklik menu file - save as dan beri nama pada program kalian
- lalu menjalankan program kalian dengan menekan **f5** atau mengklik menu **RUN**
- Perhatikan gambar dibawah ini !

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/save%20as%20dan%20run.png)



- Jika gagal silahkan cek kembali apakah kodingan kalian sudah seperti gambar diatas 👆
- Dan jika berhasil maka tampilan pada program python anda akan seperti ini 👇

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/Hasil%20Latihan%202.PNG)

- Berikut penjelas Latihan2.py

max=0

while True:

a=int(input('Masukkan bilangan='))

if max < a:

max = a

if a==0:

break

print('Bilangan terbesarnya adalah',max)


"max"	: fungsi bulid-in untuk mencari nilai tertinggi. Fungsi ini dapat diberikan sebuah parameter berupa angka.

"while"	: disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak 
perulangannya.

"int"	: berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).

"if"	= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu. 

"input"	: masukan yang kita berikan ke program.

"break"	: fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.

"print"	: berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.


# Alur Algoritma program1.py

- Buat program sederhana dengan perulangan,
- Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya
- Dengan modal awal 100 juta
- Pada bulan pertama dan kedua belum mendapatkan laba
- Pada bulan ketiga baru mulai mendapatkan laba sebesar 1%
- Pada bulan kelima pendapatan meningkat 5%
- Selanjutnya pada bulan ke-8 mengalami penurunan keuntungan sebesar 2%
- Sehingga laba menjadi 3%
- Hitung total keuntungan selama 8 bulan berjalan usahanya

- Kita mulai cara membuat program diatas 👆

**FLOWCHART**

![Image are easy](https://user-images.githubusercontent.com/46926758/53196983-d970b480-364b-11e9-846a-f738b6116a58.png)


- Sebelum memulainya pastikan anda punya aplikasi **PYTHON** 
- jika belum punya silahkan [link ini](https://filehippo.com/download_python/)
- Jika Sudah seperti biasa mendownload Apk lainnya hanya klik next - next - lalu finish :smiley:
- Buka aplikasi python tersebut 
- Lalu pilih menu file - New File atau juga bisa tekan **CTRL + N**
- contoh nya seperti ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/menu%20nex%20file.PNG)


- Jika sudah lakukan kodingan seperti gambar di bawah ini

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/kodingan%20program1.PNG)

- Jika sudah kalian bisa save program kalian dengan tekan **CTRL+S** atau mengklik menu file - save as dan beri nama pada program kalian
- lalu menjalankan program kalian dengan menekan **f5** atau mengklik menu **RUN**
- Perhatikan gambar dibawah ini !

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/save%20as%20dan%20run.png)

- Jika gagal silahkan cek kembali apakah kodingan kalian sudah seperti gambar diatas 👆
- Dan jika berhasil maka tampilan pada program python anda akan seperti ini 👇

![Image are easy](https://github.com/MuhammadNurFahmi/Labpy03/blob/master/Hasil%20Program1.PNG)

- Berikut penjelasan dari Program1.py

- masukkan nilai a

- gunakan for untuk perulangan dari 1 sampai 8.Perulangan for disebut counted loop (perulangan yang terhitung)

- lalu gunakan if pertama untuk menentukan laba bulan ke 1 dan ke 2.masukan variabel (b) kalikan nilai (a) dengan data bulan 1 dan 2. cetak (x) dan (b)

- lalu gunakan if kedua untuk menentukan laba bulan ke 3 dan ke 4.masukan variabel (b) kalikan nilai (a) dengan data bulan 3 dan 4. cetak (x) dan (c)

- lalu gunakan if ketiga untuk menentukan laba bulan ke 5 sampai ke 7.masukan variabel (b) kalikan nilai (a) dengan data bulan 5 sampai 7. cetak (x) dan (d)

- lalu gunakan if keempat untuk menentukan laba bulan ke 8.masukan variabel (b) kalikan nilai (a) dengan data bulan 8. cetak (x) dan (e)

- lalu total keseluruhan.

- cetak total
