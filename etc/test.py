import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

def submit():
    tenggat = calendar.get_date()
    if not tenggat:
        messagebox.showerror("Error", "Tenggat tidak boleh kosong.")
    else:
        print("===== Informasi Program =====")
        print("Nama Program:", nama)
        print("Deskripsi Program:", deskripsi)
        print("Target Donasi:", target_donasi)
        print("Tenggat Selesai Pengumpulan Dana:", tenggat)
        messagebox.showinfo("Informasi Program", f"Nama Program: {nama}\nDeskripsi Program: {deskripsi}\nTarget Donasi: {target_donasi}\nTenggat Selesai Pengumpulan Dana: {tenggat}")

nama = input("Nama Program: ")
deskripsi = input("Deskripsi Program: ")
target_donasi = input("Target Donasi: ")

app = tk.Tk()
app.title("Pengumpulan Dana")
app.geometry("400x250")

tk.Label(app, text="Tenggat Selesai Pengumpulan Dana (YYYY-MM-DD):", font=("Helvetica", 12)).pack(pady=5)
calendar = DateEntry(app, font=("Helvetica", 12), date_pattern='yyyy-mm-dd')
calendar.pack(pady=5)

submit_button = tk.Button(app, text="Submit", font=("Helvetica", 12), command=submit)
submit_button.pack(pady=10)

app.mainloop()
