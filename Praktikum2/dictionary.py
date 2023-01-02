# membuat dictionary menggunakan {key : value}
# untuk mrngaksesnya menggunakan key
data_diri = {'nama' : 'fina'}

print(data_diri['nama'])

# untuk mengakses valuenya menggunakan function values()
nilai = {'firda' : 89, 'inayah' : 78, 'fawaz' : 99, 'rahmah' : 75}
for i in nilai.values():
    print(i)
    
# mengakses key nya saja
for i in nilai.keys():
    print(i)
    
# mencetak key dan value menggunakan items()
for nama,skor in nilai.items():
    print(nama, ':', skor)
    
