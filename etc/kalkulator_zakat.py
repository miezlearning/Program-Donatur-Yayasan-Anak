class ZakatCalculator:
    def __init__(self):
        self.emas = 0
        self.perak = 0
        self.tabungan = 0
        self.hutang = 0

    def input_asset(self):
        self.emas = float(input("Masukkan nilai emas yang Anda miliki (gram): "))
        if self.emas is None:
            raise ValueError("Nilai emas tidak bisa kosong.")
        elif self.emas < 0:
            raise ValueError("Nilai emas tidak bisa kurang dari 0.")
        

        self.perak = float(input("Masukkan nilai perak yang Anda miliki (gram): "))
        if self.perak is None:
            raise ValueError("Nilai perak tidak bisa kosong.")
        elif self.perak < 0:
            raise ValueError("Nilai perak tidak bisa kurang dari 0.")
        

        self.tabungan = float(input("Masukkan jumlah tabungan Anda: "))
        if self.tabungan is None:
            raise ValueError("Jumlah tabungan tidak bisa kosong.")
        elif self.tabungan < 0:
            raise ValueError("Jumlah tabungan tidak bisa kurang dari 0.")
        

        self.hutang = float(input("Masukkan jumlah hutang Anda (jika ada, jika tidak, masukkan 0): "))
        if self.emas is None:
            raise ValueError("Harga emas tidak bisa kosong.")
        elif self.emas < 0:
            raise ValueError("Harga emas tidak bisa kurang dari 0.")

    def hitung_zakat_emas(self):
        nishab_emas = 85  # nishab emas dalam gram
        harga_emas_per_gram = float(input("Masukkan harga emas saat ini (per gram): "))
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
        harga_perak_per_gram = float(input("Masukkan harga perak saat ini (per gram): "))
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
