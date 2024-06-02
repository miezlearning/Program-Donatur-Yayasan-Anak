# Selamat Datang di Program Yayasan Budi Pekerti


# ━━━━━━━━━━━━━━━━━━━━━━━━ IMPORT MODULE ━━━━━━━━━━━━━━━━━━━━━━━━ 
# Modul Koneksi Database 
import datetime
import mysql.connector
from mysql.connector import Error
# Modul Password Char
from pwinput import pwinput as enkripsi_password
# Modul Fitur Tambahan
from etc.fitur_tambahan import validasi_email, kirim_forgot_account, pembersih, lanjut, org_chart, menu_navigasi, kalkulatorzakat, submenu_navigasi, top_up


# Modul GUI
import tkinter as tk
from tkinter import messagebox


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

    def query(self, query, params=None):
        if self.connection:
            try:
                CMD = self.connection.cursor()
                CMD.execute(query, params)
                result = CMD.fetchall()
                self.connection.commit()
                return result
            except Error as e:
                print(f"Terjadi kesalahan saat menjalankan query: {e}")
                self.connection.rollback()
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
    def __init__(self, user_id, username, password):
        self.__id = user_id
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
    
    def get_id(self):
        return self.__id

    
  


class Donatur(User):
    def __init__(self, user_id, nama, username, password, notelp, email, dompet=0):
        super().__init__(user_id, username, password)
        self.__notelp = notelp
        self.__nama = nama
        self.__email = email
        self.__dompet = dompet
        self.__password = password
        self.cek_login = True
        
    def get_notelp(self):
        return self.__notelp
    
    def get_nama(self):
        return self.__nama
    
    def get_email(self):
        return self.__email
    
    def get_dompet(self):
        return self.__dompet
    
    def get_password(self):
        return self.__password
    
    def set_dompet(self, dompet):
        self.__dompet = dompet
    
    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def logout(self):
        self.cek_login = False

    def cek_dompet(self):
        print(f"Saldo dompet Anda adalah: {self.__dompet}.")



class Admin(User):
    def __init__(self,user_id, nama, username, password):
        super().__init__(user_id,username, password)
        self.__nama = nama
        self.cek_login = True
    
    def get_nama(self):
        return self.__nama
    
    def logout(self):
        self.cek_login = False


# =====================================
# Program Yayasan
# =====================================
class Program:
    def __init__(self, nama, deskripsi, target_donasi, donasi_terkumpul, tenggat):
        self._nama = nama
        self._deskripsi = deskripsi
        self._target_donasi = target_donasi
        self._donasi_terkumpul = donasi_terkumpul
        self._tenggat = tenggat

    # Getters
    def get_nama(self):
        return self._nama

    def get_deskripsi(self):
        return self._deskripsi

    def get_target_donasi(self):
        return self._target_donasi

    def get_donasi_terkumpul(self):
        return self._donasi_terkumpul

    def get_tenggat(self):
        return self._tenggat
    
    def tambah_donasi(self, jumlah):
        self._donasi_terkumpul += jumlah

    def __str__(self):
        return (f"Nama Program: {self._nama}\n"
                f"Deskripsi: {self._deskripsi}\n"
                f"Target Donasi: {self._target_donasi}\n"
                f"Donasi Terkumpul: {self._donasi_terkumpul}\n"
                f"Tenggat: {self._tenggat}\n")

    
