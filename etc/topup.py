# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

# def kirim_forgot_account(nama, username, password, notelp, tujuan):
#     sender_email = 'trynore2342@gmail.com'
#     app_password = 'osqo ddwe eiyw zlcj'
#     subject = 'Lupa Akun ( Yayasan Budi Pekerti )'
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = tujuan
#     msg['Subject'] = subject

#     # Isi email
#     body = f'''
#     <html>
#     <body>
#         <img src="cid:banner_lupa_akun" style="width: 507px; height: 127px; aspect-ratio: auto 507 / 127;">
#         <p>Halo, <b>{nama}</b>,</p>
#         <p>Berikut adalah informasi akun Anda:</p>
#         <ul>
#             <li>Username: {username}</li>
#             <li>Password: {password}</li>
#             <li>No Telepon: {notelp}</li>
#         </ul>
#         <p>Jika Anda tidak meminta informasi ini, mohon abaikan email ini.</p>
#         <p>Salam,<br>Yayasan Budi Pekerti</p>
#     </body>
#     </html>
#     '''
#     msg.attach(MIMEText(body, 'html'))
#     # Lampirkan gambar
#     gambar_path = 'etc/media/banner_lupa_akun.jpeg'
#     with open(gambar_path, 'rb') as fp:
#         img = MIMEImage(fp.read())
#         img.add_header('Content-ID', '<banner_lupa_akun>')
#         img.add_header('Content-Disposition', 'inline', filename='Banner.jpeg')
#         msg.attach(img)

#     # Kirim email
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#         server.login(sender_email, app_password)
#         server.send_message(msg)
#         print('Berhasil, mengirim email...')


import smtplib
import random
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_random_code():
    # Generate a random code consisting of uppercase letters and digits
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

def send_email(receiver_email, code):
    sender_email = 'trynore2342@gmail.com'
    app_password = 'osqo ddwe eiyw zlcj'
    subject = 'Top-up Code'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    body = f'''
    Hi there,
    
    Here is your top-up code: {code}
    Please use it to complete the top-up process within 2 minutes.
    
    Regards,
    Your App Team
    '''
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

def top_up(amount):
    code = generate_random_code()
    
    receiver_email = 'm.alif7890@gmail.com'
    send_email(receiver_email, code)
    
    start_time = time.time()
    elapsed_time = 0
    
    while elapsed_time < 120:
        entered_code = input('Enter the code received via email: ')
        
        if entered_code == code:
            print(f'Top-up successful! Amount: {amount}')
            break
        
        elapsed_time = time.time() - start_time
        remaining_time = 120 - elapsed_time
        
        if remaining_time <= 0:
            # Code expired, generate a new code
            code = generate_random_code()
            start_time = time.time()
            elapsed_time = 0
            send_email(receiver_email, code)
            print('Code expired. New code has been sent.')
        else:
            print(f'Invalid code. Remaining time: {int(remaining_time)} seconds.')
# Usage example
top_up(100)