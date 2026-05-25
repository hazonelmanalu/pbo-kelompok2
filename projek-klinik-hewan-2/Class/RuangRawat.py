class RuangRawat:
    def __init__(self, kode_ruangan, hewan_yang_menempati):
        self.kode_ruangan = kode_ruangan  
        self.hewan_yang_menempati = hewan_yang_menempati  

    def tampilkan_info(self):  
        print(f"Ruang: {self.kode_ruangan} | Hewan yang Menempati: {self.hewan_yang_menempati.nama}")
