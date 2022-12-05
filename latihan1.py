#input data
from code import InteractiveConsole


stock = {}
#dengan struktur {id : 'jenis_barang','merk_barang','qty'}

#home
def garis():
    print('='*29)

def menu_awal():
    garis()
    print("   CRUD SYSTEM   ")
    garis()
    print("Selamat Datang di aplikasi CRUD")
    print("Gudang kami bisa menyimpan barang")
    print("Sesuai Kebutuhan Anda!")
    garis()

def menu():
    garis()
    print("=Storage Management Menu=")
    garis()
    print("(1) - Input Barang")
    print("(2) - Ambil Barang")
    print("(3) - Cek Barang")
    print("(4) - End Program")
    return int(input("= "))

run = menu_awal()
run = menu()

#data
class sistem:#kelas sistem
    while True:
        if run == 1:
            auth1 = int(input("Barang Baru : 1 atau Barang lama : 2 ?"))
            if auth1 == 1:
                id_barang = int(input("Masukan Id Barang = "))
                jenis_barang = input("Masukan Jenis Barang = ")
                merk_barang = input("Masukan Merk Barang = ")
                qty_barang = int(input("Masukan Qty Barang = "))
                garis()
                stock[id_barang] = jenis_barang, merk_barang, qty_barang
                print(stock[id_barang])
                print("Barang Berhasil Ditambah")
                choice = int(input("Ketika 4 untuk lanjut atau ketik 5 untuk keluar"))
                if choice == 4:
                    run = menu()
                else:
                    break
            elif run == 2:
                print("Fitur masih dalam pengembangan")
        elif run == 3:
            print("BARANG YANG TERSEDIA")
            print("-Id Barang--Jenis--Merk--QTY--")
            for key, value in stock.items():
                print("{}:{}".format(key,value))
            garis()
            choice = int(input("Ketika 4 untuk lanjut atau ketik 5 untuk keluar"))
            if choice == 4:
                run = menu()
            else:
                break

#tambah data 
#update data
#delete data