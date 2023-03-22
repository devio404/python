#function non parameter
#membuat perintah blok kode ke dalam function
def helllo_world():
    var = 'halo masbro !'
    print(var)
#pemanggilan function
helllo_world()

#function parameter
#kurang lebih sama, 
#tetapi disini kita harus memasukkan inputan saat memanggil function
def pagi(nama):
    var1 = f'Pagi {nama}, selamat datang !'
    print(var1)

pagi('masbro')

def data_diri(nama, umur, pekerjaan):
    var2 = f'Perkenalkan nama saya {nama}, umur saya {umur}, sekarang saya bekerja sebagai {pekerjaan}'
    print(var2)
data_diri('Nviel', '78', 'Pro player pubg') #cara memanggil 1
data_diri(nama='MasPitul', umur='98', pekerjaan='rusher pro') #cara 2

#menambah parameter di pemanggilan function dengan jumlah tidak menentu
def welcome_nama(*daftar_nama):

    var = "Haloo " #menambahkan string di awal
    for name in daftar_nama:
        var += name + ', ' #menambahkan koma tiap nama/parameter
    
    var += 'welcome' #var = var + 'welcome'
    print(var)

welcome_nama('nviel', 'maspitul', 'glaezz', 'cahyaa')

# fungsi anonim
double = lambda x: x * 2
print(double(5)) #mengkalikan bilangan di dalam kurung

#docstring
#komen dapat ditaruh di dalam function, dapat nge print komentar

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    '''
    var = f'Halo {nama}, welcome'
    print(var)

selamat_datang('masbro')
print(selamat_datang.__doc__)

#scope & return
# setelah mengerjakan op1, maka sebelum print akan return untuk mengerjakan op2
def operasi(a, b,c):
    op1 = a + b
    op2 = op1 // c
    return op2 #menambahkan return agar tidak terjadi none

hasil = operasi(a=10, b=5, c=5)
print(hasil)

print('batas suci')

#scope
#yaitu perbedaan peletakan, contohnya dibawah pakai angka 2 
#variable diluar function dapat dikenali dari dalam function,
#tapi tidak berlaku sebaliknya
a = 2
def operasi(a, b,c):
    op1 = a + b
    op2 = op1 // c
    print('scope didalam: ', a) #akan dicari dulu di dalam function, apabila tidak ada makan akan mencari diluar function
    return op2

hasil = operasi(a=10, b=5, c=5)
print(hasil)
print('scope diluar: ', a)