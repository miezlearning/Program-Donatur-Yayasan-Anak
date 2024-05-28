from tabulate import tabulate
from termcolor import colored

# Membuat data dalam bentuk list
data = [
    ["Ketua", "Budi Santoso", "budi.santoso@example.com"],
    ["Wakil Ketua", "Ani Rahmawati", "ani.rahmawati@example.com"],
    ["Koordinator Pendidikan", "Eko Nugroho", "eko.nugroho@example.com"],
    ["Koordinator Kesehatan", "Fitri Handayani", "fitri.handayani@example.com"],
    ["Koordinator Kesejahteraan", "Gita Pramesti", "gita.pramesti@example.com"],
    ["Sekretaris", "Citra Dewi", "citra.dewi@example.com"],
    ["Bendahara", "Darmawan Putra", "darmawan.putra@example.com"]
]

# Menambahkan warna pada judul kolom
headers = [colored(header, "blue") for header in ["Jabatan", "Nama", "Email"]]

# Menambahkan warna pada baris data
data = [[colored(cell, "yellow") if index != 0 else cell for index, cell in enumerate(row)] for row in data]

# Menampilkan tabel teks dengan tabulate
table = tabulate(data, headers=headers, tablefmt="rounded_outline")
print(table)