class ProgramManager:
    def __init__(self, db):
        self.db = db

    def tambah_program(self, program):
        query = """
        INSERT INTO programs (nama, deskripsi, target_donasi, donasi_terkumpul, tenggat)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            program.get_nama(),
            program.get_deskripsi(),
            program.get_target_donasi(),
            program.get_donasi_terkumpul(),
            program.get_tenggat()
        )
        result = self.db.query(query, params)
        if result is not None:
            print("Program berhasil ditambahkan.")
        else:
            print("Gagal menambahkan program.")

    def lihat_program(self):
        query = "SELECT id_program, nama FROM programs"
        result = self.db.query(query)
        return result

    def lihat_detail_program(self, idx):
        query = "SELECT nama, deskripsi, target_donasi, donasi_terkumpul, tenggat FROM programs WHERE id_program = %s"
        result = self.db.query(query, (idx,))
        if result:
            program = Program(*result[0])
            print(program)
            return program
        else:
            print("Program tidak ditemukan.")
            return None

    def update_donasi_terkumpul(self, program_id, jumlah):
        query = "UPDATE programs SET donasi_terkumpul = donasi_terkumpul + %s WHERE id_program = %s"
        result = self.db.query(query, (jumlah, program_id))
        if result is not None:
            print("Donasi berhasil diperbarui.")
        else:
            print("Gagal memperbarui donasi.")

    def catat_donasi(self, id_akun, id_program, jumlah, nama_donatur, pesan):
        query = """
        INSERT INTO donasi (id_akun, id_program, jumlah_donasi, nama_donatur, pesan)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (id_akun, id_program, jumlah, nama_donatur, pesan)
        result = self.db.query(query, params)
        if result is not None:
            print("Donasi berhasil dicatat.")
        else:
            print("Gagal mencatat donasi.")
    
    def lihat_histori_donasi(self, id_program):
        query = """
        SELECT nama_donatur, pesan, jumlah_donasi, tanggal_donasi
        FROM donasi
        WHERE id_program = %s
        ORDER BY tanggal_donasi DESC
        """
        result = self.db.query(query, (id_program,))
        return result if result else []

    def edit_program(self, idx, **kwargs):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs])
        params = list(kwargs.values()) + [idx]
        query = f"UPDATE programs SET {set_clause} WHERE id_program = %s"
        self.db.query(query, params)

    def hapus_program(self, idx):
        window = tk.Tk()
        window.title("Konfirmasi Hapus")
        
        label = tk.Label(window, text="Apakah Anda yakin ingin menghapus program ini?")
        label.pack(pady=(25, 10))
        
        def hapus():
            query = "DELETE FROM programs WHERE id_program = %s"
            self.db.query(query, (idx,))
            messagebox.showinfo("Informasi", "Program berhasil dihapus.")
            window.destroy()
        
        def batal():
            messagebox.showinfo("Informasi", "Penghapusan program dibatalkan.")
            window.destroy()

        def tombol_ya_enter(event):
            hapus_button.config(bg="green")

        def tombol_ya_leave(event):
            hapus_button.config(bg="SystemButtonFace")

        def tombol_tidak_enter(event):
            batal_button.config(bg="red")

        def tombol_tidak_leave(event):
            batal_button.config(bg="SystemButtonFace")
        
        hapus_button = tk.Button(window, text="Ya", command=hapus)
        hapus_button.pack(side=tk.LEFT, pady=25, padx=65)
        hapus_button.bind("<Enter>", tombol_ya_enter)
        hapus_button.bind("<Leave>", tombol_ya_leave)

        batal_button = tk.Button(window, text="Tidak", command=batal)
        batal_button.pack(side=tk.RIGHT, pady=25, padx=65)
        batal_button.bind("<Enter>", tombol_tidak_enter)
        batal_button.bind("<Leave>", tombol_tidak_leave)

        
        
        window.mainloop()

# ====================================
# Anak Asuh
# ====================================
class AdikAsuh:
    def __init__(self, nama, tempat_tinggal, umur, kebutuhan):
        self._nama = nama
        self._tempat_tinggal = tempat_tinggal
        self._umur = umur
        self._kebutuhan = kebutuhan

    # Getters
    def get_nama(self):
        return self._nama

    def get_tempat_tinggal(self):
        return self._tempat_tinggal

    def get_umur(self):
        return self._umur

    def get_kebutuhan(self):
        return self._kebutuhan

    # Setters
    def set_nama(self, nama):
        self._nama = nama

    def set_tempat_tinggal(self, tempat_tinggal):
        self._tempat_tinggal = tempat_tinggal

    def set_umur(self, umur):
        self._umur = umur

    def set_kebutuhan(self, kebutuhan):
        self._kebutuhan = kebutuhan

    def __str__(self):
        return (f"Nama: {self._nama}\n"
                f"Tempat Tinggal: {self._tempat_tinggal}\n"
                f"Umur: {self._umur}\n"
                f"Kebutuhan: {self._kebutuhan}\n")


