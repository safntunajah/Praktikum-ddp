
nama_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

total = len(nama_buah)

for i in range(int(total/2)):
    nama = nama_buah[i]
    nama_buah[i] = nama_buah[total -i-1]
    nama_buah[total-i-1] = nama

print(nama_buah)