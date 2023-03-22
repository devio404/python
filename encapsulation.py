class Mobil:
    def __init__(self, tipe):

        self.tipe = tipe
        self.speed = "420KM"
        self.__bensin = "Pertamax Racing"
        self.__nomer = 14

    #getter
    def lihatJenisBensin(self):
        print(f"Jenis bensin yaitu:  {self.__bensin} ")
    
    def lihatMinNomer(self):
        print(f"min nomer yaitu: {self.__nomer}")

    #setter
    def aturMaksNomer(self, nomer):
        self.__nomer = nomer

kns = Mobil(tipe="drag")
print(kns.tipe)
kns.lihatJenisBensin()
print(kns.speed)
kns.aturMaksNomer(24)
kns.lihatMinNomer()

