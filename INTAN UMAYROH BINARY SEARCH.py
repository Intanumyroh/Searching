def binary_search(arr, x):
    """
    Melakukan binary search untuk menemukan elemen x dalam array arr.
    
    Parameters:
    arr (list): Daftar elemen yang sudah diurutkan.
    x (int): Elemen yang ingin dicari.
    
    Returns:
    int: Indeks dari elemen jika ditemukan, -1 jika tidak ditemukan.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        
        # Membandingkan elemen tengah dengan x
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # Elemen ditemukan
    
    return -1  # Elemen tidak ditemukan

def is_odd(number):
    """
    Mengecek apakah sebuah bilangan adalah ganjil.
    
    Parameters:
    number (int): Bilangan yang akan dicek.
    
    Returns:
    bool: True jika bilangan adalah ganjil, False jika tidak.
    """
    return number % 2 != 0

def main():
    # Menerima input daftar elemen ganjil yang sudah terurut dari pengguna
    arr = list(map(int, input("Masukkan daftar bilangan ganjil yang sudah terurut, pisahkan dengan spasi: ").split()))

    # Memastikan semua elemen dalam daftar adalah ganjil
    if not all(is_odd(num) for num in arr):
        print("Daftar hanya boleh berisi bilangan ganjil.")
        return

    # Menerima input bilangan ganjil yang ingin dicari
    x = int(input("Masukkan bilangan ganjil yang dicari: "))   
    
    # Mengecek apakah x adalah bilangan ganjil
    if not is_odd(x):
        print("Bilangan yang dicari harus ganjil.")
        return

    # Memanggil fungsi binary_search
    result = binary_search(arr, x)

    if result != -1:
        print(f"Bilangan {x} ditemukan pada indeks {result}.")
    else:
        print(f"Bilangan {x} tidak ditemukan dalam daftar.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
