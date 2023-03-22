class Car:
    '''
        ini adalag class untuk membuat object kucing
        melalui class ini kita bisa mendefinisikan nama
        dan juga tipe dari mobil yang dibuat
    '''

    jenis = "mobil"

    def __init__(self, merk, tipe):
        self.merk = merk
        self.tipe = tipe

    def run(self, speed):
        print(f"Mobil {self.merk} berlari dengan {speed}...")

    def play(self):
        print(f"Mobil {self.merk} balapan dengan mobil lainnya")

#membuat objek
McKing = Car(merk="McLaren", tipe="Supercar")
McQueen = Car(merk="Maserati", tipe="Supercar")

print(f"Porsche adalah bagian dari {McKing.__class__.jenis}")
print(f"{McQueen.merk} merupakan mobil jenis {McQueen.tipe}")

McKing.run('sedang')
McQueen.play()