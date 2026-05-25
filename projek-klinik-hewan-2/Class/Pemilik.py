class Pemilik:
    def __init__(self, nama, no_hp, id_pemilik, jenis_kelamin, daftar_hewan):
        self.nama = nama
        self.No_hp = no_hp
        self.ID_pemilik = id_pemilik
        self.Jenis_kelamin = jenis_kelamin
        self.Daftar_hewan = daftar_hewan
    def tampilkan_info(self):
        print("Informasi pemilik")
        print(f"Nama          : {self.nama}\nNomer HP      : {self.No_hp}\nID pemilik    : {self.ID_pemilik}\nJenis kelamin : {self.Jenis_kelamin}\nDaftar hewan  : {self.Daftar_hewan}")


#P1 = Pemilik("Andre", "09339749", "K44", "laki laki", "kucing")
#P1.tampilkan_info()
