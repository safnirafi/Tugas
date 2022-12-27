print('-'*8)
n = int(input("Masukkan angka integer : "))
print("="*8)

print("==== While ====")
m = 1
while m <= n:    
     if m%2 == 0: 
          print(m, end = " ")
     m += 1  

print("\n===== For =====")
for i in range(1,n+1):
     if i %2 == 0 :
          print(i, end = " ")