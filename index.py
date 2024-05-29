# Selamat Datang di Program Yayasan Budi Pekerti


# ━━━━━━━━━━━━━━━━━━━━━━━━ IMPORT MODULE ━━━━━━━━━━━━━━━━━━━━━━━━ 
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error
# Modul Password Char
from pwinput import pwinput as enkripsi_password
# Modul Fitur Tambahan
from etc.fitur_tambahan import validasi_email, kirim_forgot_account, pembersih , lanjut, org_chart, print_menu, menu_navigasi
# Modul Keymenu


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
                # print("Berhasil Koneksi ke Database")
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
        self.cek_login = True
        
    def get_notelp(self):
        return self.__notelp
    def get_nama(self):
        return self.__nama
    def get_email(self):
        return self.__email
    
    def set_email(self):
        self.__email = self.__email

    def logout(self):
        self.cek_login = False



class Admin(User):
    def __init__(self, nama, username, password):
        super().__init__(username, password)
        self.__nama = nama
        self.cek_login = True
    
    def get_nama(self):
        return self.__nama
    
    def logout(self):
        self.cek_login = False


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

    # Setters
    def set_nama(self, nama):
        self._nama = nama

    def set_deskripsi(self, deskripsi):
        self._deskripsi = deskripsi

    def set_target_donasi(self, target_donasi):
        self._target_donasi = target_donasi

    def set_donasi_terkumpul(self, donasi_terkumpul):
        self._donasi_terkumpul = donasi_terkumpul

    def set_tenggat(self, tenggat):
        self._tenggat = tenggat

    def __str__(self):
        return (f"Nama Program: {self._nama}\n"
                f"Deskripsi: {self._deskripsi}\n"
                f"Target Donasi: {self._target_donasi}\n"
                f"Donasi Terkumpul: {self._donasi_terkumpul}\n"
                f"Tenggat: {self._tenggat}\n")

    def edit(self, nama=None, deskripsi=None, target_donasi=None, donasi_terkumpul=None, tenggat=None):
        if nama:
            self.set_nama(nama)
        if deskripsi:
            self.set_deskripsi(deskripsi)
        if target_donasi:
            self.set_target_donasi(target_donasi)
        if donasi_terkumpul:
            self.set_donasi_terkumpul(donasi_terkumpul)
        if tenggat:
            self.set_tenggat(tenggat)

class ProgramManager:
    def __init__(self):
        self.programs = []

    def tambah_program(self, program):
        self.programs.append(program)

    def lihat_program(self):
        return [program.get_nama() for program in self.programs]

    def lihat_detail_program(self, idx):
        if 0 <= idx < len(self.programs):
            print(self.programs[idx])
        else:
            print("Program tidak ditemukan.")

    def edit_program(self, idx, **kwargs):
        if 0 <= idx < len(self.programs):
            self.programs[idx].edit(**kwargs)
        else:
            print("Program tidak ditemukan.")

    def hapus_program(self, idx):
        if 0 <= idx < len(self.programs):
            del self.programs[idx]
        else:
            print("Program tidak ditemukan.")

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
            kueri = db.query(f"SELECT nama, username, password, role, notelp, email FROM akun WHERE {tipe_kredensial} = '{credential}' AND password = '{password}'")
            if not kueri:
                print(f"{tipe_kredensial} atau password yang dimasukkan salah.")
                lanjut()
                percobaan += 1
            else:
                role = kueri[0][3]
                if role == "Donatur":
                    donatur = Donatur(kueri[0][0], kueri[0][1], password, kueri[0][4], kueri[0][5])
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
        menu = ['Forgot Username', 'Forgot Password', 'Forgot No Telepon', 'Kembali']
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
        menu = ['Dengan Username', 'Dengan No Telepon','Kembali']
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
        # print("1. Tentang Kami")
        # print("2. Program Kami")
        # print("3. Donasi")    
        # print("4. Donasi Mingguan")    
        # print("5. Adik Asuh") 
        # print("6. Pengaturan Akun")
        # print("0. Logout")'
        #             0                1            2           3               4              5               6
        menu = ['Tentang Kami', 'Program Kami', 'Donasi', 'Donasi Mingguan', 'Adik Asuh', 'Pengaturan Akun','Logout']
        pilihan = menu_navigasi(header, menu)

        # pilihan = input("Pilih Menu > ")
        # if not pilihan:
        #     print("Inputan tidak boleh kosong.")
        #     continue
        # if not pilihan.isdigit():
        #     print("Inputan harus angka.")
        #     continue

        if pilihan == 0 :
            TentangKami()
        elif pilihan == 1 :
            UserProgramKami()
        elif pilihan == 2 :
            pass
        elif pilihan == 3 :
            pass
        elif pilihan == 4 :
            pass
        elif pilihan == 5 :
            pass
        elif pilihan == 6 :
            donatur.logout()
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
    lihatProgram()


       

# ━━━━━━━━━━━━━━━━━━━━━━━━ ADMIN STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━ 

def menuAdmin(admin):
    program_manager = ProgramManager()
    while admin.cek_login:
        # print(f"Selamat datang Admin {admin.get_nama()}")
        # print("1. Manajemen Program Donasi")
        # print("2. Manajemen Adik Asuh")
        # print("0. Logout")
        # pilihan = input("Masukkan Pilihan")
        header = f"Selamat datang Admin {admin.get_nama()}"
        menu = ['Manajemen Program Donasi', 'Manajemen Adik Asuh', 'Logout']
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
            AdminManajemen_AdikAsuh()
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
        menu = ['Lihat Program Yayasan', 'Tambah Program Yayasan', 'Edit Program Yayasan', 'Hapus Program Yayasan', 'Kembali']
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


