# Nama File: penjumlahan_suku2.py
# Pembuat: Athallah Nazif Arlis Pratama
# tanggal 02/10/2026
# Deskripsi: Menjumlahkan suku pertama sampai ke-15 (S15) dari deret 1 + 2 + 4 + 8 + 16 + 32...(n15) secara rekursif

# Definisi dan Spesifikasi
# penjumlahan_suku2: integer -> integer
#   {deret_2(n)  Menjumlahkan suku pertama sampai ke-15 (S15) dari deret 1 + 2 + 4 + 8 + 16 + 32...(n15) secara rekursif}

# Realisasi


def penjumlahan_suku2(n):
    if n == 0: return 0
    return penjumlahan_suku2(n-1) + 2**(n-1)


#Aplikasi
print(penjumlahan_suku2(15))

