jumlah = int(input("Masukkan jumlah angka yang ingin kamu jadikan input: "))
i=0
hasilKali = 1
hasilJumlah = 0
arrayAngka = []
while(i<jumlah):
    a = int(input("masukkan angka: "))
    hasilKali = hasilKali*a
    hasilJumlah = hasilJumlah+a
    arrayAngka.append(a)
    i=i+1
ratarata = hasilJumlah/jumlah
arrayAngka.sort()
median = 0
if jumlah%2 == 0:
    median = (arrayAngka[int((jumlah/2)-1)] + arrayAngka[int(jumlah/2)])/2
else:
    median = arrayAngka[int((jumlah/2)-0.5)]
print("Array setelah diurutkan: {}".format(arrayAngka))
print("Nilai rata-rata: {}".format(ratarata))
print("Nilai hasil kali seluruh variabel: {}".format(hasilKali))
print("Nilai tengah: {}".format(median))
    