class AdikAsuhManager:
    def __init__(self):
        self.anak_asuh = []

    def tambah_anak(self, anak):
        self.anak_asuh.append(anak)

    def lihat_anak(self):
        return [anak.get_nama() for anak in self.anak_asuh]

    def lihat_detail_anak(self, idx):
        if 0 <= idx < len(self.anak_asuh):
            print(self.anak_asuh[idx])
        else:
            print("Anak Asuh tidak ditemukan.")

    def edit_anak(self, idx, **kwargs):
        if 0 <= idx < len(self.anak_asuh):
            anak = self.anak_asuh[idx]
            if 'nama' in kwargs:
                anak.set_nama(kwargs['nama'])
            if 'tempat_tinggal' in kwargs:
                anak.set_tempat_tinggal(kwargs['tempat_tinggal'])
            if 'umur' in kwargs:
                anak.set_umur(kwargs['umur'])
            if 'kebutuhan' in kwargs:
                anak.set_kebutuhan(kwargs['kebutuhan'])
        else:
            print("Anak Asuh tidak ditemukan.")

    def hapus_anak(self, idx):
        if 0 <= idx < len(self.anak_asuh):
            del self.anak_asuh[idx]
        else:
            print("Anak Asuh tidak ditemukan.")

program_manager = ProgramManager(db)
adik_asuh_manager = AdikAsuhManager()



# ━━━━━━━━━━━━━━━━━━━━━━━━ LOGIN PAGE STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 


def menuLogin():
    menu = ["• Login", "• Register", "• Forgot Account", "• Exit"]
    while True:
        header = "Selamat datang!"
        selected_index = menu_navigasi(header, menu)
        if selected_index == 0:
            login()
        elif selected_index == 1:
            register()
        elif selected_index == 2:
            forgot_account()
        elif selected_index == 3:
            exit(0)

def login():
    maks = 3
    percobaan = 0
    while percobaan < maks:
        options = ["1", "2", "3"]
        menu_items = ["• Username", "• No Telepon", "• Kembali"]
        header = "Pilih Metode Login :"
        selected_index = menu_navigasi(header, menu_items)
        if selected_index == -1 or selected_index >= len(options):
            print("Pilihan tidak valid.")
            continue
        
        pilihan = options[selected_index]
        
        if pilihan == "3":
            print("Kembali ke menu utama.")
            break
        
        if pilihan == "1":
            tipe_kredensial = "Username"
        elif pilihan == "2":
            tipe_kredensial = "No Telp"
        
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
            kueri = db.query(f"SELECT id_akun, nama, username, password, role, notelp, email, dompet FROM akun WHERE {tipe_kredensial} = '{credential}' AND password = '{password}'")
            if not kueri:
                print(f"{tipe_kredensial} atau password yang dimasukkan salah.")
                lanjut()
                percobaan += 1
            else:
                role = kueri[0][4]
                if role == "Donatur":
                    donatur = Donatur(kueri[0][0], kueri[0][1], kueri[0][2], password, kueri[0][5], kueri[0][6], kueri[0][7])
                    menuDonatur(donatur)
                elif role == "Admin":
                    admin = Admin(kueri[0][0], kueri[0][1], kueri[0][2], password)
                    menuAdmin(admin)
                else:
                    print("Role tidak valid.")
                break
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan login: {e}")
            lanjut()

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
                print("Email tidak valid. Coba masukkan kembali.") 

        cek_email = db.query(f"SELECT * FROM akun WHERE email = '{email}'")
        if cek_email:
            print("Email sudah digunakan. Silakan coba dengan data yang berbeda.")
            lanjut()
            continue

        try:
            donatur = Donatur(None, nama, username, password, notelp, email, 0)
            db.query(f"INSERT INTO akun(nama, username, password, notelp, role, email, dompet) VALUES ('{donatur.get_nama()}','{donatur.get_username()}', '{donatur.get_password()}', '{donatur.get_notelp()}', 'Donatur', '{donatur.get_email()}', {donatur.get_dompet()})")
            print("Berhasil Daftar...")
            lanjut()
            break  
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan register: {e}")
            lanjut()

    
    
