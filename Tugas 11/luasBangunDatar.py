import modulBangunDatar as luas

# Luas Persegi
s = int(input("masukkan nilai sisi ="))

print("Luas Persegi =", luas.luas_persegi(s))


# Luas Persegi Panjang
p = int(input("masukkan panjang persegi panjang ="))
l = int(input("masukkan lebar persegi panjang ="))

print("Luas Persegi Panjang =", luas.luas_persegipanjang(p,l))

# Luas Segitiga
a = int(input("masukkan alas segitiga ="))
t = int(input("masukkan tinggi segitiga ="))

print("Luas Segitiga =", luas.luas_segitiga(a,t))

# Luas Lingkaran
r = int(input("masukkan jari-jari lingkaran ="))
phi = 3.14

print("Luas Lingkaran =", luas.luas_lingkaran(phi,r))

# Luas Layang-Layang
d1 = int(input("masukkan diagonal satu layang-layang ="))
d2 = int(input("masukkan diagonal dau layang-layang ="))

print("Luas Layang-Layang =", luas.luas_layanglayang(d1,d2))