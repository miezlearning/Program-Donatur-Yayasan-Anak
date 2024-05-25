# Selamat Datang di Program Yayasan Budi Pekerti


# ━━━━━━━━━━━━━━━━━━━━━━━━ IMPORT MODULE ━━━━━━━━━━━━━━━━━━━━━━━━ 
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error
# s
from pwinput import pwinput as enkripsi_password

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



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

    def query(self, p):
        if self.connection:
            try:
                CMD = self.connection.cursor()
                CMD.execute(p)
                self.connection.commit()  # Tambahkan commit untuk menyimpan perubahan
                return CMD.fetchall()
            except Error as e:
                print(f"Terjadi kesalahan saat menjalankan query: {e}")
                return None
        else:
            print("Tidak dapat membuat koneksi ke database untuk menjalankan query.")
            return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            # print("Koneksi ke database ditutup")


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



def login():
    
    username = input("Masukkan Username > ")
    password = input("Masukkan Password > ")
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
    finally:
        db.close_connection()

def register():

    # DAftar
    username = input("Masukkan Username > ")
    password = input("Masukkan Password > ")
    notelp = input("Masukkan No Telepon > ")

    try:
        db.query(f"INSERT INTO akun(username,notelp,password,role) VALUES ('{username}', '{notelp}' , '{password}', 'Donatur') ")
        print("Berhasil Daftar...")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan register: {e}")
    finally:
        db.close_connection()


def forgot_password():
    username = input("Masukkan Username > ")

    try:
        cari_username = db.query(f"SELECT username FROM akun WHERE username = {username}")
        if cari_username == True:
            cari_password = db.query(F"SELECT password FROM akun WHERE username = {username}")
            print("Password kamu adalah : " + cari_password)
        else:
            print("Username tidak ditemukan.")
        
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan register: {e}")
    finally:
        db.close_connection()

def menuDonatur():
    print("Selamat datang Donatur")

def menuAdmin():
    print("Selamat datang Admin")





forgot_password()

