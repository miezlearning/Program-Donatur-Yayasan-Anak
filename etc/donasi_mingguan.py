import time

class Donasi:
    def __init__(self, jumlah, donatur):
        self.jumlah = jumlah
        self.donatur = donatur

class RekeningYayasan:
    def __init__(self, nama):
        self.nama = nama
        self.saldo = 0
        self.donasi_terkumpul = []

    def terima_donasi(self, donasi):
        self.saldo += donasi.jumlah
        self.donasi_terkumpul.append(donasi)
        print(f"Donasi sebesar {donasi.jumlah} dari {donasi.donatur} telah diterima. Total saldo: {self.saldo}")

def main():
    nama_yayasan = "Yayasan Anak Bangsa"
    yayasan = RekeningYayasan(nama_yayasan)

    donatur = "Budi"
    jumlah_donasi = 100000  # jumlah donasi dalam rupiah

    try:
        while True:
            donasi = Donasi(jumlah_donasi, donatur)
            yayasan.terima_donasi(donasi)
            time.sleep(6)  # jeda 6 detik antara donasi
    except KeyboardInterrupt:
        print("\nPenghentian donasi otomatis oleh pengguna.")

if __name__ == "__main__":
    main()
