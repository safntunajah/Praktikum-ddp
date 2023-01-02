from Mahasiswa import *
from Dosen import *

mhs1 = Mahasiswa("Safinatunnajah", "Perempuan", 20, "Teknik Informatika", 1)
dsn1 = Dosen("Safinatunnajah", "Perempuan", 20, "S.T", "Dosen")

dsn1.setGaji(12000000)
mhs1.cetak()
dsn1.cetak()