def forgot_account():
    while True:
        menu = ['• Forgot Username', '• Forgot Password', '• Forgot No Telepon', '• Kembali']
        header = "Pilih Metode Forgot Account :"
        selected_index = menu_navigasi(header, menu)
        if selected_index == 0:
            forgot_username()
        elif selected_index == 1:
            forgot_password()
        elif selected_index == 2:
            forgot_no_telepon()
        elif selected_index == 3:
            menuLogin()
            return False
        
        # pilih = input("Masukkan Pilihan > ")
        # if not pilih:
        #     print("Inputan tidak boleh kosong.")
        #     continue
        # if not pilih.isdigit():
        #     print("Inputan harus angka.")
        #     continue
        
        # if pilih == "1":
        #     forgot_username()
        # elif pilih == "2":
        #     forgot_password()
        # elif pilih == "3":
        #     forgot_no_telepon()
        # elif pilih == "0":
        #     login()
        # else: 
        #     print("Pilihan tidak valid.")
            

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
        # print("Metode Forgot Password : ")
        # print("1. by Username")
        # print("2. by No Telepon")
        # print("0. Kembali")
        menu = ['• Dengan Username', '• Dengan No Telepon','• Kembali']
        header = "Pilih Metode Forgot Password :"
        pilih_metode = menu_navigasi(header, menu)
        if pilih_metode == 0:
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

        elif pilih_metode == 1:
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
        elif pilih_metode == 2:
            forgot_account()
            return False

        
        # pilih_metode = input("Masukkan Pilihan > ")
        # if not pilih_metode:
        #         print("Inputan tidak boleh kosong.")
        #         continue
        # if not pilih_metode.isdigit():
        #     print("Inputan harus angka.")
        #     continue
        # if pilih_metode == "1":
        #     pass
        # elif pilih_metode == "2":
        #     pass
        # elif pilih_metode == "3":
        #     pass
        # else:
        #     print("Pilihan tidak valid.")

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
       
# BAGIAN LOGIN-FORGOT ACCOUNT UDAH SELESAI JANGAN DI UBAH UBAH DULU!



# ━━━━━━━━━━━━━━━━━━━━━━━━ USER STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 


def menuDonatur(donatur):
    
    while donatur.cek_login:
        header = f"Selamat datang Donatur {donatur.get_nama()}"
        menu = ['• Tentang Kami', '• Program Kami', '• Donasi', '• Donasi Mingguan', '• Adik Asuh', '• Dompet', '• Pengaturan Akun','• Logout']
        pilihan = menu_navigasi(header, menu)
        if pilihan == 0 :
            TentangKami()
        elif pilihan == 1 :
            UserProgramKami()
        elif pilihan == 2 :
            donasiProgram(donatur)
        elif pilihan == 3 :
            DonasiMingguan()
        elif pilihan == 4 :
            pass
        elif pilihan == 5 :
            menuDompet(donatur)
            lanjut()
        elif pilihan == 6 :
            pass
        elif pilihan == 7 :
            donatur.logout()
        else:
            pass


def DonasiMingguan():
    while True:
        header = "Halaman Donasi Mingguan"
        menu = ['• Donasi Mingguan', '• Kalkulator Zakat', '• Kembali']
        pilihan = menu_navigasi(header,menu)
        if pilihan == 1:
            kalkulatorzakat()
        elif pilihan == 2:
            pass
        elif pilihan == 3:
            break
        else:
            pass
        



def TentangKami():

    while True:
        # pembersih()
        # print("Tentang Kami")
        # print("1. Profil")
        # print("2. Visi & Misi")
        # print("3. Tujuan")
        # print("4. Struktur Pengurus")
        # print("5. Laporan Keuangan")
        # print("0. Kembali")
        # pilihan = input("Pilih Menu >")
                    #0             1              2              3                                    4                     5
        menu = ['• Profil', '• Visi & Misi', '• Tujuan', '• Struktur Pengurus', '• Laporan Keuangan ( Coming Soon )', '• Kembali']
        header = "Informasi Tentang Kami :"
        pilihan  = menu_navigasi(header, menu)
        
        if pilihan == 0:
            profil()
        elif pilihan == 1:
            visi_misi()
        elif pilihan == 2:
            tujuan()
        elif pilihan == 3:
            struktur_pengurus()
        elif pilihan == 4:
            laporan_keuangan() #Nanti aja setelah donasi dan program kami selesai
        elif pilihan == 5:
            break
        else:
            print("Pilihan tidak valid.")
            lanjut()


