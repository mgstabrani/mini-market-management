# Inisialisasi Array dan Variabel
produk = [["",0,0,0] for i in range(200)]

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
    if(n == 1):
        Penambahan_Produk()
    elif(n == 2):
        Penambahan_Stok()
    elif(n==3):
        Penjualan()
    elif(n == 4):
        List_Harga()
    # elif(n==5):
    #     Keuntungan(m)
    elif(n == 6):
        Keluar()
    else:
        error_message()

def Keluar():
    print()
    print("Apakah anda yakin ingin keluar program?")
    print("Semua data anda akan terhapus")
    print("1. Keluar")
    print("2. Kembali ke menu")
    pilihan = int(input())
    if(pilihan == 1):
        exit
    else:
        Menu()

def error_message():
    print()
    print("Error, kembali ke menu awal")
    Menu()

def Penambahan_Produk():
    print()
    namaProduk = input("Nama produk yang ditambahkan: ")
    found = False
    i = 0
    while(found == False and i < 200):
        if(namaProduk == produk[i][0]):
            found = True
        else:
            i += 1
    if(found):
        print("Produk sudah ada.")
    else:
        i = 0
        tulis = False
        while(tulis == False and i < 200):
            if (produk[i][0] == ""):
                tulis = True
            else:
                i += 1
        produk[i][0] = namaProduk
        produk[i][1]=int(input("Harga beli produk: "))
        produk[i][2]=int(input("Harga jual produk: "))
        produk[i][3]=int(input("Stok awal produk: "))
        print("\nPenambahan produk berhasil")
    print("Mengalihkan Anda ke menu awal")
    Menu()
    
def tampilDaftar():
    print("\nList Produk")
    print("Nama - Sisa Stok")
    n = 0
    while(produk[n][0] != ""):
        n += 1
    for i in range(n):
        print(str(i+1) + ". " + produk[i][0] + " - " + str(produk[i][3]))

def List_Harga():
    tampilDaftar()
    Menu()

def Penambahan_Stok():
    print()
    tampilDaftar()
    nomorProduk = int(input("\nNomor produk yang akan ditambah: "))
    if (produk[nomorProduk-1][0] != ""):
        produk[nomorProduk-1][3] += int(input("Banyak stok yang akan ditambah: "))
        print("\nStok berhasil ditambahkan")
    else:
        print("Produk tidak ditemukan.")
    print("Mengalihkan ke menu awal\n")
    Menu()

def Penjualan():
    tampilDaftar()
    nomorProduk = int(input("Nomor produk yang terjual: "))
    if (produk[nomorProduk-1][0] != ""):
        produk[nomorProduk-1][3] -= int(input("Banyak stok yang terjual: "))
        print("\nStok berhasil dijual")
    else:
        print("Produk tidak ditemukan.")
    print("Mengalihkan ke menu awal")
    Menu()

# def Keuntungan(n):
#     print("Pilih metode perhitungan keuntungan! ")
#     print("1. Keuntungan per produk")
#     print("2. Keuntungan total")
#     o = int(input("Masukkan pilihan(angka)! "))
#     if(o==1):
#             Keuntungan_per_produk(o)
# ##    elif (o==2):
# ##        Keuntungan_total(o)
#     else:
#         error_message(o)

# def Keuntungan_per_produk(n):
#     List_Harga1(n)


print("Selamat Datang di Program Manajemen Stok Minimarket!")
Menu()
