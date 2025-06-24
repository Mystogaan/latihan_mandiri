from db import connect 
from utils import login_utils, landing_page, menu_admin, menu_customer, register 

def main():
    while True:
        pilihan_utama = landing_page() 
        
        if pilihan_utama == '1': 
            while True: 
                role = login_utils() 
                
                if role == "admin":
                    menu_admin() 
                    break 
                elif role == "customer":
                    menu_customer() 
                    break 
                else:
                    print("Silakan coba login kembali.") 
            
        elif pilihan_utama == '2': 
            register()
            
        elif pilihan_utama == '3': 
            print("Terima kasih telah menggunakan aplikasi.")
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()