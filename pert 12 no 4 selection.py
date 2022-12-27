def selectionsort(D):                               #D = [17,  83,  37,  6,   10,  82,  5,   11,  1]
    n = len(D)                                      #n=9
    print("SELECTION SORT>> input:",D, ", n:",n)    
    for i in range(n-1):                            #i=0,1,2,3,4,5,6,7     
        print(" PUTARAN",i+1,">> idx area",i,"sd",n-1,":",D[i:n]) 
        #mencari minimum
        #ketika i bernilai 0
        idx_min = i                 #idx_min = 0 tebakan awal (sementara) idx_min=0 datanya 9
        for j in range(i+1,n-1+1):  #j = range(1,9) = [1,2,3,4,5,6,7,8] --> datanya=[83, 37, 6, 10, 82, 5, 11, 1]--------------> range(i+1,n-1+1)
            if D[j]< D[idx_min]:    # D[j] = D[8]= 1 APAKAH LEBIH KECIL DARI? D[idx_min] = D[0] = 17 IYAAAA --> idx_min = 8
                idx_min = j
        print("  minimum:",D[idx_min],"[idx:",idx_min,"]")
        #tukar posisi minimum dengan yang terkiri pada area
        D[idx_min],D[i] = D[i],D[idx_min]
        print("  hasil akhir:",D)
        print("--------------------------------------------------------------")

data = [17,  83,  37,  6,   10,  82,  5,   11,  1]
selectionsort(data)