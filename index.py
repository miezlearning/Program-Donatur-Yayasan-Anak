# Selamat Datang di Program Yayasan Budi Pekerti


# ━━━━━━━━━━━━━━━━━━━━━━━━ IMPORT MODULE ━━━━━━━━━━━━━━━━━━━━━━━━ 
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error
# Modul Password Char
from pwinput import pwinput as enkripsi_password
# Modul Fitur Tambahan
from etc.fitur_tambahan import validasi_email, kirim_forgot_account, pembersih , lanjut

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
    def __init__(self, nama, username, password, notelp, email):
        super().__init__(username, password)
        self.__notelp = notelp
        self.__nama = nama
        self.__email = email

    def get_notelp(self):
        return self.__notelp
    def get_nama(self):
        return self.__nama
    def get_email(self):
        return self.__email


class Admin(User):
    def __init__(self, nama, username, password):
        super().__init__(username, password)
        self.__nama = nama
    
    def get_nama(self):
        return self.__nama

# ━━━━━━━━━━━━━━━━━━━━━━━━ LOGIN PAGE STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 


def menuLogin():
    while True:
        print("Selamat datang")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Account")

        pilih = input("Pilih Menu > ")

        if not pilih:
            print("Inputan tidak boleh kosong.")
            continue
        if not pilih.isdigit():
            print("Inputan harus angka.")
            continue

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            forgot_account()
        else:
            print("Pilihan tidak valid.")

def login():
    maks = 3
    percobaan = 0
    while percobaan < maks:
        pilihan = input("Pilih metode login (1. Username, 2. No Telepon): ")
        
        if pilihan == "1":
            tipe_kredensial = "Username"
        elif pilihan == "2":
            tipe_kredensial = "No Telp"
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            continue
        
        credential = input(f"Masukkan {tipe_kredensial} > ")
        if not credential:
            print("Inputan tidak boleh kosong.")
            continue
        password = enkripsi_password(prompt="Masukkan Password > ", mask="•")
        if not password:
            print("Password tidak boleh kosong.")
            continue

        if tipe_kredensial == "No Telp":
            tipe_kredensial = "notelp"
        elif tipe_kredensial == "Username":
            tipe_kredensial = "username"
        
        try:
            kueri = db.query(f"SELECT nama, username, password, role, notelp, email FROM akun WHERE {tipe_kredensial} = '{credential}' AND password = '{password}'")
            if not kueri:
                print("Username atau password yang dimasukkan salah.")
                percobaan += 1
            else:
                role = kueri[0][3]
                if role == "Donatur":
                    donatur = Donatur(kueri[0][0], kueri[0][1], password, kueri[0][4], kueri[0][5] )
                    menuDonatur(donatur)
                elif role == "Admin":
                    admin = Admin(kueri[0][0], kueri[0][1], password)
                    menuAdmin(admin)
                else:
                    print("Role tidak valid.")
                break
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan login: {e}")

    if percobaan == maks:
        print("Anda telah melebihi batas percobaan login. Silakan coba lagi nanti.")

  
def register():
    while True:
        pembersih()
        nama = input("Masukkan Nama Lengkap > ")
        if not nama:
            print("Nama tidak boleh kosong.")
            lanjut()
            continue
        username = input("Masukkan Username > ")
        if not username:
            print("Username tidak boleh kosong.")
            lanjut()
            continue
        cek_username = db.query(f"SELECT * FROM akun WHERE username = '{username}'")
        if cek_username:
            print("Username sudah digunakan. Silakan coba dengan data yang berbeda.")
            lanjut()
            continue
        password = enkripsi_password(prompt="Masukkan Password > ", mask="•")
        if not password:
            print("Password tidak boleh kosong.")
            lanjut()
            continue
        notelp = input("Masukkan No Telepon > ")
        if not notelp:
            print("Nomor telepon tidak boleh kosong.")
            lanjut()
            continue
        cek_notelp = db.query(f"SELECT * FROM akun WHERE notelp = '{notelp}'")
        if cek_notelp:
            print("Nomor telepon sudah digunakan. Silakan coba dengan data yang berbeda.")
            lanjut()
            continue
        percobaan_email = True
        while percobaan_email:
            email = input("Masukkan Email > ")
            if validasi_email(email):
                percobaan_email = False
            else:
                pass               

        cek_email = db.query(f"SELECT * FROM akun WHERE email = '{email}'")
        if cek_email:
            print("Email sudah digunakan. Silakan coba dengan data yang berbeda.")
            lanjut()
            continue


        try:
            donatur = Donatur(nama, username, password, notelp, email)
            db.query(f"INSERT INTO akun(nama, username, password, notelp, role, email) VALUES ('{donatur.get_nama()}','{donatur.get_username()}', '{donatur.get_password()}', '{donatur.get_notelp()}', 'Donatur', '{donatur.get_email()}')")
            print("Berhasil Daftar...")
            break  
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan register: {e}")


    
    
def forgot_account():
    while True:
        print("Pilih Metode Forgot Account : ")
        print("1. Forgot Username")
        print("2. Forgot Password")
        print("3. Forgot No Telepon")
        print("0. Kembali")
        
        pilih = input("Masukkan Pilihan > ")
        if not pilih:
            print("Inputan tidak boleh kosong.")
            continue
        if not pilih.isdigit():
            print("Inputan harus angka.")
            continue
        
    
            
        if pilih == "1":
            forgot_username()
        elif pilih == "2":
            forgot_password()
        elif pilih == "3":
            forgot_no_telepon()
        elif pilih == "0":
            login()
        else: 
            print("Pilihan tidak valid.")
            

