def divbyseven():
	n=int(input("Enter number upto :"))
	for i in range(0,n):
		if i%5==0 and i%7==0:
			yield i

for i in divbyseven():
	print(i,end=",")