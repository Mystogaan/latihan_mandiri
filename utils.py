from models import check_username_exists

def tambah_buku():
    from models import tambah_novel
    print("\n=== Tambah Novel ===")

    nama_buku = input("Masukkan Nama Buku: ").strip()
    penulis = input("Masukkan Nama Penulis: ").strip()

    try:
        stok = int(input("Masukkan Stok Buku: "))
    except ValueError:
        print("Stok harus berupa angka.")
        return

    if stok < 0:
        print("Stok tidak boleh kurang dari 0.")
        return
    if not nama_buku or not penulis:
        print("Nama buku dan penulis tidak boleh kosong.")
        return

    tambah_novel(nama_buku, penulis, stok)

    
def daftar_buku():
    from models import daftar_novel
    print("\n=== Daftar Novel ===")
    daftar_novel()
    
def edit_buku():
    from models import edit_novel
    print("\n=== Edit Novel ===")
    try:
        novel_id = int(input("Masukkan ID Novel yang ingin diubah: "))
        nama_buku = input("Masukkan Nama Buku Baru: ")
        penulis = input("Masukkan Nama Penulis Baru: ")
        stok = int(input("Masukkan Stok Buku Baru: "))
        if stok < 0:
            print("Stok tidak boleh kurang dari 0.")
            return
        edit_novel(novel_id, nama_buku, penulis, stok)
    except ValueError:
        print("ID Novel harus berupa angka.")

def hapus_buku(novel_id):
    from models import hapus_novel
    print("\n=== Hapus Novel ===")
    try:
        novel_id = int(input("Masukkan ID Novel yang ingin dihapus: "))
        hapus_novel(novel_id)
    except ValueError:
        print("ID Novel harus berupa angka.")

def menu_admin():
    print("\n=== Menu Admin ===")
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Novel")
        print("2. Daftar Novel")
        print("3. Edit Novel")
        print("4. Hapus Novel")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_buku()
            
        elif pilihan == '2':
            daftar_buku()
            
        elif pilihan == '3':
            edit_buku()
            
        elif pilihan == '4':
            hapus_buku()
            
        elif pilihan == '5':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# utils.py
def login_utils():
    # Menggunakan alias untuk menghindari kebingungan dengan nama fungsi di utils
    from models import login as login_model

    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Panggil fungsi login dari models.py
    role = login_model(username, password)

    # Cetak pesan dan kembalikan role ke pemanggil (main.py)
    if role == "admin":
        print("Login berhasil sebagai Admin.")
        return "admin"
    elif role == "customer":
        print("Login berhasil sebagai Customer.")
        return "customer"
    else:
        print("Username atau password salah.") # Hanya pesan kesalahan sederhana
        return None # Kembalikan None jika login gagal


def register():
    from models import register
    # Input username dan password
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Validasi: username dan password tidak boleh kosong
    if not username or not password:
        print("Username dan password tidak boleh kosong.")
        return
    
    # Periksa apakah username sudah terdaftar (fungsi di models.py)
    if check_username_exists(username):
        print("Username sudah terdaftar, coba dengan username lain.")
        return
    
    # Proses pendaftaran pengguna baru
    register(username, password)
    print(f"Registrasi berhasil untuk {username}! Silakan login.")
    

def landing_page():
    print("\n=== Selamat Datang di Aplikasi Novel ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

    

def menu_customer():
    print("\n=== Menu Customer ===")
    while True:
        print("\n=== Menu ===")
        print("1. Daftar Novel")
        print("2. Keluar")
        
        pilihan = input("Pilih menu (1-2): ")
        
        if pilihan == '1':
            daftar_buku()
            
        elif pilihan == '2':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")






