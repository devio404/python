#cara 1
var1 = "pubg"
var2 = 1000
var3 = "platinum 5"

print(var1)
print(var2)
print(var3)

#cara 2
var1, var2, var3 = "pubg", 1000, "platinum v"
print(var1, var2, var3)
#atau
print(var1)
print(var2)
print(var3)

#persamaan variable (variable sama)
var1 = var2 = 5000
print(var1)
print(var2)

#naming variable
#dilarang !, @, #, $, % digit 0-9 di awal
nama_variable = "Var 1"
NAMA_VARIABLE = "VAR 1"
namaVariable = "Var1"
NamaVariable = "VAr 1"

#float & int
a = 5
b = 0.5
c = 4/5
d = a + b
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("batas")

#memaksa merubah tipe data awal
x = 7 #int
x = float(x) #int akan dirubah menjadi float
y = 4.7 #float
y = int(y) #float akan dirubah menjadi int
z = 9 #int
  #int akan dirubah menjadi string
print(type(x))
print(type(y))
print(type(z)) 

#pembulatan
q = 9/5
print(q)
#dibulatkan ke atas
q = q.__ceil__()
print(q)

p = 6/4
print(p)
#dibulatkan ke bawah
p = p.__floor__()
print(p)

#string
s1 = "ini adalah string single-line"
s2 = '''ini adalah
string multi-line tanpa enter'''
s3 =  '''
ini adalah
string multi-line dengan enter
'''
print(s1)
print(s2)
print(s3)

#upper & lower case
kecil = "DITULIS DENGAN HURUF KAPITAL"
kecil = kecil.lower()
print(kecil)

besar = "ditulis dengan huruf kecil"
besar = besar.upper()
print(besar)

kalimat1 = "before ini adalah kalimat "
print(kalimat1)
#merubah/mereplace kalimat before menjadi after
kalimat1 = kalimat1.replace("before", "after")
print(kalimat1)

#mencetak suatu variable
#cara ke 1
namaNabi = "Muhammad"
m = f"Nabi saya adalah Nabi {namaNabi}"
print(m)

#cara ke 2
namaKitab = "Al-quran"
k = "Kitab saya adalah {}".format(namaKitab)
print(k)

#boolean (true/false)
bool = True
print(type(bool)) 

#boolean logika pemrograman
print(False or True) #or bisa diganti dengan simbol |
print(False and True) #and bisa diganti dengan simbol &

#list, tuple, dictionary
list = [10, "ular", 2.2]
print(type(list))

tuple = (6, 5 + 1, "enam")
print(type(tuple))

dictionary = {'key':1, 'value':2}
print(type(dictionary))