def forgot_username():
    while True:
        notelp = input("Masukkan No Telepon > ")
        if not notelp:
            print("No Telepon tidak boleh kosong")
            continue
        try:
            cari_username = db.query(f"SELECT nama, username, password, notelp, email FROM akun WHERE notelp = '{notelp}'")
            if cari_username:
                nama, username, password, notelp, email = cari_username[0]
                if validasi_email(email):
                    kirim_forgot_account(nama, username, password, notelp, email)
                    print("Informasi akun telah dikirim ke email Anda.")
                    return False
                else:
                    print("Email tidak valid.")
            else:
                print("Nomor telepon tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan pencarian username: {e}")

        
def forgot_password():
    while True:
        print("Metode Forgot Password : ")
        print("1. by Username")
        print("2. by No Telepon")
        print("0. Kembali")
        pilih_metode = input("Masukkan Pilihan > ")
        if not pilih_metode:
                print("Inputan tidak boleh kosong.")
                continue
        if not pilih_metode.isdigit():
            print("Inputan harus angka.")
            continue
        if pilih_metode == "1":
            while True:
                username = input("Masukkan Username > ")
                if not username:
                    print("Inputan tidak boleh kosong.")
                    continue
                try:
                    cari_username = db.query(f"SELECT nama, username, password, notelp, email FROM akun WHERE username = '{username}'")
                    if cari_username:
                        nama, username, password, notelp, email = cari_username[0]
                        if validasi_email(email):
                            kirim_forgot_account(nama, username, password, notelp, email)
                            print("Informasi akun telah dikirim ke email Anda.")
                            return False
                        else:
                            print("Email tidak valid.")
                    else:
                        print("Username tidak ditemukan.")
                except Exception as e:
                    print(f"Terjadi kesalahan saat mencari password berdasarkan username: {e}")

        elif pilih_metode == "2":
            while True:
                notelp = input("Masukkan No Telepon > ")
                if not pilih_metode:
                    print("Inputan tidak boleh kosong.")
                    continue
                try:
                    cari_notelp = db.query(f"SELECT nama, username, password, notelp, email FROM akun WHERE notelp = '{notelp}'")
                    if cari_notelp:
                        nama, username, password, notelp, email = cari_notelp[0]
                        if validasi_email(email):
                            kirim_forgot_account(nama, username, password, notelp, email)
                            print("Informasi akun telah dikirim ke email Anda.")
                            return False
                        else:
                            print("Email tidak valid.")
                    else:
                        print("No Telepon tidak ditemukan.")
                except Exception as e:
                    print(f"Terjadi kesalahan saat mencari password berdasarkan no telepon: {e}")
        elif pilih_metode == "3":
            forgot_account()
        else:
            print("Pilihan tidak valid.")

def forgot_no_telepon():
    while True:
        username = input("Masukkan Username > ")
        if not username:
            print("Inputan tidak boleh kosong.")
        try:
            cari_notelp = db.query(f"SELECT nama, username, password, notelp, email FROM akun WHERE username = '{username}'")
            if cari_notelp:
                nama, username, password, notelp, email = cari_notelp[0]
                if validasi_email(email):
                    kirim_forgot_account(nama, username, password, notelp, email)
                    print("Informasi akun telah dikirim ke email Anda.")
                    return False
                else:
                    print("Email tidak valid.")
            else:
                print("Username tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat mencari nomor telepon berdasarkan username: {e}")
       




# ━━━━━━━━━━━━━━━━━━━━━━━━ USER STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 
def menuDonatur(donatur):
    print(f"Selamat datang Donatur {donatur.get_nama()}")
    print("1. Tentang Kami")
    print("2. Program Kami")
    print("3. Donasi")    
    print("4. Donasi Mingguan")    
    print("5. Adik Asuh") 
    print("6. Pengaturan Akun")
    print("0. Logout")

    pilihan = int(input("Pilih Menu >"))

    if pilihan == 1 :
        UserTentangKami()
    elif pilihan == 2 :
        pass
    elif pilihan == 3 :
        pass
    elif pilihan == 4 :
        pass
    elif pilihan == 5 :
        pass
    elif pilihan == 6 :
        pass
    elif pilihan == 0 :
        pass
    else:
        pass




def UserTentangKami():
    print("Tentang Kami")
    print("1. Profil")
    print("2. Visi & Misi")
    print("3. Tujuan")
    print("4. Struktur Pengurus")
    print("5. Laporan Keuangan")
    print("0. Kembali")
    pilihan = int(input("Pilih Menu >"))

    if pilihan == 1:
        pass
    elif pilihan == 2:
        pass
    elif pilihan == 3:
        pass
    elif pilihan == 4:
        pass
    elif pilihan == 5:
        pass
    elif pilihan == 0:
        return


def UserProgramKami():
    pass


       

# ━━━━━━━━━━━━━━━━━━━━━━━━ ADMIN STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

def menuAdmin(admin):
    print(f"Selamat datang Admin {admin.get_nama()}")
    print("1. Manajemen Program Donasi")
    print("2. Manajemen Adik Asuh")
    print("3. Logout")

def AdminManajemen_ProgramDonasi():
    pass

def AdminManajemen_AdikAsuh():
    pass






menuLogin()
