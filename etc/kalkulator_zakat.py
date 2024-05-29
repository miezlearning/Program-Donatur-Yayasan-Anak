class ZakatCalculator:
    def __init__(self):
        self.emas = 0
        self.perak = 0
        self.tabungan = 0
        self.hutang = 0

    def input_asset(self):
        self.emas = float(input("Masukkan nilai emas yang Anda miliki (gram): "))
        self.perak = float(input("Masukkan nilai perak yang Anda miliki (gram): "))
        self.tabungan = float(input("Masukkan jumlah tabungan Anda: "))
        self.hutang = float(input("Masukkan jumlah hutang Anda (jika ada, jika tidak, masukkan 0): "))

    def hitung_zakat_emas(self):
        nishab_emas = 85  # nishab emas dalam gram
        harga_emas_per_gram = float(input("Masukkan harga emas saat ini (per gram): "))
        total_nilai_emas = self.emas * harga_emas_per_gram

        if total_nilai_emas >= nishab_emas:
            zakat_emas = 0.025 * total_nilai_emas
            print(f"Jumlah zakat emas yang harus Anda bayarkan: {zakat_emas} rupiah")
        else:
            print("Anda tidak wajib membayar zakat emas.")

    def hitung_zakat_perak(self):
        nishab_perak = 595  # nishab perak dalam gram
        harga_perak_per_gram = float(input("Masukkan harga perak saat ini (per gram): "))
        total_nilai_perak = self.perak * harga_perak_per_gram

        if total_nilai_perak >= nishab_perak:
            zakat_perak = 0.025 * total_nilai_perak
            print(f"Jumlah zakat perak yang harus Anda bayarkan: {zakat_perak} rupiah")
        else:
            print("Anda tidak wajib membayar zakat perak.")

    def hitung_zakat_tabungan(self):
        if self.tabungan >= 4236133:  # nisab tabungan
            zakat_tabungan = 0.025 * self.tabungan
            print(f"Jumlah zakat tabungan yang harus Anda bayarkan: {zakat_tabungan} rupiah")
        else:
            print("Anda tidak wajib membayar zakat tabungan.")

    def hitung_total_zakat(self):
        total_zakat = 0.025 * (self.emas + self.perak) + 0.025 * self.tabungan - self.hutang
        print(f"Total jumlah zakat yang harus Anda bayarkan: {total_zakat} rupiah")


def main():
    print("Selamat datang di Kalkulator Zakat")
    calculator = ZakatCalculator()

    calculator.input_asset()

    print("\n-- Hitung Zakat --")
    calculator.hitung_zakat_emas()
    calculator.hitung_zakat_perak()
    calculator.hitung_zakat_tabungan()

    print("\n-- Total Zakat --")
    calculator.hitung_total_zakat()


if __name__ == "__main__":
    main()
