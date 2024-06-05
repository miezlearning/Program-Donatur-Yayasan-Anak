import re
# import yagmail as email
import smtplib
import random
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# from etc.topup import send_topup_code, top_up, generate_random_code
import os
import readchar
import getpass
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error
import threading
from tabulate import tabulate
# Modul Kebutuhan Loading Bar
from progressbar import ProgressBar, Percentage, Bar




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
            error(f"Terjadi kesalahan saat menghubungkan ke database: {e}")
            return None

    def query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            self.connection = self.koneksi()
        if self.connection:
            try:
                CMD = self.connection.cursor()
                CMD.execute(query, params)
                result = CMD.fetchall()
                self.connection.commit()
                return result
            except Error as e:
                error(f"Terjadi kesalahan saat menjalankan query: {e}")
                self.connection.rollback()
                return None
        else:
            error("Tidak dapat membuat koneksi ke database untuk menjalankan query.")
            return None

    def tutup_koneksi(self):
        if self.connection and self.connection.is_connected():
            try:
                self.connection.close()
            except Exception as e:
                error(f"Terjadi kesalahan saat menutup koneksi ke database: {e}")

class ZakatCalculator:
    def __init__(self):
        self.emas = 0
        self.perak = 0
        self.tabungan = 0
        self.hutang = 0

    def input_asset(self):
        while True:
            try:
                self.emas = float(input(f"{warna.biru+warna.bold}Masukkan nilai emas yang Anda miliki (gram) > {warna.reset}"))
                if self.emas < 0:
                    raise ValueError("Nilai emas tidak bisa kurang dari 0.")
                break  

            except ValueError:
                print("Masukan harus berupa angka.")

        while True:
            try:
                self.perak = float(input(f"{warna.biru+warna.bold}Masukkan nilai perak yang Anda miliki (gram) > {warna.reset}"))
                if self.perak < 0:
                    raise ValueError("Nilai perak tidak bisa kurang dari 0.")
                break  

            except ValueError:
                print("Masukan harus berupa angka.")

        while True:
            try:
                self.tabungan = float(input(f"{warna.biru+warna.bold}Masukkan jumlah tabungan Anda > {warna.reset}"))
                if self.tabungan < 0:
                    raise ValueError("Jumlah tabungan tidak bisa kurang dari 0.")
                break  

            except ValueError:
                print("Masukan harus berupa angka.")

        while True:
            try:
                self.hutang = float(input(f"{warna.biru+warna.bold}Masukkan jumlah hutang Anda (jika ada, jika tidak, masukkan 0) > {warna.reset}"))
                if self.hutang < 0:
                    raise ValueError("Jumlah hutang tidak bisa kurang dari 0.")
                break  

            except ValueError:
                print("Masukan harus berupa angka.")

    def hitung_zakat_emas(self):
        nishab_emas = 85  # nishab emas dalam gram
        harga_emas_per_gram = float(input(f"{warna.biru+warna.bold}Masukkan harga emas saat ini (per gram) > {warna.reset}"))
        if harga_emas_per_gram is None:
            raise ValueError("Harga emas tidak bisa kosong.")
        elif harga_emas_per_gram <= 0:
            raise ValueError("Harga emas tidak bisa kurang dari 0.")
        total_nilai_emas = self.emas * harga_emas_per_gram

        if total_nilai_emas >= nishab_emas:
            zakat_emas = 0.025 * total_nilai_emas
            return f"Jumlah zakat emas yang harus Anda bayarkan: {zakat_emas} rupiah"
        else:
            return "Anda tidak wajib membayar zakat emas."

    def hitung_zakat_perak(self):
        nishab_perak = 595  # nishab perak dalam gram
        harga_perak_per_gram = float(input(f"{warna.biru+warna.bold}Masukkan harga perak saat ini (per gram) > {warna.reset}"))
        if harga_perak_per_gram is None:
            raise ValueError("Harga perak tidak bisa kosong.")
        elif harga_perak_per_gram <= 0:
            raise ValueError("Harga perak tidak bisa kurang dari 0.")
        total_nilai_perak = self.perak * harga_perak_per_gram

        if total_nilai_perak >= nishab_perak:
            zakat_perak = 0.025 * total_nilai_perak
            return f"Jumlah zakat perak yang harus Anda bayarkan: {zakat_perak} rupiah"
        else:
            return "Anda tidak wajib membayar zakat perak."

    def hitung_zakat_tabungan(self):
        if self.tabungan >= 70000:  # nisab tabungan
            zakat_tabungan = 0.025 * self.tabungan
            return f"Jumlah zakat tabungan yang harus Anda bayarkan: {zakat_tabungan} rupiah"
        else:
            return "Anda tidak wajib membayar zakat tabungan."

    def hitung_total_zakat(self):
        total_zakat = 0.025 * (self.emas + self.perak) + 0.025 * self.tabungan - self.hutang
        return f"Total jumlah zakat yang harus Anda bayarkan: {total_zakat} rupiah"


