def  mygen():
	n=int(input("Enter till which numbers are to be printed:"))
	for i in range(0,n):
		if i%7==0:
			yield i

for i in mygen():
	print(i,end=",")