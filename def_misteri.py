def misteri (n):
    if (n == 1):
        return 1
    else :
            return misteri(n - 1) + n
print(misteri(5))

'''
misteri (5)  n=5 #n!=1
	return misteri (4)+5
	return misteri (3)+4+5
	return misteri (2)+3+4+5
	return misteri (1)+2+3+4+5
	return 1+2+3+4+5
	return 15
	
'''