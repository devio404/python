#syntax error
# car_list = ['nissan', 'porsche', 'maserati']
# for car in car_list
#     print(car)

#logical error
# hasilnya akan error dan program akan langsung break
# nilai = 100
# bagi = 0
# hasil = nilai/bagi
# print(hasil)
# print('instruksi setelah bagi')

#jika error maka akan memunculkan isi dari except dan tidak akan terjadi break
try: 
    nilai = 100
    bagi = 0
    hasil = nilai/bagi
    print(hasil)
except:
    print('maaf, hasil pembagian error')

print('instruksi setelah bagi')

#akan menampilkan detail error nya
# try: 
#     nilai = 100
#     bagi = 0
#     hasil = nilai/bagi
#     print(hasil)
# except Exception as er:
#     print('maaf, terjadi error', er.__class__, '.')

#membuat program error sendiri
class valueToSmallError(Exception):
    pass

class valueToBigError(Exception):
    pass

goal = 14

while True:

    try:
        masukan = int(input("ketikkan angka: "))
        if masukan < goal:
            raise valueToSmallError
        elif masukan > goal:
            raise valueToBigError
        break

    except valueToSmallError:
        print('angka yang dimasukkan terlalu kecil')
    except valueToBigError:
        print('angka yang dimasukkan terlalu besar')

print('kamu memasukkan angka yang tepat')
