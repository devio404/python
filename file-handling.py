#Read
data = open('./data.txt', mode = 'r')
print(data.read()) #menampilkan semua isi di variable data di file data.txt
# print(data.read(10)) #menampilkan 5 karakter di variable dat di file data.txt

data = open('./data.txt', mode = 'r', encoding='utf-8') #encoding (direkomendasikan)

string = data.read()
print(string)
string = string.replace('ini', 'berikut') #mengganti elemen ini menjadi berikut di file data.txt
print(string)

#Append
data = open('./data.txt', mode='a', encoding='utf-8')
# data.write('\n yuk belajar') #menambahkan kata yuk belajar di file data.txt
# data.write('\n yuk belajar lebih giat') #menambahkan kata yuk belajar di file data.txt
 
#Write
data = open('./data.txt', mode='w', encoding='utf-8')
data.write('\n belajar python itu mudah') #merewrite/menulis ulang/mereplace isi file data.txt dengan kata berikut
data.write('\n bisa programming atau data science')#merewrite/menulis ulang/mereplace isi file data.txt dengan kata berikut
data.close()

#Better Practice
try:
    f = open('./data.txt', mode='w', encoding='utf-8')
finally:
    f.close()

#Best Practice
with open('./data.txt', mode='w', encoding='utf-8') as f:
    #bisa diisi kodingan apa saja
    pass