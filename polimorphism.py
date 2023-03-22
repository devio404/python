class Cat:
    def __init__(self):
        self.nama = "meong"
        self.tipe = "British"

    def forward(self):
        print("Kucing ini berlari....")

class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"

    def forward(self):
        print("Burung Terbang....")

def melaju(objek):
    objek.forward()

neko = Cat()
er = Bird()

melaju(neko)
melaju(er)