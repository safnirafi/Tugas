def fibo (k)  :
         if k==1 or k==2 :
                 return 1
         else : 
                return fibo (k-1) + fibo (k-2)
print(fibo(1))
print(fibo(2))
print(fibo(3))
print (fibo(6))  

'''
fibo(1) = 1 

fibo(2) = 1

fibo(3) = fibo(2) + fibo(1)
		=   1     +   1     = 2
		
fibo(6) = fibo(5) + fibo(4)
		= fibo(4)+fibo(1)+fibo(1)  + fibo(4) 
		= fibo(3)+fibo(1)+fibo(1)+fibo(1) + fibo(4)
		= fibo(2)+fibo(1)+fibo(1)+fibo(1)+fibo(1) + fibo(4)
		=   1    +   1   +   1   +   1   +   1    + fibo(3)          +fibo(2)       
		=           	  5        				  + fibo(2)+fibo(1)  +fibo(2)
		= 				  5 					  +    1   +  1      +fibo(2)
		= 				  5    					  +      2           +   1		= 8
	
'''