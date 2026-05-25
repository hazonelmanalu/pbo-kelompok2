class BiayaLayanan:
    def __init__(self, code, IDhewan, IDtenagalayanan, perawatan):
        self.code = code
        self.IDhewan = IDhewan
        self.IDtenagalayanan = IDtenagalayanan
        self.perawatan = perawatan

    def hitungbiayatenagalayanan(self):
        if self.IDtenagalayanan == "A":
            return 100000
        elif self.IDtenagalayanan == "B":
            return 200000
        elif self.IDtenagalayanan == "C":
            return 300000
        else:
            return 0
    
    def hitungbiayaperawatan(self):
        if self.perawatan == "A":
            return 100000
        elif self.perawatan == "B":
            return 200000
        elif self.perawatan == "C":
            return 300000
        else:
            return 0
    
    def hitungtotal(self):
        return self.hitungbiayatenagalayanan() + self.hitungbiayaperawatan()

# Contoh penggunaan / instansiasi

layanan1 = BiayaLayanan(
    code="BL001",
    IDhewan="H001",
    IDtenagalayanan="A",
    perawatan="B"
)

print("Kode Layanan:", layanan1.code)
print("ID Hewan:", layanan1.IDhewan)
print("Biaya Tenaga Layanan:", layanan1.hitungbiayatenagalayanan())
print("Biaya Perawatan:", layanan1.hitungbiayaperawatan())
print("Total Biaya:", layanan1.hitungtotal())
