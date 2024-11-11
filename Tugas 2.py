#Muhammad Ridwan, 1B, RPL, 2407357
 
username = "Daspro2023"
password_fix = "Latihan"

def login():
    kesempatan = 0  
    
    print("Selamat datang di sistem login!")
    
    # User diberi 3 kesempatan untuk memasukkan password
    while kesempatan < 3:
        password_input = input("Masukkan password: ")
        
        if password_input == password_fix:
            print("Login berhasil! Selamat datang.")
            return True  # Login berhasil, keluar dari fungsi
        else:
            kesempatan += 1
            print(f"Password salah. Anda masih memiliki {3 - kesempatan} kesempatan.")
    
    # Jika sudah 3 kali gagal, keluar dari sistem
    print("Anda telah gagal 3 kali memasukkan password. Program keluar.")
    return False  # Login gagal, keluar dari fungsi

# Memanggil fungsi login
login()