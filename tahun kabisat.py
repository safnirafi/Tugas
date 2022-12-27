print("[+] Program Tahun Kabisat")
tahun = int(input("Masukkan Tahunmu : "))
if tahun % 400 == 0:
    print(f"Tahun {tahun} merupakan Tahun Kabisat")
elif tahun % 100 == 0:
    print(f"Tahun {tahun} bukan merupakan Tahun Kabisat")
elif (tahun % 4 == 0):
    print(f"Tahun {tahun} merupakan Tahun Kabisat")
else:
    print(f"Tahun {tahun} bukan merupakan Tahun Kabisat")