def lihatProgram(program_manager):
    while True:
        header = "Daftar Program Yayasan"
        options = [program.get_nama() for program in program_manager.programs] + ["Kembali"]
        pilihan = menu_navigasi(header, options)
        if pilihan < len(program_manager.programs):
            program_manager.lihat_detail_program(pilihan)
            lanjut()
        else:
            break

def tambahProgram(program_manager):
    nama = input("Nama Program: ")
    deskripsi = input("Deskripsi Program: ")
    target_donasi = float(input("Target Donasi: "))
    donasi_terkumpul = 0.0  
    tenggat = input("Tenggat Selesai Pengumpulan Dana: ")
    program = Program(nama, deskripsi, target_donasi, donasi_terkumpul, tenggat)
    program_manager.tambah_program(program)
    print("Program berhasil ditambahkan.")
    lanjut()

def editProgram(program_manager):
    header = "Pilih Program untuk Diedit"
    options = program_manager.lihat_program() + ["Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(program_manager.programs):
        idx = pilihan
        nama = input("Nama Program (biarkan kosong jika tidak ingin mengubah): ")
        deskripsi = input("Deskripsi Program (biarkan kosong jika tidak ingin mengubah): ")
        target_donasi = input("Target Donasi (biarkan kosong jika tidak ingin mengubah): ")
        donasi_terkumpul = input("Donasi Terkumpul (biarkan kosong jika tidak ingin mengubah): ")
        tenggat = input("Tenggat Selesai Pengumpulan Dana (biarkan kosong jika tidak ingin mengubah): ")
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
    options = program_manager.lihat_program() + ["Kembali"]
    pilihan = menu_navigasi(header, options)
    if pilihan < len(program_manager.programs):
        idx = pilihan
        program_manager.hapus_program(idx)
        lanjut()

def hapusProgram(program_manager):
    program_manager.lihat_program()
    idx = int(input("Pilih nomor program yang akan dihapus: ")) - 1
    program_manager.hapus_program(idx)
    print("Program berhasil dihapus.")
    lanjut()



# QUEST
# Udin
# 1. Beli Seragram > 200 Ribu
# 2. Beli Peralatan Sekolah > 100

# Donatur? pilih udin, otomatis apa yang dibutuhkan Udin donatur harus selesaikan dengan memberikan donasi. ( MENGAMBIL QUEST )

def AdminManajemen_AdikAsuh():
    while True:
        header = "Halaman Manajemen Adik Asuh"
        menu = ['Lihat Data Adik Asuh','Tambah Data Adih Asuh', 'Edit Data Adik Asuh', 'Hapus Data Adik Asuh', 'Kembali']
        pilihan = menu_navigasi(header,menu)

        if pilihan == 0:
            lihatAnak()
        elif pilihan == 1:
            tambahAnak()
        elif pilihan == 2:
            editAnak()
        elif pilihan == 3:
            hapusAnak()
        elif pilihan == 4:
            break

def tambahAnak():
    pembersih()
    print('''
=====================================================================================================================================================================
                                                                    Tambah Data Adik Asuh
=====================================================================================================================================================================
''')
    a = input("Nama Adik Asuh: ")
    b = input("Tempat Tinggal Adik Asuh: ")
    c = input("Umur Adik Asuh: ")
    d = input("Kebutuhan Adik Asuh: ")
    # cek data yang sama
    # if a == class atau panggil metode cek data sama
    print ("Data adik asuh telah ditambahkan")
    lanjut()
    pembersih()
    return

def editAnak():
    pembersih()
    header = """
=====================================================================================================================================================================
                                                                    Ubah Data Adik Asuh
=====================================================================================================================================================================
"""
    options = ["Kembali"] # + classadikasuh.liat()
    pilihan = menu_navigasi(header, options)
    # if pilihan < len(program_manager.programs):
    #     idx = input("Nama Adik Asuh: ")
    #     a = input("Nama Adik Asuh: ")
    #     b = input("Tempat Tinggal Adik Asuh: ")
    #     c = input("Umur Adik Asuh: ")
    #     d = input("Kebutuhan Adik Asuh: ")
    #     pembersih()
    #     return

def hapusAnak():
    pembersih()
    header = """
=====================================================================================================================================================================
                                                                    Hapus Data Adik Asuh
=====================================================================================================================================================================
"""
    options = ["Kembali"] # + classadikasuh.liat()
    pilihan = menu_navigasi(header, options)
    # if pilihan < len(program_manager.programs):
        # header = "Apakah anda yakin ingin menghapus data ini?"
        # options = ['Ya', 'Tidak']
        # konfirmasi = menu_navigasi(header, options)
        # if konfirmasi == 1:
        #     class.hapusanak(pilihan)
        #     print("Data Adik Asuh di Hapus")
        #     lanjut()
        #     pembersih()
        #     return
        # elif konfirmasi == 2:
        #     print("Penghapusan Dibatalkan")
        #     lanjut()
        #     pembersih()
        #     return

def lihatAnak():
#     while True:
#         header = """
# =====================================================================================================================================================================
#                                                                     Lihat Data Adik Asuh
# =====================================================================================================================================================================
# """
#         options = [program.get_nama() for program in program_manager.programs] + ["Kembali"]
#         pilihan = menu_navigasi(header, options)
#         if pilihan < len(program_manager.programs):
#             program_manager.lihat_detail_program(pilihan)
#             lanjut()
#         else:
#             break
    pass

menuLogin()