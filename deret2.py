# Nama File: deret_2.py
# Pembuat: Athallah Nazif Arlis Pratama
# Deskripsi: Mencari suku ke-n dari deret 1, -2, 3, -4, 5, -6,... secara rekursif

# Definisi dan Spesifikasi
# deret_2: integer -> integer
#   {deret_2(n) Mencari suku ke-n dari deret 1, -2, 3, -4, 5, -6,... secara rekursif.}

# Realisasi

def deret_2(n):
    if n == 1: return 1
    return -deret_2(n-1) + (1 if n%2 == 1 else -1)


#Aplikasi
print(deret_2(4))