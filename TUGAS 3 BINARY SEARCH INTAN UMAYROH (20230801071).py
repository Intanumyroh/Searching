def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Jika elemen berada di tengah
        if arr[mid] < x:
            low = mid + 1

        # Jika elemen berada di sebelah kiri tengah
        elif arr[mid] > x:
            high = mid - 1

        # Elemen ditemukan
        else:
            return mid 

    # Elemen tidak ditemukan
    return -1

def main():
    # Menerima input data daftar elemen yang sudah terurut dari pengguna
    arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut, pisahkan dengan spasi: ").split()))

    # Menerima input elemen yang ingin dicari
    x = int(input("Masukkan elemen yang dicari: "))   

    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()