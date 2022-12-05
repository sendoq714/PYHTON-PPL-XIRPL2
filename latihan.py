#belajar pewarisan (inheritance)
#3 Objek = orang, pelajar, pekerja
#masing2 mempunyai nama, asal, kemampuan untuk introduce ur self
#pelajar di sekolah, pekerja di kantor

class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("Perkenalan nama saya", self.nama, "dari", self.asal)

class Pelajar(Orang):
    #Sekolahny dimana 
     def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class pekerja(Orang):
    #kerjanya dimana
    def __init__(self, nama, asal, kerja):
        Orang.__init__(self, nama, asal)
        self.kerja = kerja

dani = Orang('Dani', 'Jakarta\n')
dani.perkenalan()

rahma = Pelajar('rahma', 'jawa', 'SMK JP 1')
rahma.perkenalan()
print("Saya bersekolah di", rahma.sekolah, "\n")

arya = pekerja('arya', 'bandung', 'SMK JP 1')
arya.perkenalan()
print("Saya Bekerja di", arya.kerja, "\n")