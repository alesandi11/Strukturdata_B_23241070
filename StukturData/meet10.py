# belajar perbandingan lanjutan, elif

nama = input("masukan nama :")

if nama=="eby": # kondisi 1
    print("dosen ganteng") # aksi true 1
elif nama=="dawya": #kondisi 2
    print("dosen sangat ganteng") # aksi true 2 
elif nama=="sandi": # kondisi 3
    print("anda kn mahasiwa") # aksi true 3
else :
    print("bukan dosen ganteng") # aksi false
print("program selsai")

def penjumbalahan(a, b):
    return a + b 

def pengurangan(a, b):
    return a - b

print("selamat datang di aplikasi penjumlahan/pengurangan")
print("pilih operasi yang ingin anda lakukan")
print("1. penjumblahan")
print("2. pengurangan")

pilihan = input("masukan pilihan anda (1 atau 2): ")

if pilihan == '1':
    bil1 = float (input("masukan bilangan pertama: "))
    bil2 = float (input("masukan bilangan kedua: "))
    hasil = penjumbalahan(bil1,bil2)
    print("hasil penjumlahan:", hasil)
elif pilihan =='2':
    bil1 = float (input("masukan bilangan pertama: "))
    bil2 = float (input("masukan bilangan kedua: "))
    hasil = pengurangan(bil1,bil2)
    print("hasil pengurangan:", hasil)
else:
    print("pilihan tidak valid")