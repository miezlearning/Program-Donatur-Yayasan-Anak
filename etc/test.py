# Selamat Datang di Program Yayasan Budi Pekerti


# ━━━━━━━━━━━━━━━━━━━━━━━━ IMPORT MODULE ━━━━━━━━━━━━━━━━━━━━━━━━ 
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error
# s
from pwinput import pwinput as enkripsi_password

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ━━━━━━━━━━━━━━━━━━━━━━━━ DATABASE STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

class Database:
    def __init__(self):
        self.connection = self.koneksi()

    def koneksi(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbotest"
            )
            if mydb.is_connected():
                print("Berhasil Koneksi ke Database")
                return mydb
            else:
                print("Koneksi Gagal")
                return None
        except Error as e:
            print(f"Terjadi kesalahan saat menghubungkan ke database: {e}")
            return None

    def query(self, query):
        if self.connection:
            try:
                CMD = self.connection.cursor()
                CMD.execute(query)
                result = CMD.fetchall()
                self.connection.commit()
                return result
            except Error as e:
                print(f"Terjadi kesalahan saat menjalankan query: {e}")
                return None
        else:
            print("Tidak dapat membuat koneksi ke database untuk menjalankan query.")
            return None


    def tutup_koneksi(self):
        if self.connection.is_connected():
            try:
                CMD = self.connection.cursor()
                CMD.fetchall()  # Membersihkan hasil dari query sebelum menutup koneksi
                self.connection.close()
                print("Koneksi ke database ditutup")
            except Exception as e:
                print(f"Terjadi kesalahan saat menutup koneksi ke database: {e}")



# <> Inisialisasi Modul database.
db = Database()



# ━━━━━━━━━━━━━━━━━━━━━━━━ CLASS STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 
class User():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class Donatur(User):
    def __init__(self, username, password, notelp):
        super().__init__(username, password)
        self.__notelp = notelp

    def get_notelp(self):
        return self.__notelp


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

# ━━━━━━━━━━━━━━━━━━━━━━━━ LOGIN PAGE STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

def login():
    username = input("Masukkan Username > ")
    password = enkripsi_password(prompt="Masukkan Password > ", mask="•")
    try:
        kueri = db.query(f"SELECT username, password, role FROM akun WHERE username = '{username}' AND password = '{password}'")
        if not kueri:
            print("Username atau password yang dimasukkan salah.")
        else:
            role = kueri[0][2]  
            if role == "Donatur":
                menuDonatur()
            elif role == "Admin":
                menuAdmin()
            else:
                print("Role tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan login: {e}")
  

def register():
    username = input("Masukkan Username > ")
    password = enkripsi_password(prompt="Masukkan Password > ", mask="•")
    notelp = input("Masukkan No Telepon > ")

    try:
        cek_username = db.query(f"SELECT * FROM akun WHERE username = '{username}'")
        cek_notelp = db.query(f"SELECT * FROM akun WHERE notelp = '{notelp}'")
        if cek_username:
            print("Username  sudah digunakan. Silakan coba dengan data yang berbeda.")
        elif cek_notelp:
            print("Nomor telepon  sudah digunakan. Silakan coba dengan data yang berbeda.")
        else:
            db.query(f"INSERT INTO akun(username, password, notelp, role) VALUES ('{username}', '{password}', '{notelp}', 'Donatur')")
            print("Berhasil Daftar...")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan register: {e}")

    

def forgot_account():
    print("Pilih Metode Forgot Account : ")
    print("1. Forgot Username")
    print("2. Forgot Password")
    print("3. Forgot No Telepon")
    print("0. Kembali")
    pilih = int(input("Masukkan Pilihan > "))
    
    if pilih == 1:
        forgot_username()
    elif pilih == 2:
        forgot_password()
    elif pilih == 3:
        forgot_no_telepon()
    elif pilih == 0:
        login()
    else: 
        print("Pilihan tidak valid.")

def forgot_username():
    while True:
        username = input("Masukkan Username > ")
        try:
            cari_username = db.query(f"SELECT id_akun, username, password, notelp FROM akun WHERE username = '{username}'")
            if cari_username:
                id_akun, username, password, notelp = cari_username[0]
                print("Informasi akun kamu adalah:")
                print(f"ID Akun: {id_akun}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print(f"No Telepon: {notelp}")
                return False
            else:
                print("Username tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan pencarian username: {e}")
        

def forgot_password():
    print("Metode Forgot Password : ")
    print("1. by Username")
    print("2. by No Telepon")
    pilih_metode = int(input("Masukkan Pilihan > "))
    if pilih_metode == 1:
        while True:
            username = input("Masukkan Username > ")
            try:
                cari_username = db.query(f"SELECT id_akun, username, password, notelp FROM akun WHERE username = '{username}'")
                if cari_username:
                    id_akun, username, password, notelp = cari_username[0]
                    print("Informasi akun kamu adalah:")
                    print(f"ID Akun: {id_akun}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print(f"No Telepon: {notelp}")

                    return False
                else:
                    print("Username tidak ditemukan.")
            except Exception as e:
                print(f"Terjadi kesalahan saat mencari password berdasarkan username: {e}")
            
    elif pilih_metode == 2:
        while True:
            notelp = input("Masukkan No Telepon > ")
            try:
                cari_notelp = db.query(f"SELECT id_akun, username, password, notelp FROM akun WHERE notelp = '{notelp}'")
                if cari_notelp:
                    id_akun, username, password, notelp = cari_notelp[0]
                    print("Informasi akun kamu adalah:")
                    print(f"ID Akun: {id_akun}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print(f"No Telepon: {notelp}")

                    return False
                else:
                    print("No Telepon tidak ditemukan.")
            except Exception as e:
                print(f"Terjadi kesalahan saat mencari password berdasarkan no telepon: {e}")
            
    else:
        print("Pilihan tidak valid.")

def forgot_no_telepon():
    while True:
        notelp = input("Masukkan No Telepon > ")
        try:
            cari_notelp = db.query(f"SELECT id_akun, username, password, notelp FROM akun WHERE notelp = '{notelp}'")
            if cari_notelp:
                id_akun, username, password, notelp = cari_notelp[0]
                print("Informasi akun kamu adalah:")
                print(f"ID Akun: {id_akun}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print(f"No Telepon: {notelp}")
                return False
            else:
                print("No Telepon tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat mencari password berdasarkan no telepon: {e}")
       

    


# ━━━━━━━━━━━━━━━━━━━━━━━━ USER STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 
def menuDonatur():
    print("Selamat datang Donatur")
    print("1. Tentang Kami")
    print("2. Program Kami")
    print("3. Donasi")    
    print("4. Donasi Mingguan")    
    print("5. Adik Asuh") 
    print("6. Logout") 


def UserTentangKami():
    pass

def UserProgramKami():
    pass


       

# ━━━━━━━━━━━━━━━━━━━━━━━━ ADMIN STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

def menuAdmin():
    print("Selamat datang Admin")
    print("1. Manajemen Program Donasi")
    print("2. Manajemen Adik Asuh")
    print("3. Logout")

def AdminManajemen_ProgramDonasi():
    pass

def AdminManajemen_AdikAsuh():
    pass






register()

