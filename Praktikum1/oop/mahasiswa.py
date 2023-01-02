class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""
    
    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
    
    def welcome(self):
        print("hallo", self.nama, "Di STT Terpadu Nurul Fikri")
        
    def lulus(self, nilai):
     if(nilai > 90):
        return("lulus")
     else:
        return("tidak lulus")
        
mhs1 = Mahasiswa("0110222234", "Fina", "TI13")
# mhs1.nama = "Fina"
# mhs1.nim = "0110222234"
# mhs1.rombel = "TI13"

print("Nama mahasiswa :", mhs1.nama)
print("nim :", mhs1.nim)
print("rombel :", mhs1.rombel)
print("lulus :", mhs1.lulus)