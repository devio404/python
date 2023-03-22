import re
#mengimport package regex

teks = 'regex'
#untuk mengembalikan status kecocokan dari variable teks
x = re.match('^r...x$', teks)
print(x)

teks = 'saya pintar belajar regex'
#mensplit kalimat menjadi per kata
y = re.split('\s', teks) #\s adalah string memuat spasi
print(y)

teks = '''
        Haikyuu merupakan serial anime dari jepang
        awal perilisannya pada tahun 2014.
        '''
#mengubah bagian dari string berdasarkan kecocokan
x = re.sub('\d+', "X", teks) #\d string memuat 0-9 digit dan + (1 atau lebih keberadaan)
print(x)

text = 'Hujan deras di kawasan miyagi'
result = re.search("^Hujan.*miyagi$", text)
if result:
    print('yes match')
else: 
    print('no match')

tekss = "23 maret 2023 23 maret, 2023 23 mar, 2023 maret 23, 2023"
x = re.findall("\d{2} [a-z]{3} \d{4}", tekss)
print(x)

teks = 'harga 1 pisang itu $1'
x = re.sub("\$\d+", "----", teks)
print(x)

teks = 'akan beralih ke https://google.com'
x = re.sub("http[s]?\://\S+", "_", teks)
print(x)

teks = 'banyak anak muda tahun 2025 antusias belajar coding #pintar #_oke #rpl'
x = re.findall("#[_]*[a-z]+", teks)
print(x)