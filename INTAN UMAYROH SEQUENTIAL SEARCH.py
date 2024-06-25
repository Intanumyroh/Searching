# Fungsi untuk menambahkan baju ke dalam daftar
def add_baju():
    baju_list = []
    while True:
        try:
            id_baju = int(input("Masukkan ID baju: "))
            nama_baju = input("Masukkan nama baju: ").strip()  # Menghapus spasi di awal/akhir
            harga_baju = int(input("Masukkan harga baju: "))
            
            baju_list.append({"id": id_baju, "nama": nama_baju, "harga": harga_baju})
            
            lagi = input("Apakah Anda ingin menambahkan baju lagi? (y/n): ").lower().strip()
            if lagi != 'y':
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan data dengan benar.")
    return baju_list

# Fungsi untuk mencari baju berdasarkan nama
def search_by_name(baju_list, target_name):
    target_name = target_name.lower().strip()  # Normalisasi input pencarian
    for baju in baju_list:
        if baju["nama"].lower() == target_name:
            return baju
    return None

# Fungsi untuk menampilkan daftar baju
def show_baju_list(baju_list):
    if not baju_list:
        print("\nDaftar baju kosong.")
        return
    
    print("\nDaftar Baju:")
    for i, baju in enumerate(baju_list, 1):
        print(f"{i}. ID: {baju['id']}, Nama: {baju['nama']}, Harga: {baju['harga']}")

# Fungsi utama untuk menjalankan program
def search_baju_program():
    print("\n--- Selamat Datang di Program Pencarian Baju ---")
    baju_list = add_baju()
    
    while True:
        print("\nSilakan pilih opsi:")
        print("1. Tampilkan daftar baju")
        print("2. Cari baju berdasarkan nama")
        
        try:
            choice = int(input("Masukkan pilihan Anda: ").strip())
        except ValueError:
            print("Pilihan tidak valid. Harap masukkan angka.")
            continue
        
        if choice == 1:
            show_baju_list(baju_list)
        elif choice == 2:
            target_name = input("Masukkan nama baju yang ingin dicari: ").strip()
            if not target_name:
                print("Nama baju tidak boleh kosong.")
                continue

            result = search_by_name(baju_list, target_name)
            
            if result:
                print(f"\nBaju dengan nama '{target_name}' ditemukan:")
                print(f"ID: {result['id']}")
                print(f"Harga: {result['harga']}")
            else:
                print(f"\nBaju dengan nama '{target_name}' tidak ditemukan")
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")
        
        again = input("\nApakah Anda ingin melakukan aksi lain? (y/n): ").lower().strip()
        if again != 'y':
            break

    print("\nTerima kasih telah menggunakan program pencarian baju!")

# Jalankan program
search_baju_program()