db = Database()

from rich.progress import track
from time import sleep

def proses_loading():
    sleep(0.01)

def loading_bar():
    for _ in track(range(100), description=f'[read]{warna.bold}Mohon Bersabar{warna.reset}'):
        proses_loading()
    berhasil("Login Berhasil")
    lanjut()

class warna:
    ungu = "\033[95m"
    hijau = "\033[92m"
    kuning = "\033[93m"
    bold = "\033[1m"
    biru = "\033[0;34m"
    biru_tebel = "\033[1;34m"
    underline = "\033[4m" 
    merah = "\033[91m"
    putih = "\033[0;37m"
    putih_bg = "\033[47m"
    reset = "\033[0m"


def validasi_email(email):
    pola = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pola, email):
        return True
    else:
        return False

def error(p):
    print(warna.merah + "[ERROR] >> " + p + warna.reset)

def berhasil(p):
    print(warna.hijau + "[BERHASIL] >> " + p + warna.reset)

def info(p):
    print(warna.kuning + "\n[INFORMATION] >> " + p + warna.reset)

def donasi_berhasil(p, jumlah_donasi):
    print(warna.hijau + "[DONASI BERHASIL] >> " + p  + f"{warna.reset}Jumlah Donasi : {jumlah_donasi}"+ warna.reset)

