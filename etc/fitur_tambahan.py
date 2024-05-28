import re
# import yagmail as email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import readchar

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
        <p>Halo, {nama},</p>
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
    garis()
    input()

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
                            |                        Budi Pekerti                  |
                            |                       Yayasan Sosial                 |
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