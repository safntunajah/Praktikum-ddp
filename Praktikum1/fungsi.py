def Hello():
    print("Hello World")

Hello()

def data_diri(nama, rombel, nim):
    print("Nama", nama)
    print("Rombel", rombel)
    print("Nim", nim)
    
data_diri("safinatunnajah", "TI13", "0110222234")

def berangkat_kuliah(cuaca):
    if cuaca == "hujan":
        print("Naik Gocar")
    elif cuaca == "adem":
        print("Naik motor")
    else :
        print("Jalan kaki")
        
berangkat_kuliah("hujan")