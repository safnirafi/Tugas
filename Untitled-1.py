for i in range (1, 10, 3): #batas awal:1, batas akhir: 10, method: +3
     print(i) #cetak variable i 
     j = 0 #j dimulai dari 0
     while j < 2 * i: #ketika j < 2 * i = true, lakukan perulangan. jika false, tidak dilakukan perulangan
         print (j, end = " ") #cetak j 
         j = j+2 #dilakukan pengulangan dengan penjumlahan +2
     print("")

a, b = input().split() #input angka
a = int (a) #jadikan tipe data integer
b = int (b) #jadikan tipe data integer

if a < b: #jika a < b = true, maka lakukan proses percabangan, jika false maka berhenti
     print (b - a, end = " ")
     print (a - b)

bu = 8 #nilai pada variable bu = 8
mat = ['ba', 'bi', [4.67, 32, 20], bu] #index pada variabel mat [0, 1, 2[0,1,2], 3]

print (mat[2][1]+3, bu - 5) #cetak variable mat pada index 2 & 1 dijumlahkan dengan 3 dan bu dikurang 5

