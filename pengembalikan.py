def kalimat(string):
    return "{} {} {}".format(string, string, string) #fungsi format string untuk menampilkan 3 salinan kalimat

if __name__== "__main__":
    while True: #looping 
        txt = str(input("Masukkan Kalimat: ")) #input data pada string
        if txt == "": #jika teks yang diinput = ""
            break #berhenti
        ret = kalimat(txt) #memanggil fungsi kalimat
        print(ret) #mencetak fungsi