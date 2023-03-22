#list
list1 = ["samsung", "realme", "oppo",]
list2 = [1, 4, 5, 8, 8, 9]
list3 = [True, False, True,]
list4 = ["abc", 10, True, 40, "Hyundai"]
list5 = [list1, list2, list3, list4]
print(list1 + list2) #kedua list akan digabung dan menjadi satu di dalam kurung siku
print(list2 + list2) #tetap menggabungkan dan tak akan dijumlahkan

#list sort
list2.sort() #mengurutkan dari angka terkecil
print(list2)

list1.sort() #mengurutkan berdasarkan abjad 
print(list1)

list2.reverse() #membalikkan isi dari list
print(list2)

list6 = list1.copy() #akan mengcopy isi dari list 1 (bisa string atau int)
print(list6)

print(list2.count(8)) #menghitung ada berapa banyak angka 8 di dalam list2

#mengakses list
carlist = ["lexus", "vw", "ferrari", "volvo", "mclaren", "porsche", "bmw", "koenigsegg"]
print(carlist[2]) #mengakses isi carlist pada index ke 2
print(carlist[0:4]) #mengakses isi carlist mulai dari index 0 hingga index 3 (4 tidak disertakan)
print(carlist[-2]) #mengakses isi carlist pada index dua terakhir
print(carlist[-4:4]) #mengakses isi carlist mulai dari index 4 terakhir hingga index ke 3 (4 tidak disertakan)
print(carlist[-3:]) #mengakses isi carlist mulai dari index 3 terakhir hingga index paling akhir


#mengganti list
carlist = ["lexus", "vw", "ferrari", "volvo", "mclaren", "porsche", "bmw", "koenigsegg"]
carlist[3] = "lamborghini" #mengganti isi index ke 3 menjadi lamborghini
print(carlist)

carlist.append("hyundai") #menambahkan element hyundai pada carlist (terletak di bagian akhir)
print(carlist)

carlist.insert(2, "dfsk") #menambahkan element dfsk pada carlist, akan diletakkan pada index ke 2
print(carlist)

clothlist1 = ["roughneck", "erigo", "thankinsomnia"]
clothlist2 = ["kremlin", "kizaru", "clowor"]
clothlist1.extend(clothlist2) #mengextend clothlist1 dengan clothlist2
print(clothlist1)

#membership test
#apakah ada elemen tertentu pada sebuah list
print("vw" in carlist) #mengecek apakah ada element vw pada carlist ( out: true or false)
print("ferrari" not in carlist) #mengecek apakah tidak ada element ferrari di carlist


#menghapus element
carlist = ["lexus", "vw", "ferrari", "volvo", "mclaren", "porsche", "bmw", "koenigsegg"]
carlist.remove("koenigsegg") #menghapus element koenigsegg pada carlist
print(carlist)

carlist.pop(3) #menghapus element pada index ke 3 pada carlist
print(carlist)

del carlist[2] #menghapus element pada index ke 2
print(carlist)

# del carlist #menghapus seluruh isi dari carlist dan list akan menghilang

carlist.clear() #menghapus seluruh isi dari carlist tetapi tidak sampe list nya menghilang
print(carlist)

#tuple
#sama seperti list, tetapi tuple tidak inputable (isinya tidak bisa diganti)
tuple1 = ("kawasaki", "suzuki", "ducati", "MVagusta")
tuple2 = (1,5,7,3,9,3,5)
tuple3 = (True, False, True, False, False)
tuple4 = ("bmw", 4,5, True, "Monster", False)
print(tuple1[3])
print(tuple1[0:2])
print(tuple2[2:5])
print(tuple2[-4:])

#dictionary
car_dict = {'merk'  : 'nissan',
            'type'  : 'gtr-r34',
            'plat'  : 1234,
            'harga' : 50000000000, }

print(car_dict)
print(car_dict['type']) #mengakses dictionary car_dict untuk melihat value dari key type
car_dict['type'] = 'gtr-r35' #mengganti value di type menjadi gtr-r35
print(car_dict)

#looping key dan value di car_dict
for key, value in car_dict.items():
    print(key, value)

#looping key di car_dict
for key in car_dict.keys():
    print(key)

#looping value di car_dict
for value in car_dict.values():
    print(value)

#dapat menampung lebih dari 1 dictionary di dalam list
car_pro = [
            {
                'merk'  : 'nissan',
                'type'  : 'gtr-r34',
                'plat'  : 1234,
                'harga' : 50000000000, },
            
            {
                'merk'  : 'bmw',
                'type'  : 'GS1200',
                'plat'  : 1200,
                'harga' : 2000000000,
            }
        ]

print(car_pro)

#set atau himpunan dalam matematika
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#union
print(A | B)

#Intercestion
print(A & B)

#difference
print(A - B)
print(B - A)

#Symetric Difference
print(A ^ B)