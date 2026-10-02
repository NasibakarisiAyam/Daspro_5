# Nama File: pengurangan.py
# Pembuat: Athallah Nazif Arlis Pratama
# tanggal 02/10/2026
# Deskripsi: Mengurangkan dua bilangan secara rekursif

# Definisi dan Spesifikasi
# pengurangan: 2integer -> integer
#   {pengurangan(a,b) mengurangkan dua bilangan a dan b secara rekursif.}

# Realisasi
def pengurangan(a,b):
    if b == 0: return a
    elif b<0: return pengurangan(a+1,b+1)
    return pengurangan(a-1, b-1)

print(pengurangan(-3,-1))