def profil():
    print('''
=====================================================================================================================================================================
                                                Selamat datang di aplikasi Yayasan Anak Budi Pekerti!
=====================================================================================================================================================================

Yayasan kami didirikan untuk memberikan dukungan dan pendidikan bagi anak-anak yang kurang beruntung, menciptakan lingkungan yang penuh kasih dan
mendukung perkembangan optimal mereka.

Aplikasi ini memiliki berbagai fitur untuk memudahkan Anda, seperti halaman login yang lengkap dengan opsi register, pemulihan akun, pemulihan kata sandi
nama pengguna, dan nomor telepon yang terlupakan.

Menu utama untuk pengguna mencakup informasi tentang kami, profil yayasan, visi, misi, tujuan, struktur pengurus, dan laporan keuangan. Selain itu, Anda dapat
menjelajahi program kami, melakukan donasi, mengikuti donasi mingguan, dan mendukung program adik asuh.

Bagi admin, tersedia fitur manajemen program donasi yang mencakup tambah, edit, hapus, lihat, dan konfirmasi program donasi. Juga ada manajemen adik asuh yang
memungkinkan admin untuk menambah, mengedit, menghapus, dan melihat data anak.

Fitur tambahan dalam aplikasi ini termasuk koneksi database, karakter kata sandi, pembersihan layar terminal, dan email untuk pemulihan akun yang terlupakan.

Dengan aplikasi ini, kami berharap dapat memudahkan Anda untuk berpartisipasi dalam mendukung anak-anak yang membutuhkan, melalui berbagai program yang kami
tawarkan.
=====================================================================================================================================================================
''')
    lanjut()
    pembersih()
    return


def visi_misi():
    print('''
=====================================================================================================================================================================
> Visi

Menjadi yayasan terdepan yang menyediakan pendidikan dan dukungan komprehensif bagi anak-anak yang kurang beruntung, sehingga mereka dapat tumbuh menjadi individu
yang berintegritas, berpengetahuan, dan mandiri.
=====================================================================================================================================================================
> Misi

1. Menyediakan akses pendidikan berkualitas yang terjangkau bagi anak-anak yang kurang beruntung.
2. Menciptakan lingkungan yang aman, sehat, dan mendukung untuk perkembangan fisik dan mental anak-anak.
3. Mengembangkan program-program yang berfokus pada peningkatan keterampilan hidup, kepercayaan diri, dan kreativitas anak-anak.
4. Menjalin kerjasama dengan berbagai pihak untuk memperluas jangkauan dan efektivitas program-program yayasan.
5. Menyediakan layanan kesehatan dan kesejahteraan yang komprehensif untuk mendukung pertumbuhan optimal anak-anak.
=====================================================================================================================================================================
          ''')
    lanjut()
    pembersih()
    return
    
def tujuan():
    print('''
=====================================================================================================================================================================
> Tujuan          

1. Meningkatkan kualitas pendidikan dan prestasi akademis anak-anak melalui program pendidikan yang inovatif dan berkelanjutan.
2. Membangun karakter dan integritas anak-anak melalui kegiatan budi pekerti dan nilai-nilai moral.
3. Memastikan setiap anak memiliki akses ke fasilitas kesehatan dasar dan layanan pendukung psikologis.
4. Memberdayakan anak-anak dengan keterampilan hidup yang dibutuhkan untuk menghadapi tantangan masa depan.
5. Menggalang dukungan dan partisipasi masyarakat dalam upaya peningkatan kesejahteraan anak-anak yang kurang beruntung.
=====================================================================================================================================================================
''')
    lanjut()
    pembersih()
    return

def struktur_pengurus():
    org_chart()
    lanjut()
    pembersih()
    return

def laporan_keuangan():
    print('''
=====================================================================================================================================================================
>Laporan Keuangan
          
Halaman ini belum selesai, mohon gunakan halaman lain terlebih dahulu.
=====================================================================================================================================================================
''')
    lanjut()
    pembersih()
    return


def UserProgramKami():
    lihatProgram(program_manager)



