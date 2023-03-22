class Animal:
    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = "Lambat"

    def grow(self):
        print("Mamalia ini bertumbuh.....")

#child class
class Cat(Animal):
    def __init__(self, nama, tipe):

        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"Kucing {self.tipe} ini berlari")    
        

class Dog(Animal):
    pass

neko = Cat(nama="neko", tipe="british")
eko = Cat(nama="eko", tipe="kampung")

print(neko.kecepatan)
print(neko.tipe)

neko.run()
neko.grow()