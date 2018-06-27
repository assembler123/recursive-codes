def decPrint(n):
	if n==1:
		print(1)
		return
	print(n)
	decPrint(n-1)
decPrint(10) #n = 10 
