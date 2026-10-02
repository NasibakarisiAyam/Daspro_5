# Nama File: Pembagian.py
# Pembuat: Athallah Nazif Arlis Pratama
# tanggal 02/10/2026
# Deskripsi: Membagi dua bilangan secara rekursif

# Definisi dan Spesifikasi
# Pembagian: 2integer -> integer
#   {Pembagian(a,b) membagi a dengan b secara rekursif.}

# Realisasi
def pembagian(a,b):
    return(
        "Undifined" if b == 0 else
        a if b == 1 else
        -pembagian(a,-b) if b < 0 else
        -pembagian(-a,b) if a < 0 else
        pembagian(-a,-b) if a < 0 and b < 0 else
        0 if a < b
        else 1+pembagian(a-b,b)
    )

#Aplikasi
print(pembagian(32,8))