fruits = ['apple', 'banana', 'cherry','cherry','cherry','orange','cherry']
F = fruits.copy()
deltasebelumnya = 0
while "cherry" in F:
	x = F.index("cherry")
	print("indeks cherry:",x+deltasebelumnya)
	deltasebelumnya = deltasebelumnya+x+1
	F = F[x+1:]
	print(F)
    
'''
                0          1         2         3        4          5         6
"cherry" in F['apple', 'banana', 'cherry', 'cherry', 'cherry', 'orange', 'cherry'] = true
x = 2
indeks cherry: 2+0 -> indeks cherry: 2
deltasebelumnya = 0+2+1 = 3
F = F[2+1:] = F[3:]
['cherry', 'cherry', 'orange', 'cherry']

                  0         1         2         3
"cherry" in F['cherry', 'cherry', 'orange', 'cherry'] = true
x = 0
indeks cherry: 0+3 -> indeks cherry: 3
delta sebelumnya = 3+0+1 = 4
F = F[0+1:] = F[1:]
['cherry', 'orange, 'cherry']

                  0         1         2     
"cherry" in F['cherry', 'orange', 'cherry'] = true
x = 0
indeks cherry: 0+4 -> indeks cherry: 4
deltasebelumnya = 4+0+1 = 5
F = [0+1:] = F[1:]
['orange', 'cherry']

                  0         1
"cherry" in F['orange', 'cherry'] = true
x = 1
indeks cherry: 1+5 -> indeks cherry: 6
deltasebelumnya = 5+1+1 = 7
F = [1+1:] = F[2:]
[]

"cherry" in F[] = false
while loop end
'''