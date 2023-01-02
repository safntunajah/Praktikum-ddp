# list makanan dengan dua dimensi
list_makanan = [
    ['bakwan', 'tempe', 'tahu'],
    ['nasi uduk', 'nasi pecel', 'sate padang']
]

# # print nasi pecel
# print(list_makanan[1][1])

# # print tahu
# print(list_makanan[0][2])

# print semua data
# for makanan in list_makanan :
#     # aksi untuk for pertama
#     for detail_makanan in makanan :
#         # aksi untuk for kedua
#         print(detail_makanan)

# print semua data menggunakan cara lain        
for index0 in list_makanan[0]:
    print(index0)
    
for index1 in list_makanan[1]:
    print(index1)