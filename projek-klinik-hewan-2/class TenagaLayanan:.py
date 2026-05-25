class TenagaLayanan:
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        self.nomor_pegawai = nomor_pegawai 
        self.nama = nama 
        self.harga_layanan = harga_layanan

    def tampilkan_info(self):  
        print(f"Tenaga Layanan: {self.nama} | ID Pegawai: {self.nomor_pegawai}")

class Dokter(TenagaLayanan): 
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)

class DokterSpesialis(Dokter): 
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)

class DokterUmum(Dokter): 
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)

class Perawat(TenagaLayanan): 
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)

class PerawatInap(Perawat):
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)

class PerawatGrooming(Perawat): 
    def __init__(self, nomor_pegawai, nama, harga_layanan):
        super().__init__(nomor_pegawai, nama, harga_layanan)
