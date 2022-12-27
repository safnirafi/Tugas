# menentukan apakah bangun datar adalah sebuah segitiga sama sisi
print("masukan setiap sisi")

sisi1 = int(input("sisi1: "))
sisi2 = int(input("sisi2: "))
sisi3 = int(input("sisi3: "))

if (sisi1 == sisi2 == sisi3):
    print("ini adalah segitiga sama sisi")
else :
    print("ini bukan segitiga sama sisi")