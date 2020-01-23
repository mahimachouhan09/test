t1=(1,2,3,4,5,6,7,8,9,10)
t2=list()
for i in t1:
	if i%2 == 0:
		t2.append(i)
t3=tuple(t2)
print(t3)