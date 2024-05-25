import yagmail

user = 'trynore2342@gmail.com'
app_password = 'osqo ddwe eiyw zlcj' 
to = 'm.alif7890@gmail.com'
subject = 'Email Python'
contents = "Bintang putra sadewa"

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, contents)
    print('Berhasil, mengirim email...')
    print('Segera cek email kamu' + to)