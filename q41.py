def printtuple():
	l1=list()
	for i in range(0,21):
		l1.append(i*i)
	print(l1)
	print("list print : ",type(l1))
	t1=tuple(l1)
	print("tuple : ")
	print(t1)
printtuple()