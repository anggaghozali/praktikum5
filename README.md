# praktikum5
Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut:

~Program meminta memasukan data sebanyak-banyaknya (gunakan perulangan)
Tampilkan pertanyaan untuk menambah data (ya/tidak?), apabila jawaban "tidak", maka program akan menampilkan daftar datanya.
Nilai akhir diambil dari perhitungan 3 komponen nilai (Tugas: 30%, UTS: 35%, UAS: 35%)
Buat flowchart dan penjelasan programnya pada README.md.
Commit dan push repository ke github.

#langkah-langkah
  1. Buat source code seperti ini
  i=0
nm = []
ni = []
tgs = []
uts = []
uas = []
akh = []

while True:
    nama = input("nama\t\t: ")
    nm.append(nama)
    nim = input("NIM\t\t:")
    ni.append(nim)
    nilai_tugas = input("Nilai Tugas\t: ")
    tgs.append(nilai_tugas)
    nilai_uts = input("Nilai Uts\t: ")
    uts.append(nilai_uts)
    nilai_uas = input("Nilai Uas\t: ")
    uas.append(nilai_uas)
    akhir = (nilai_tugas+nilai_uts+nilai_uas)
    akh.append(akhir)

    data = ''
    while data !='y' and data!='t':
        data = input('Tambah Data (y/t)?')
    i+=1
    if data == 't':
        break
print("=======================================================")
print("No |   Nama   |   NIM   |  TUGAS  | UTS | UAS | AKHIR |")
print("=======================================================")
for n in range(i):
    print (" ",n+1,"| ",nm[n]," | ", ni[n], " | ", tgs[n], " | ", uts[n], "| ",uas[n], "| ",akh[n],"|")


source cide dan cidingannya
![Screenshot 1](https://user-images.githubusercontent.com/116193257/204076136-262fcf35-85d5-452f-8257-f605199d1495.png)


![Screenshot 2](https://user-images.githubusercontent.com/116193257/204076143-da6b4588-4c86-41eb-b431-41c016ff150c.png)


#flowchart
![screenshot 3](https://user-images.githubusercontent.com/116193257/204076201-c56d9a38-578e-403e-a1ce-b3748e9ccd62.jpg)

#SEKIAN TERIMAKASIH
