import re
import yagmail as email

def validasi_email(email):
    pola = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pola, email):
        return True
    else:
        return False

def kirim_forgot_account(nama, username, password, notelp, tujuan):
    user = 'trynore2342@gmail.com'
    app_password = 'osqo ddwe eiyw zlcj'
    subject = 'Lupa Akun ( Yayasan Budi Pekerti )'
    contents = f'''
Halo, {nama}

Berikut adalah informasi akun Anda:
Username: {username}
Password: {password}
No Telepon: {notelp}

Jika Anda tidak meminta informasi ini, mohon abaikan email ini.

Salam,
Yayasan Budi Pekerti
'''

    with email.SMTP(user, app_password) as yag:
        yag.send(tujuan, subject, contents)
        print('Berhasil, mengirim email...')
