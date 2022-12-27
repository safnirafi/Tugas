print("\n[+] Menentukan Integer")

x = int(input("Masukkan Integer Ke-1: "))
y = int(input("Masukkan Integer Ke-2: "))
if x > y:
    selisih = x - y
else:
    selisih = y - x
print(" |")
if (x == 5) or (y == 5) or (x + y == 5) or selisih == 5:
    print("Benar")
else:
    print("Salah")