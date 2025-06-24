# main.py
from db import connect
from utils import login_utils, landing_page, menu_admin, menu_customer

def main():
    landing_page() # Tampilkan halaman landing awal

    # Loop sampai login berhasil
    while True:
        role = login_utils() # Panggil fungsi login dari utils.py

        if role == "admin":
            print("Login berhasil sebagai Admin.")
            menu_admin() # Masuk ke menu admin
            break # Keluar dari loop setelah berhasil login
        elif role == "customer":
            print("Login berhasil sebagai Customer.")
            menu_customer() # Masuk ke menu customer
            break # Keluar dari loop setelah berhasil login
        else:
            print("Username atau password salah. Silakan coba lagi.")

# Panggil fungsi main untuk memulai aplikasi
if __name__ == "__main__":
    main()