# Inisialisasi Array dan Variabel
produk = [["",0,0,0,0,0] for i in range(200)]
'''
produk[i][0] = Nama Produk
produk[i][1] = Harga Beli Produk
produk[i][2] = Harga Jual Produk
produk[i][3] = Stok Produk
produk[i][4] = Modal
produk[i][5] = Jumlah Produk yang Dijual
'''
def Menu():
    print("\n=== MENU UTAMA ===")
    print("Pilihan Menu :")
    print("1. Penambahan Produk Baru")
    print("2. Penambahan Stok Produk Lama")
    print("3. Penjualan Produk")
    print("4. List Produk")
    print("5. Keuntungan")
    print("6. Keluar")
    n = int(input("Pilihan Menu (angka) : "))
    if n == 1:
        Penambahan_Produk()
    elif n == 2:
        Penambahan_Stok()
    elif n==3:
        Penjualan()
    elif n == 4:
        List_Harga()
    elif n == 5:
        Keuntungan()
    elif n == 6:
        Keluar()
    else:
        error_message()

def Keluar():
    print("\nApakah anda yakin ingin keluar program?")
    print("Semua data anda akan terhapus")
    print("1. Keluar")
    print("2. Kembali ke menu")
    pilihan = int(input())
    if pilihan == 1:
        exit
    else:
        Menu()

def error_message():
    print("\nError, kembali ke menu awal")
    Menu()

def Penambahan_Produk():
    print("\n=== Penambahan Produk ===")
    namaProduk = input("Nama produk yang ditambahkan: ")
    found = False
    i = 0
    while(found is False and i < 200):
        if namaProduk == produk[i][0]:
            found = True
        else:
            i += 1
    if found:
        print("Produk sudah ada.")
    else:
        i = 0
        tulis = False
        while(tulis is False and i < 200):
            if produk[i][0] == "":
                tulis = True
            else:
                i += 1
        produk[i][0] = namaProduk
        produk[i][1]=int(input("Harga beli produk: "))
        produk[i][2]=int(input("Harga jual produk: "))
        produk[i][3]=int(input("Stok awal produk: "))
        produk[i][4]=produk[i][1] * produk[i][3]
        print("Penambahan produk berhasil")
    print("\nKembali ke menu utama...")
    Menu()

def tampilDaftar():
    print("\n=== Daftar Produk ===")
    print("Nama - Sisa Stok")
    n = 0
    while produk[n][0] != "":
        n += 1
    for i in range(n):
        print(str(i+1) + ". " + produk[i][0] + " - " + str(produk[i][3]))

def List_Harga():
    tampilDaftar()
    print("\nKembali ke menu utama...")
    Menu()

def Penambahan_Stok():
    print("\n=== Penambahan Stok ===")
    tampilDaftar()
    nomorProduk = int(input("\nNomor produk yang akan ditambah: "))
    if produk[nomorProduk-1][0] != "":
        jumlahTambahStok = int(input("Banyak stok yang akan ditambah: "))
        produk[nomorProduk-1][3] += jumlahTambahStok
        produk[nomorProduk-1][4] += jumlahTambahStok * produk[nomorProduk-1][1]
        print("Stok berhasil ditambahkan")
    else:
        print("Produk tidak ditemukan.")
    print("\nKembali ke menu utama...")
    Menu()

def Penjualan():
    print("\n=== Penjualan ===")
    tampilDaftar()
    nomorProduk = int(input("\nNomor produk yang terjual: "))
    if produk[nomorProduk-1][0] != "":
        jumlahProdukJual = int(input("Banyak stok yang terjual: "))
        if produk[nomorProduk-1][3] - jumlahProdukJual < 0:
            print("Produk kurang")
        else:
            produk[nomorProduk-1][3] -= jumlahProdukJual
            produk[nomorProduk-1][5] += jumlahProdukJual
            print("Stok berhasil dijual")
    else:
        print("Produk tidak ditemukan.")
    print("\nKembali ke menu utama...")
    Menu()

def Keuntungan():
    print("\n=== Keuntungan ===")
    print("Pilih metode perhitungan keuntungan! ")
    print("1. Keuntungan per produk")
    print("2. Keuntungan total")
    pilihan = int(input("Masukkan pilihan(angka): "))
    if pilihan == 1:
        tampilDaftar()
        nomorProduk = int(input("\nNomor produk yang ingin diketahui keuntungannya: "))
        if produk[nomorProduk-1][0] == "":
            print("Produk tidak ditemukan")
        else:
            print(produk[nomorProduk-1][0])
            print("Keuntungan:", produk[nomorProduk-1][2]*produk[nomorProduk-1][5] - produk[nomorProduk-1][4])
    elif pilihan == 2:
        totalKeuntungan = 0
        for i in range(200):
            totalKeuntungan += (produk[i][2]*produk[i][5] - produk[i][4])
        print("\nTotal Keuntungan:", totalKeuntungan)
    else:
        error_message()
    print("\nKembali ke menu utama...")
    Menu()

print("Selamat Datang di Program Manajemen Stok Minimarket!")
Menu()
