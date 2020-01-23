def print_even():
	n=int(input("Enter n:"))
	for i in range(0,n):
		if i%2==0:
			yield i
		 	
for i in print_even():
	print(i,end=",")
