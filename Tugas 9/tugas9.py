def linear(x,y,z):
    return x**+7*y-z

print(linear(4,6,7))

    
#cuaca
def kuliah(cuaca):
    if(cuaca=="hujan"):
        print("cuaca sedang hujan maka saya berangkat kuliah naik gocar")
    elif(cuaca=="adem"):
        print("cuaca sedang adem maka saya berangkat kuliah naik motor")
    else:
        print("hari ini sedang libur kuliah")

kuliah("adem")


#biodata


def _biodata(nama,alamat,tgl,umur,tb):
    bbi=tb-110
    print("nama saya adalah ", nama)
    print("alamat saya adalah ", alamat)
    print("tgl saya adalah ", tgl)
    print("umur saya adalah ", umur)
    print("tinggi badan saya" , tb)
    print("berat badan ideal saya", bbi)

_biodata("safinatunnajah","jakarta","13 agustus 2002","19",155)
