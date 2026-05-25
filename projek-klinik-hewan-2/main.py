from Class.BiayaLayanan import BiayaLayanan
from Class.Hewan import Hewan
from Class.Invoice import Invoice
from Class.Pemilik import Pemilik
from Class.Perawatan import Perawatan_Umum
from Class.RuangRawat import RuangRawat
from Class.TenagaLayananan import DokterUmum

H1 = Hewan("H1", "Gary", 2, "jantan", 3, None)
P1 = Pemilik("Andre Puji Saputro", "12345", "K3525020", "pria", H1)
D1 = DokterUmum("D1", "Justin Patrick Lineker", 100000)
R1 = RuangRawat("R1", H1)
Per1 = Perawatan_Umum("PER1", H1, D1, R1, 25000)
B1 = BiayaLayanan("B1", "H1", "D1", "A")
I1 = Invoice("I1", H1, R1, D1, Per1, B1)

I1.tampilkan_info()