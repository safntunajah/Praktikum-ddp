# mendeklarasi tuple dengan()
# mengaksesnya dengan index

gorengan = ('bakwan', 'combro', 'misro')   # index 0
sop = ('sop iga', 'sop buntut', 'sop kaki')     # index 1
nasi = ('nasi uduk', 'nasi goreng', 'nasi rames')       # index 2

# tuple didalam tuple
makanan = (gorengan, sop, nasi)

# cetak gorengannya aja
# print(makanan[0])
# for i in makanan[0] :
#     print(i)
    
# cetak sop buntut
# print(makanan[1])
# for sop in makanan[1][1] :
#     print(sop)

# # cetal nasi rames
# print(makanan[2])
# for rames in makanan[2][2] :
#     print(rames)
    
# cetak sop buntut dan nasi rames cara mudah
print(makanan[1][1])
print(makanan[2][2])

# cetak semuanya dan keluarkan dari buka tutup kurungnya
for i in makanan :
    for detail in i :
        print(detail)