def donasiProgram(donatur):
    header = "Pilih Program untuk Donasi"
    programs = program_manager.lihat_program()
    options = ["• "+nama for id, nama in programs] + ["• Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(programs):
        program_id = programs[pilihan][0]
        program = program_manager.lihat_detail_program(program_id)
        if program:
            jumlah_donasi = int(input("Masukkan jumlah donasi: "))
            pesan_donasi = input("Masukkan pesan untuk donasi: ")
            nama_donatur = donatur.get_nama()
            program_manager.update_donasi_terkumpul(program_id, jumlah_donasi)
            program_manager.catat_donasi(donatur.get_id(), program_id, jumlah_donasi, nama_donatur, pesan_donasi)
            program.tambah_donasi(jumlah_donasi)
            print(f"Terima kasih atas donasi Anda! Donasi terkumpul: {program.get_donasi_terkumpul()} / {program.get_target_donasi()}")
        lanjut()
    else:
        pass


def menuDompet(donatur):
    while True:
        header = f"Dompet {donatur.get_nama()}"
        menu = ["Cek Dompet", "Top Up Dompet", "Kembali"]
        pilihan = menu_navigasi(header, menu)
        if pilihan == 0:
            cekDompet(donatur)
        elif pilihan == 1 :
            sistemTopUp()
        elif pilihan == 2:
            break

def cekDompet(donatur):
    # pembersih()
    print(f"Dompet anda : {donatur.get_dompet()}")
    lanjut()

def sistemTopUp():
    topupamount = input("Masukkan jumlah pengisian dompet: ")
    if topupamount == "":
        print("Jumlah pengisian tidak boleh kosong.")
        lanjut()
        return
    topupamount = int(topupamount)
    tambahandompet = top_up(topupamount)
    #                ^ belum pake email user
    # contoh top_up(amount, receiver_email)
    # ambil jumlah dompet dari database dan tambahkan dengan tambahandompet
    # lalu simpan lagi di database
    lanjut()

        

# ━━━━━━━━━━━━━━━━━━━━━━━━ ADMIN STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

def menuAdmin(admin):
    
    while admin.cek_login:
        # print(f"Selamat datang Admin {admin.get_nama()}")
        # print("1. Manajemen Program Donasi")
        # print("2. Manajemen Adik Asuh")
        # print("0. Logout")
        # pilihan = input("Masukkan Pilihan")
        header = f"Selamat datang Admin {admin.get_nama()}"
        menu = ['• Manajemen Program Donasi', '• Manajemen Adik Asuh', '• Logout']
        pilihan = menu_navigasi(header, menu)
        # if not pilihan:
        #     print("Inputan tidak boleh kosong.")
        #     continue
        # if not pilihan.isdigit():
        #     print("Inputan harus angka.")
        #     continue

        if pilihan == 0:
            AdminManajemen_ProgramDonasi(program_manager)
        elif pilihan == 1:
            AdminManajemen_AdikAsuh(adik_asuh_manager)
        elif pilihan == 2:
            admin.logout()
        else:
            print("Pilihan tidak valid.")

def AdminManajemen_ProgramDonasi(program_manager):
    while True:
        # print("Halaman Manajemen Program Yayasan")
        # print("1. Lihat Program Yayasan")
        # print("2. Tambah Program Yayasan")
        # print("3. Edit Program Yayasan")
        # print("4. Hapus Program Yayasan")
        # print("Untuk kembali ke menu sebelumnya \"kembali\" untuk menu utama \"menu\" ")
        header = "Halaman Manajemen Program Yayasan"
        menu = ['• Lihat Program Yayasan', '• Tambah Program Yayasan', '• Edit Program Yayasan', '• Hapus Program Yayasan', '• Kembali']
        # pilihan = input("Masukkan Pilihan > ")
        pilihan = menu_navigasi(header,menu)
        # if not pilihan:
        #     print("Inputan tidak boleh kosong.")
        #     continue

        if pilihan == 0:
            lihatProgram(program_manager)
        elif pilihan == 1:
            tambahProgram(program_manager)
        elif pilihan == 2:
            editProgram(program_manager)
        elif pilihan == 3:
            hapusProgram(program_manager)
        elif pilihan == 4:
            break


# def lihatProgram(program_manager):
#     while True:
#         header = "Daftar Program Yayasan"
#         programs = program_manager.lihat_program()
#         options = [nama for id, nama in programs] + ["Kembali"]
#         pilihan = menu_navigasi(header, options)
#         if pilihan < len(programs):
#             program_manager.lihat_detail_program(programs[pilihan][0])
#             lanjut()
#         else:
#             break

def lihatProgram(program_manager):
    while True:
        header = "Daftar Program Yayasan"
        programs = program_manager.lihat_program()
        options = ["• " + nama for id, nama in programs] + ["• Kembali"]
        pilihan = menu_navigasi(header, options)
        if pilihan < len(programs):
            program_id = programs[pilihan][0]
            program_nama = programs[pilihan][1]  
            program = program_manager.lihat_detail_program(program_id)
            if program:
                print(f"Progress Donasi: {program.get_donasi_terkumpul()} / {program.get_target_donasi()}")
                lanjut()
                while True:
                    pembersih()
                    detail_header = f"Detail Program {program_nama}"  
                    detail_options = ["• Melihat Histori Donasi", "• Kembali"]

                    detail_pilihan = submenu_navigasi(detail_header, detail_options)
                    if detail_pilihan == 0:
                        histori_donasi = program_manager.lihat_histori_donasi(program_id)
                        print("===== Histori Donasi =====")
                        for donasi in histori_donasi:
                            print("==================")
                            print(f"Nama Dermawan : {donasi[0]}")
                            print(f"Pesan Donasi  : {donasi[1]}")
                            print(f"Jumlah Donasi : {donasi[2]}")
                            print(f"Tanggal & Waktu Donasi: {donasi[3]}")
                            print("==================")
                        lanjut()
                    else:
                        break
            lanjut()
        else:
            break





def tambahProgram(program_manager):
    nama = input("Nama Program: ")
    deskripsi = input("Deskripsi Program: ")
    target_donasi = float(input("Target Donasi: "))
    donasi_terkumpul = 0.0  
    while True:
        tenggat = input("Tenggat Selesai Pengumpulan Dana (YYYY-MM-DD): ")
        try:
            if not tenggat:
                raise ValueError("Tenggat tidak boleh kosong.")
            datetime.datetime.strptime(tenggat, '%Y-%m-%d')
            break
        except ValueError as e:
            print("Error:", e)

    program = Program(nama, deskripsi, target_donasi, donasi_terkumpul, tenggat)
    program_manager.tambah_program(program)
    lanjut()


def editProgram(program_manager):
    header = "Pilih Program untuk Diedit"
    programs = program_manager.lihat_program()
    options = ["• "+nama for id, nama in programs] + ["• Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(programs):
        idx = programs[pilihan][0]
        nama = input("Nama Program (biarkan kosong jika tidak ingin mengubah): ")
        deskripsi = input("Deskripsi Program (biarkan kosong jika tidak ingin mengubah): ")
        target_donasi = input("Target Donasi (biarkan kosong jika tidak ingin mengubah): ")
        donasi_terkumpul = input("Donasi Terkumpul (biarkan kosong jika tidak ingin mengubah): ")
        while True:
            tenggat = input("Tenggat Selesai Pengumpulan Dana (biarkan kosong jika tidak ingin mengubah): ")
            try:
                if not tenggat:
                    raise ValueError("Tenggat tidak boleh kosong.")
                datetime.datetime.strptime(tenggat, '%Y-%m-%d')
                break
            except ValueError as e:
                print("Error:", e)
        kwargs = {}
        if nama:
            kwargs['nama'] = nama
        if deskripsi:
            kwargs['deskripsi'] = deskripsi
        if target_donasi:
            kwargs['target_donasi'] = float(target_donasi)
        if donasi_terkumpul:
            kwargs['donasi_terkumpul'] = float(donasi_terkumpul)
        if tenggat:
            kwargs['tenggat'] = tenggat
        program_manager.edit_program(idx, **kwargs)
        print("Program berhasil diedit.")
        lanjut()

def hapusProgram(program_manager):
    header = "Pilih Program untuk Dihapus"
    programs = program_manager.lihat_program()
    options = ["• "+nama for id, nama in programs] + ["• Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(programs):
        idx = programs[pilihan][0]
        program_manager.hapus_program(idx)
        lanjut()

# def hapusProgram(program_manager):
#     program_manager.lihat_program()
#     idx = int(input("Pilih nomor program yang akan dihapus: ")) - 1
#     program_manager.hapus_program(idx)
#     print("Program berhasil dihapus.")
#     lanjut()



# QUEST
# Udin
# 1. Beli Seragram > 200 Ribu
# 2. Beli Peralatan Sekolah > 100

# Donatur? pilih udin, otomatis apa yang dibutuhkan Udin donatur harus selesaikan dengan memberikan donasi. ( MENGAMBIL QUEST )



def AdminManajemen_AdikAsuh(adik_asuh_manager):
    while True:
        header = "Halaman Manajemen Adik Asuh"
        menu = ['• Lihat Data Adik Asuh','• Tambah Data Adik Asuh', '• Edit Data Adik Asuh', '• Hapus Data Adik Asuh', '• Kembali']
        pilihan = menu_navigasi(header,menu)

        if pilihan == 0:
            lihatAnakAsuh(adik_asuh_manager)
        elif pilihan == 1:
            tambahAnakAsuh(adik_asuh_manager)
        elif pilihan == 2:
            editAnakAsuh(adik_asuh_manager)
        elif pilihan == 3:
            hapusAnakAsuh(adik_asuh_manager)
        elif pilihan == 4:
            break

def tambahAnakAsuh(adik_asuh_manager):
    pembersih()
    print('''
=====================================================================================================================================================================
                                                                    Tambah Data Adik Asuh
=====================================================================================================================================================================
''')
    nama = input("Nama Adik Asuh: ")
    tempat_tinggal = input("Tempat Tinggal Adik Asuh: ")
    umur = input("Umur Adik Asuh: ")
    kebutuhan = input("Kebutuhan Adik Asuh: ")
    anak = AdikAsuh(nama, tempat_tinggal, umur, kebutuhan)
    adik_asuh_manager.tambah_anak(anak)
    print("Data adik asuh telah ditambahkan")
    lanjut()
    pembersih()

def editAnakAsuh(adik_asuh_manager):
    pembersih()
    header = """
=====================================================================================================================================================================
                                                                    Ubah Data Adik Asuh
=====================================================================================================================================================================
"""
    options = "• "+adik_asuh_manager.lihat_anak() + ["• Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(adik_asuh_manager.anak_asuh):
        idx = pilihan
        nama = input("Nama Adik Asuh (biarkan kosong jika tidak ingin mengubah): ")
        tempat_tinggal = input("Tempat Tinggal Adik Asuh (biarkan kosong jika tidak ingin mengubah): ")
        umur = input("Umur Adik Asuh (biarkan kosong jika tidak ingin mengubah): ")
        kebutuhan = input("Kebutuhan Adik Asuh (biarkan kosong jika tidak ingin mengubah): ")
        kwargs = {}
        if nama:
            kwargs['nama'] = nama
        if tempat_tinggal:
            kwargs['tempat_tinggal'] = tempat_tinggal
        if umur:
            kwargs['umur'] = umur
        if kebutuhan:
            kwargs['kebutuhan'] = kebutuhan
        adik_asuh_manager.edit_anak(idx, **kwargs)
        print("Data adik asuh telah diedit.")
        lanjut()
        pembersih()

def hapusAnakAsuh(adik_asuh_manager):
    pembersih()
    header = """
=====================================================================================================================================================================
                                                                    Hapus Data Adik Asuh
=====================================================================================================================================================================
"""
    options = "• "+adik_asuh_manager.lihat_anak() + ["• Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(adik_asuh_manager.anak_asuh):
        idx = pilihan
        header = "Apakah anda yakin ingin menghapus data ini?"
        options = ['Ya', 'Tidak']
        konfirmasi = menu_navigasi(header, options)
        if konfirmasi == 0:
            adik_asuh_manager.hapus_anak(idx)
            print("Data Adik Asuh dihapus")
            lanjut()
            pembersih()
        elif konfirmasi == 1:
            print("Penghapusan dibatalkan")
            lanjut()
            pembersih()

def lihatAnakAsuh(adik_asuh_manager):
    while True:
        header = """
====================================================================================================================================================================
                                                                    Lihat Data Adik Asuh
====================================================================================================================================================================
"""
        options = "• "+adik_asuh_manager.lihat_anak() + ["• Kembali"]
        pilihan = menu_navigasi(header, options)
        if pilihan < len(adik_asuh_manager.anak_asuh):
            adik_asuh_manager.lihat_detail_anak(pilihan)
            lanjut()
        else:
            break


menuLogin()


# Checkpoint Sementara :
# Mengubah adik asuh ke database.