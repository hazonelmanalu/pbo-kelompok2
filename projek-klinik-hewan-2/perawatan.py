class Perawatan:
    def __init__(self, kode_perawatan, hewan_rawatan, 
                 penanggung_jawab_hewan, ruang_rawat,
                 biaya_perawatan):
        self.kode_perawatan = kode_perawatan
        self.hewan_rawatan = hewan_rawatan
        self.penanggung_jawab_hewan = penanggung_jawab_hewan
        self.ruang_rawat = ruang_rawat
        self.biaya_perawatan = biaya_perawatan

    def tampilkan_info(self):
        print("-------------------------------------------")
        print("Kode Perawatan = ", self.kode_perawatan)
        print("Hewan Rawatan = ", self.hewan_rawatan)
        print("Penanggung Jawab Hewan = ", self.penanggung_jawab_hewan)
        print("Ruang Rawat = ", self.ruang_rawat)
        print("Biaya Perawatan = ", self.biaya_perawatan)
        print("-------------------------------------------")

class Perawatan_Umum(Perawatan):

    database_perawatan_umum = {
        1 : "Pemeriksaan Rutin",
        2 : "Rawat Inap"
}

    def __init__(self, kode_perawatan, hewan_rawatan, 
                 penanggung_jawab_hewan, ruang_rawat, 
                 biaya_perawatan):
        
        super().__init__(kode_perawatan, hewan_rawatan, 
                         penanggung_jawab_hewan, ruang_rawat, 
                         biaya_perawatan)
        

class Perawatan_Khusus(Perawatan):

    database_perawatan_khusus = {
        1 : "Perawatan Khusus",
        2 : "Grooming"
    }

    def __init__(self, kode_perawatan, hewan_rawatan, 
                 penanggung_jawab_hewan, ruang_rawat, 
                 biaya_perawatan):
        
        super().__init__(kode_perawatan, hewan_rawatan, 
                         penanggung_jawab_hewan, ruang_rawat, 
                         biaya_perawatan)

class Perawatan_Lain(Perawatan):

    def __init__(self, kode_perawatan, hewan_rawatan, 
                 penanggung_jawab_hewan, ruang_rawat,):
        
        super().__init__(kode_perawatan, hewan_rawatan, 
                         penanggung_jawab_hewan, ruang_rawat)
        
        while True:
            try:
                self.input_perawatan_spesifik = str(input("Silahkan masukkan input perawatan"))
                self.biaya_perawatan_spesifik = int(input("Silahkan masukkan harga perawatan \n > Rp."))
            except ValueError:
                print("Harap masukkan 'input perawatan' dalam 'huruf' dan 'harga perawatan' dalam 'angka'!")


