#if
jumlah_penumpang = 12

if jumlah_penumpang > 10:
    print("mobil jalan")

if jumlah_penumpang < 10:
    print("nunggu")

#hasil akan true jika jumlah penumpang diatas 10
print("kond 1: jumlah_penumpang > 10", jumlah_penumpang > 10)


#if else
nilai = int(input("masukkan nilai: "))
if nilai > 75:
    print("lulus")
else: print("tidak lulus")

#else if (elif)
if nilai == 100:
    print("perfect")
elif nilai > 75:
    print("oke")
else: 
    print("tidak oke")

