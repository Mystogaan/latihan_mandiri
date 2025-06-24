from db import connect 

def tambah_novel(nama_buku, penulis, stok):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO tb_buku (nama_buku, penulis, stok) VALUES (%s, %s, %s)"
    val = (nama_buku, penulis, stok)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    print(f"Novel '{nama_buku}' berhasil ditambahkan.")
    db.close()

def daftar_novel():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_buku")
    results = cursor.fetchall()
    
    if results:
        print("Daftar Novel:")
        for row in results:
            print(f"ID: {row[0]}, Nama Buku: {row[1]}, Penulis: {row[2]}, Stok: {row[3]}")
    else:
        print("Tidak ada novel yang tersedia.")
    
    cursor.close()
    db.close()

def edit_novel(novel_id, nama_buku, penulis, stok):
    db = connect()
    cursor = db.cursor()
    sql = "UPDATE tb_buku SET nama_buku = %s, penulis = %s, stok = %s WHERE id_buku = %s"
    val = (nama_buku, penulis, stok, novel_id)
    cursor.execute(sql, val)
    db.commit()
    
    if cursor.rowcount > 0:
        print(f"Novel dengan ID {novel_id} berhasil diubah.")
    else:
        print(f"Novel dengan ID {novel_id} tidak ditemukan.")
    
    cursor.close()
    db.close()

def hapus_novel(novel_id):
    db = connect()
    cursor = db.cursor()
    sql = "DELETE FROM tb_buku WHERE id_buku = %s"
    val = (novel_id,)
    cursor.execute(sql, val)
    db.commit()
    
    if cursor.rowcount > 0:
        print(f"Novel dengan ID {novel_id} berhasil dihapus.")
    else:
        print(f"Novel dengan ID {novel_id} tidak ditemukan.")
    
    cursor.close()
    db.close()

def login(username, password):
    db = connect()
    cursor = db.cursor()
    sql = "SELECT * FROM tb_user WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    
    if user:
        # Menyimpan role pengguna setelah login
        role = user[3]  # Misalnya, role ada di kolom ke-4
        print(f"Login berhasil! Role pengguna: {role}")
        cursor.close()
        db.close()
        return role  # Mengembalikan role pengguna
    else:
        print("Username atau password salah.")
        cursor.close()
        db.close()
        return None  # Jika login gagal

def register(username, password):
    db = connect()
    cursor = db.cursor()
    role = 'customer'  # Default role for new users
    sql = "INSERT INTO tb_user (username, password, role) VALUES (%s, %s, %s)"
    val = (username, password, role)
    try:
        cursor.execute(sql, val)
        db.commit()
        print("Registrasi berhasil! Silakan login.")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {e}")
    
    cursor.close()
    db.close()
    
def check_username_exists(username):
    db = connect()
    cursor = db.cursor()
    sql = "SELECT * FROM tb_user WHERE username = %s"
    val = (username,)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user is not None  # Mengembalikan True jika username sudah ada


    
    
    

