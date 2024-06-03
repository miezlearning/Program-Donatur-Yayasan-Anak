import re
# import yagmail as email
import smtplib
import random
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from etc.kalkulator_zakat import ZakatCalculator
# from etc.topup import send_topup_code, top_up, generate_random_code
import os
import readchar
import getpass
# Modul Koneksi Database 
import mysql.connector
from mysql.connector import Error


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
                print(f"Terjadi kesalahan saat menjalankan query: {e}")
                self.connection.rollback()
                return None
        else:
            print("Tidak dapat membuat koneksi ke database untuk menjalankan query.")
            return None

    def tutup_koneksi(self):
        if self.connection and self.connection.is_connected():
            try:
                self.connection.close()
            except Exception as e:
                print(f"Terjadi kesalahan saat menutup koneksi ke database: {e}")



db = Database()

class warna:
    ungu = "\033[95m"
    hijau = "\033[92m"
    kuning = "\033[93m"
    bold = "\033[1m"
    underline = "\033[4m" 
    merah = "\033[91m"
    reset = "\033[0m"


def validasi_email(email):
    pola = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pola, email):
        return True
    else:
        return False



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
        print('Berhasil, mengirim email...')


def garis():
    print("="*65)

def lanjut():
    print("\n")
    garis()
    print("Press ENTER untuk melanjutkan...")
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

def print_menu(header, menu, selected_index):
    print(header)
    for i, item in enumerate(menu):
        if i == selected_index:
            print(f"> {item}")
        else:
            print(f"  {item}")

def menu_navigasi(header, options):
    selected_index = 0
    while True:
        pembersih()
        print_menu(header,options, selected_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            selected_index = (selected_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            return selected_index
        
def submenu_navigasi(header, options):
    selected_index = 0
    while True:
        pembersih()
        print_menu(header, options, selected_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            selected_index = (selected_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            return selected_index
        
def kalkulatorzakat():
    print("Selamat datang di Kalkulator Zakat")
    calculator = ZakatCalculator()

    calculator.input_asset()

    print("\n-- Hitung Zakat --")
    calculator.hitung_zakat_emas()
    calculator.hitung_zakat_perak()
    calculator.hitung_zakat_tabungan()

    print("\n-- Total Zakat --")
    calculator.hitung_total_zakat()
    return





def generate_random_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

def top_up(amount, donatur):
    if amount <= 5000:
        print("Jumlah pengisian hanya bisa lebih dari Rp. 5.000")
        return

    code = generate_random_code()
    send_topup_code(donatur.get_email(), code)

    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < 120:
        entered_code = input('Masukkan Kode (Cek Email): ')
        print("Tunggu sebentar...")

        if entered_code == code:
            print(f'Top-up berhasil! Total Topup: {amount}')
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
            send_topup_code(donatur.get_email(), code)
            print('Masa berlaku kode habis. Kode baru telah di kirim.')
        else:
            print(f'Kode salah. Sisa waktu pemasukan kode: {int(remaining_time)} Detik.')

def send_topup_code(receiver_email, code):
    sender_email = 'trynore2342@gmail.com'
    app_password = 'osqo ddwe eiyw zlcj'
    subject = 'Top-up Code'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body = f'''
    Hai Donatur,

    Berikut Kode Top-Up: {code}
    Tolong segera mengisi kode tersebut dengan batas 2 menit.

    Salam,
    Yayasan Anak Budi Pekerti
    '''

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


