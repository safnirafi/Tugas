def hrf_kecil(string):
    return string.lower() #mengubah default 'string' menjadi huruf kecil semua
def hrf_besar(string):
    return string.upper() #mengubah default 'string' menjadi huruf besar semua
def hapus_a(string):
    return string.replace("a", "").replace("A", "") #mengubah default 'string' menghapus huruf a dan A

if __name__ == "__main__":
    str = "Belajar Python di Mata Kuliah Algoritma Pemograman"
    kecil = hrf_kecil(str)
    besar = hrf_besar(str)
    hapus = hapus_a(str)

    print(f"Huruf Kecil = {kecil}")
    print(f"Huruf Besar = {besar}")
    print(f"Menghapus huruf a dan A = {hapus}")