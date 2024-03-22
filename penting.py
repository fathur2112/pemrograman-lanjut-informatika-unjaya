def tampilkan_daftar_buah(*args):
    print("Buah yang Anda beli adalah:")
    for i, buah in enumerate(args, start=1):
        print(f"{i}. {buah.capitalize()}")

# Main program
print("Toko Buah Koperasi UNJANI Yogyakarta")
jumlah_buah = int(input("Masukkan banyaknya buah yang dibeli: "))

daftar_buah = []
for i in range(jumlah_buah):
    buah = input(f"Buah {i+1}: ")
    daftar_buah.append(buah)

tampilkan_daftar_buah(*daftar_buah)
print("Terima kasih...")