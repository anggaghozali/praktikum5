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
