jumlah_penumpang = 3

if jumlah_penumpang > 10:
    print("mobil berjalan")

if jumlah_penumpang < 10:
    print("mobil menunggu penumpang lain")

print("di luar condition")


skor = 78

if skor > 75:
    print("lulus")
elif skor < 10:
    print('tidak lulus')

if skor >= 85:
    print("memuaskan")
elif skor >= 75:
    print("bagus")
else:
    print('bodoh')


#if didalam if 
kelas = 3
skore = 50

if kelas > 1:

    if skore >= 85:
        print("memuaskan")
    elif skore >= 75:
        print("bagus")
    else:
        print('bodoh')  

else:

    if skore >= 80:
        print('bagus')
    else:
        print('tidak lulus')


#kondisi inputan
inp = float(input('masukkan angka : '))

if inp >= 0:
    if inp == 0:
        print('nol')
    else:
        print('angka positif')
else:
    print('angka negatif')