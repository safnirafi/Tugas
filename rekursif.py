def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n-1)
print ('====== FAKTORIAL ======')
i = 0
x = int (input("Masukkan Bilangan : "))
while i<=x :
    print (i,'! = ',faktorial(i))
    i+=1

'''
0 ! =  1
1 ! =  1
2 ! =  2
3 ! =  6
4 ! =  24
5 ! =  120
'''