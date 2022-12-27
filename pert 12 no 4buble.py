'''
Bubble Sort

idx     0   1   2   3   4   5   6   7   8
val     17  83  37  6   10  82  5   11  1


val     17  37  6  10   82    5   11   1    83*  I
val     17  6  10  37    5   11   1    82*  83*  II
val     6  10  17   5   11    1   37*  82*  83*  III
val     6  10  5   11    1   17*  37*  82*  83*  IV
val     6  5   10   1   11*  17*  37*  82*  83*  V
val     5  6   1   10*  11*  17*  37*  82*  83*  VI
val     5  1   6*  10*  11*  17*  37*  82*  83*  VII
val     1  5*  6*  10*  11*  17*  37*  82*  83*  VIII

'''

def bubblesort(D):
    print("------------------------------------------------------------------")
    n = len(D)
    print("BUBBLE SORT >>> input:",D,", jumlah data:",n)
    print("------------------------------------------------------------------")
    for i in range(n-1):
        print("Putaran",i+1,"| id titik banding:",0,"-",(n-1)-1-i,"| area terlibat",D[:n-i])
        #kondisi benar adalah kecil di kiri, besar di kanan
        for j in range(n-i-1):
            if D[j] > D[j+1]:
                D[j],D[j+1] = D[j+1],D[j]
        print("hasil:",D)


A = [17,  83,  37,  6,   10,  82,  5,   11,  1]
bubblesort(A)

'''
output
------------------------------------------------------------------
BUBBLE SORT >>> input: [17, 83, 37, 6, 10, 82, 5, 11, 1] , jumlah data: 9
------------------------------------------------------------------
Putaran 1 | id titik banding: 0 - 7 | area terlibat [17, 83, 37, 6, 10, 82, 5, 11, 1]
hasil: [17, 37, 6, 10, 82, 5, 11, 1, 83]
Putaran 2 | id titik banding: 0 - 6 | area terlibat [17, 37, 6, 10, 82, 5, 11, 1]
hasil: [17, 6, 10, 37, 5, 11, 1, 82, 83]
Putaran 3 | id titik banding: 0 - 5 | area terlibat [17, 6, 10, 37, 5, 11, 1]
hasil: [6, 10, 17, 5, 11, 1, 37, 82, 83]
Putaran 4 | id titik banding: 0 - 4 | area terlibat [6, 10, 17, 5, 11, 1]
hasil: [6, 10, 5, 11, 1, 17, 37, 82, 83]
Putaran 5 | id titik banding: 0 - 3 | area terlibat [6, 10, 5, 11, 1]
hasil: [6, 5, 10, 1, 11, 17, 37, 82, 83]
Putaran 6 | id titik banding: 0 - 2 | area terlibat [6, 5, 10, 1]
hasil: [5, 6, 1, 10, 11, 17, 37, 82, 83]
Putaran 7 | id titik banding: 0 - 1 | area terlibat [5, 6, 1]
hasil: [5, 1, 6, 10, 11, 17, 37, 82, 83]
Putaran 8 | id titik banding: 0 - 0 | area terlibat [5, 1]
hasil: [1, 5, 6, 10, 11, 17, 37, 82, 83]
'''