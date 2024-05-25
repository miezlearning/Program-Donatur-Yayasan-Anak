def get_personal_info():
    print("=== Informasi Pribadi ===")
    name = input("Nama Lengkap: ")
    dob = input("Tanggal Lahir (DD-MM-YYYY): ")
    address = input("Alamat: ")
    phone = input("Nomor Telepon: ")
    email = input("Email: ")
    marital_status = input("Status Pernikahan: ")
    return {
        "Nama": name,
        "Tanggal Lahir": dob,
        "Alamat": address,
        "Nomor Telepon": phone,
        "Email": email,
        "Status Pernikahan": marital_status
    }

def get_spouse_info():
    print("=== Informasi Pasangan (Jika Berlaku) ===")
    has_spouse = input("Apakah Anda memiliki pasangan? (yes/no): ").strip().lower()
    if has_spouse == 'yes':
        name = input("Nama Lengkap Pasangan: ")
        dob = input("Tanggal Lahir Pasangan (DD-MM-YYYY): ")
        phone = input("Nomor Telepon Pasangan: ")
        return {
            "Nama Pasangan": name,
            "Tanggal Lahir Pasangan": dob,
            "Nomor Telepon Pasangan": phone
        }
    return {}

def get_family_info():
    print("=== Informasi Keluarga ===")
    num_children = input("Jumlah Anak yang Dimiliki Saat Ini: ")
    if int(num_children) > 0:
        children_info = []
        for i in range(int(num_children)):
            print(f"--- Anak {i+1} ---")
            name = input("Nama: ")
            age = input("Umur: ")
            children_info.append({"Nama": name, "Umur": age})
        return {
            "Jumlah Anak": num_children,
            "Anak-anak": children_info
        }
    return {"Jumlah Anak": num_children}

def get_adoption_motivation():
    print("=== Motivasi Adopsi ===")
    reason = input("Alasan Mengadopsi Anak: ")
    return {"Alasan Adopsi": reason}

def main():
    print("Formulir Pendaftaran Calon Pengadopsi")
    personal_info = get_personal_info()
    spouse_info = get_spouse_info()
    family_info = get_family_info()
    adoption_motivation = get_adoption_motivation()
    
    # Display collected information (for demonstration purposes)
    print("\n=== Informasi yang Dikirim ===")
    print("Informasi Pribadi:")
    for key, value in personal_info.items():
        print(f"{key}: {value}")
    
    if spouse_info:
        print("\nInformasi Pasangan:")
        for key, value in spouse_info.items():
            print(f"{key}: {value}")
    
    print("\nInformasi Keluarga:")
    for key, value in family_info.items():
        if key == "Anak-anak":
            for child in value:
                print(f"  Anak - Nama: {child['Nama']}, Umur: {child['Umur']}")
        else:
            print(f"{key}: {value}")
    
    print("\nMotivasi Adopsi:")
    for key, value in adoption_motivation.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
