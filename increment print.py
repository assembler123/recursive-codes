def incPrint(n):
	if n==1:
		print(1)
		return
	incPrint(n-1)
	print(n)
incPrint(10) #n = 10 