def kirim_forgot_account(nama, username, password, notelp, tujuan):
    sender_email = 'trynore2342@gmail.com'
    app_password = 'osqo ddwe eiyw zlcj'
    subject = 'Lupa Akun ( Yayasan Budi Pekerti )'
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = tujuan
    msg['Subject'] = subject

    # Isi email
    body = f'''
    <html>
    <body>
        <img src="cid:banner_lupa_akun" style="width: 507px; height: 127px; aspect-ratio: auto 507 / 127;">
        <p>Halo, <b>{nama}</b>,</p>
        <p>Berikut adalah informasi akun Anda:</p>
        <ul>
            <li>Username: {username}</li>
            <li>Password: {password}</li>
            <li>No Telepon: {notelp}</li>
        </ul>
        <p>Jika Anda tidak meminta informasi ini, mohon abaikan email ini.</p>
        <p>Salam,<br>Yayasan Budi Pekerti</p>
    </body>
    </html>
    '''
    msg.attach(MIMEText(body, 'html'))

    # Lampirkan gambar
    gambar_path = 'etc/media/banner_lupa_akun.jpeg'
    with open(gambar_path, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<banner_lupa_akun>')
        img.add_header('Content-Disposition', 'inline', filename='Banner.jpeg')
        msg.attach(img)

    # Kirim email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        berhasil('Berhasil, mengirim email...')


def garis():
    print("="*65)



def lanjut():
    print("\n")
    garis()
    print(warna.bold + warna.kuning + "Press ENTER "+warna.reset + warna.bold +"untuk melanjutkan..." + warna.reset)
    # test = getpass.getpass(stream=None)
    garis()
    # input()
    test = getpass.getpass(prompt="\033[0m",stream=None)
    # sys.stdout.write("\033[F")

def pembersih():
    os_name = os.name

    if os_name == 'posix': 
        os.system('clear')
    elif os_name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def org_chart():
    print('''
                            _______________________________________________________
                            |                         Yayasan                      |
                            |                       Budi Pekerti                   |
                            |______________________________________________________|
                                        |
                                        |-- Dewan Pembina
                                        |       |-- Ketua Dewan Pembina
                                        |       |-- Anggota Dewan Pembina
                                        |
                                        |-- Dewan Pengawas
                                        |       |-- Ketua Dewan Pengawas
                                        |       |-- Anggota Dewan Pengawas
                                        |
                                        |-- Dewan Pengurus
                                                |-- Ketua Yayasan
                                                |-- Wakil Ketua Yayasan
                                                |-- Sekretaris
                                                |-- Bendahara
                            _______________________________________________________
    ''')


def print_menu(header, menu, selected_index, info_message=None, style=None):
    menu_table = [["Pilih","Menu"]]
    for i, item in enumerate(menu):
        if i == selected_index:
            menu_table.append([f"{warna.bold + warna.biru_tebel}>{warna.reset}", warna.biru_tebel+warna.putih_bg+item])
        else:
            menu_table.append(["", item])
    print(header)
    if info_message:
        if style:
            style(info_message)
        else:
            print(warna.bold + info_message + warna.reset)

    table_str = tabulate(menu_table, headers="firstrow", tablefmt="rounded_outline")
    for line in table_str.split('\n'):
        if "➤" in line:
            print(f"{line}{warna.reset}")
        else:
            print(f"{warna.putih}{line}{warna.reset}")


def menu_navigasi(header, options, info_message=None, style=None):
    selected_index = 0
    while True:
        pembersih()
        print_menu(header, options, selected_index, info_message, style)
        key = readchar.readkey()
        if key == readchar.key.UP:
            selected_index = (selected_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            return selected_index

        
def kalkulatorzakat():
    while True:
        pembersih()
        calculator = ZakatCalculator()
        try:
            calculator.input_asset()

            print("\n-- Hitung Zakat --")
            
            
            txt = calculator.hitung_zakat_emas()
            info(txt)

            txt = calculator.hitung_zakat_perak()
            info(txt)

            txt = calculator.hitung_zakat_tabungan()
            info(txt)

            print("\n-- Total Zakat --")
            txt = calculator.hitung_total_zakat()
            info(txt)
            lanjut()
            break
        except ValueError as e:
            error(e)




def generate_random_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

def top_up(amount, donatur):
    if amount <= 5000:
        info("Jumlah pengisian hanya bisa lebih dari Rp. 5.000")
        return

    code = generate_random_code()
    send_topup_code(donatur.get_nama(),donatur.get_email(), code)

    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < 120:
        entered_code = input('Masukkan Kode (Cek Email): ')
        print("Tunggu sebentar...")

        if entered_code == code:
            berhasil(f'Top-up berhasil! Total Topup: {amount}')
            query = "UPDATE akun SET dompet = dompet + %s WHERE id_akun = %s"
            params = (amount, donatur.get_id())
            db.query(query, params)
            db.tutup_koneksi()
            donatur.set_dompet(donatur.get_dompet() + amount)
            break

        elapsed_time = time.time() - start_time
        remaining_time = 120 - elapsed_time

        if remaining_time <= 0:
            code = generate_random_code()
            start_time = time.time()
            elapsed_time = 0
            send_topup_code(donatur.get_nama(), donatur.get_email(), code)
            info('Masa berlaku kode habis. Kode baru telah di kirim.')
        else:
            error(f'Kode salah. Sisa waktu pemasukan kode: {int(remaining_time)} Detik.')

def send_topup_code(nama, receiver_email, code):
    sender_email = 'trynore2342@gmail.com'
    app_password = 'osqo ddwe eiyw zlcj'
    subject = 'Top-up Code'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body = f'''
    <html>
    <body>
        <img src="cid:banner_topup" style="width: 507px; height: 127px; aspect-ratio: auto 507 / 127;">
        <p>Hai Donatur, <b>{nama}</b>,</p>
        <p>Berikut adalah informasi top-up Anda:</p>
        <h3> Berikut Kode Top-Up: {code} </h3>
        <p>Jika Anda tidak meminta informasi ini, mohon abaikan email ini.</p>
        <p>Salam,<br>Yayasan Budi Pekerti</p>
    </body>
    </html>
    '''
    

    gambar_path = 'etc/media/banner_topup.jpg'
    with open(gambar_path, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<banner_topup>')
        img.add_header('Content-Disposition', 'inline', filename='Banner.jpeg')
        msg.attach(img)

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


class AutoDonasi:
    def __init__(self, donatur, program_manager, program_id, jumlah):
        self.donatur = donatur
        self.program_manager = program_manager
        self.program_id = program_id
        self.jumlah = jumlah
        self.active = False
        self.thread = None

    def start(self):
        self.active = True
        self.thread = threading.Thread(target=self.donasi_berkala)
        self.thread.start()

    def stop(self):
        self.active = False
        if self.thread:
            self.thread.join()

    def donasi_berkala(self):
        while self.active:
            if self.donatur.get_dompet() >= self.jumlah:
                self.donatur.kurangi_dompet(self.jumlah)
                update_dompet(self.donatur.get_id(), -self.jumlah)
                self.program_manager.update_donasi_terkumpul(self.program_id, self.jumlah)  
                self.program_manager.catat_donasi(
                    self.donatur.get_id(),
                    self.program_id,
                    self.jumlah,
                    self.donatur.get_nama(),
                    "Donasi otomatis"
                )
                berhasil(f"Donasi otomatis sebesar {self.jumlah} dari {self.donatur.get_nama()} telah diproses.")
            else:
                info("Saldo tidak mencukupi untuk donasi otomatis.")
                self.stop()
            time.sleep(10)  

def update_dompet(user_id, amount):
    query = "UPDATE akun SET dompet = dompet + %s WHERE id_akun = %s"
    params = (amount, user_id)
    db.query(query, params)

