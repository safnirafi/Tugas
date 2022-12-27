DATA = [17, 83, 37, 6, 10, 82, 5, 11, 1]  # DEKLARASI VARIABEL DATA/ SAMPLE DATA

def sekuensialSearch(D,x): # DEKLARASI FUNGSI
    print(">>> SEKUENSIAL SEARCH | input:",D,", nilai yang dicari:",x) # PRINT INFO PROGRAM
    n = len(D) # MENGHITUNG PANJANG SAMPLE DATA
    idxnya = -1 # SET NILAI VARIABEL INI KE NILAI DARI INDEX PALING AKHIR SAMPLE DATA
    for i in range(n): # PENGULANGAN SEBANYAK PANJANG VARIABEL DATA
        print("Mengecek data di indeks:",i,"-->",D[i]) # PRINT CEK DI DATA PADA INDEKS BERAPANYA SAMPLE DATA
        if D[i] == x: # JIKA NILAI INDEKS ITU SAMA DENGAN YANG DICARI
            print("Ketemu") # PRINT KETEMU
            idxnya = i # SET NILAI VARIABEL KE ANGKA INDEX YANG DICARI
            break # SELESAIKAN PENGULANGAN
    
    if idxnya == -1: # CEK JIKA NILAI IDX TETAP -1
        print(x, "tidak ada pada data" ) # BERARTI TIDAK ADA NILAI YANG DICARI DI SAMPLE DATA
        return None # KEMBALIKAN NONE
    else: # LAINNYA
        print(x, "pada indeks",idxnya ) # DATA KETEMU,PRINT NILAI DATA YANG DITEMUKAN DI SAMPLE DATA DAN DI INDEX BERAPA
        return idxnya # KEMBALIKAN NILAI DARI VARIABEL idxnya

putaran = 0 # DEKLARASI VARIABEL putaran
def binarySearch(D,x,q=0,k=len(DATA)-1): # DEKLARASI FUNGSI
    global putaran # MENGIKUTSERTAKAN VARIABEL PUTARAN
    putaran += 1 # MENAMBAH NILAI VARIBEL PUTARAN DENGAN 1
    print("---BINARY SEARCH---") # PRINT INFO PROGRAM
    print(putaran,". Data area:",q,k,D[q:k+1]) # PRINT INFO PUTRARAN KEBERAPA DAN MENGIKUT SERTAKAN INDEX 
                                               # DAN NILAI BERAPA SAJA
    if q<=k: #range valid karena q di kiri, k di kanan  # JIKA VARIABEL Q LEBIH KECIL SAMA DENGAN K
        t = (q+k)//2 # DEKLARASI NILAI VARIABEL T ADLAH NILAI VAR. Q DITAMBAH NILAI VAR. K DI DIVISION 2
        print("index tengah:",t," nilai/valuenya:",D[t]) # PRINT NILAI TENGAH SAMPLE DATA
        if D[t]==x: # CEK JIKA NILAI TENGAH TERSEBUT SAMA DENGAN NILAI YANG DICARI
            print("Nilai yang dicari ditemukan, ada di posisi pada indeks:",t, "nilai/value yang pada index itu:", D[t])
            # PRINT INFORMASI NILAI YANG DICARI KETEMU  
            return t # MENGEMBALIKAN INDEX NILAI TENGAH SAMPLE DATA
        elif x<D[t]: # CEH JIKA NILAI YANG DICARI LEBIH KECIL ATAU LEBIH BESAR DARI NILAI TENGAH
            return binarySearch(D,x,q,t-1) #fokus di kiri, buang kanan # JIKA NILAI YANG DICARI LEBIH KECIL
        else: # LAINNYA
            return binarySearch(D,x,t+1,k) #fokus di kiri, buang kanan # SEBALIKNYA
    else: # LAINNNYA
        print(x,"teu aya dina data") # PRINT DATA YANG DICARI TIDAK ADA
        return None # KEMBALIKAN NONE
        
nilai_yang_dicari = 11 #DEKALARASI NILAI YANG DICARI
binarySearch(DATA,nilai_yang_dicari) # INISIASI SEARCH BINARY
print("\n\n\n") # PEMBERI JARAK
print(sekuensialSearch(DATA,nilai_yang_dicari)) # INISISAI SEARCH SEKUENSIAL