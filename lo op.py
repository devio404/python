count = 0

while (count < 9):
    print("nilai count: ", count)
    count = count+1

print("stop masbro")


#loop yang akan nge print sesuai jumlah angka/huruf yang ada di list_angka
list_angka = [1,2,3,4,5,6,7,8,9]

for x in list_angka:
    print('loading...')
    print(x)

print(range(10))

print(list(range(10))) #membuat list secara otomatis (mulai dari 0)
print(list(range(1,9))) #membuat list secara otomatis (mulai dari 1 hing
list_range = list(range(1,10)) #sama seperti diatas, cuma beda cara
print(list_range)

#cara ke 2
#mencetak angka range mulai dari 1 hingga dibawah 20, dengan kelipatan 2
list_range1 = list(range(1,20,2))
print(list_range1)

#for x dengan range
for x in list(range(1,10)):
    print(x)


#nested loop
i = 8

while ( i < 10):

    j = 2
    print((i/j))
    while (j <= (i/j)):
            print('loop dalam loop')
            j = j + 1
            i = i + 1
    
print('stop masbro!')

#break dan continue
for val in 'string':
    print(val) #akan ngeprint setiap huruf

for val in 'string':
    if val == 'r':
         break
    print(val) #akan stop nge loop jika bertemu dengan huruf r (huruf r di break)

for val in 'string':
    if val == 'r':
         continue
    print(val) #akan tetap nge print semua tetapi huruf r di skip/tidak di print (huruf r di continue)

print('loop abis masbro')

#for else
'''aku akan mencari nama di daftar murid, jika nama yang aku cari adalah nviel,
maka print nama yang aku cari apabila ketemu. jika tidak ketemu maka akan print
tidak ketemu'''
daftar_murid = ['Glaezz', 'MasPitul', 'Nviel']
nama_murid = 'Nviel'
nama_murid1 = 'Andro'

'''akan melakukan looping pada daftar_murid untuk mencari nama_murid, apabila ketemu
maka print. apabila tidak ketemu maka diperintahkan BREAK dan print nama tidak ketemu
agar tidak terus looping/mencari'''

for nama_dicari in daftar_murid:
     if nama_dicari == nama_murid:
          print(nama_dicari) 
          break

else:
     print('nama tidak ketemu masbro')

#contoh nama tidak ketemu
for nama_dicari in daftar_murid:
     if nama_dicari == nama_murid1:
          print(nama_dicari) 
          break

else:
     print('nama tidak ketemu masbro')