class Hewan:
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        self.ID_hewan = id_hewan
        self.nama = nama
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.berat_badan = berat_badan
        self.Pemilik_hewan = pemilik_hewan
        self.jenis = None
        self.Sub_jenis = None
    def tampilkan_info(self):
        print("Informasi hewan")
        print(f"ID Hewan      : {self.ID_hewan}\nNama          : {self.nama}\nUsia          : {self.usia}\nJenis kelamin : {self.jenis_kelamin}\nBerat badan   : {self.berat_badan}\nNama pemilik  : {self.Pemilik_hewan}\nJenis         : {self.jenis}\nSub jenis     : {self.Sub_jenis}")

class Kucing(Hewan):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.jenis = "Kucing"

class KucingPersia(Kucing):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.Sub_jenis = "Kucing Persia"
class KucingKampung(Kucing):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.Sub_jenis = "Kucing Kampung"

class Anjing(Hewan):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.jenis = "Anjing"

class AnjingPenjaga(Anjing):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.Sub_jenis = "Anjing Penjaga"
class AnjingRumahan(Anjing):
    def __init__(self, id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan):
        super().__init__(id_hewan, nama, usia, jenis_kelamin, berat_badan, pemilik_hewan)
        self.Sub_jenis = "Anjing Rumahan"



#H1 = AnjingRumahan("A123","Ragnard",9,"laki laki", 40,"andre")
#H1.tampilkan_info()
