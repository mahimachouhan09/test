s=str(input("Input String : "))
uppercount=0
lowercount=0
for i in s:
	if i.isupper():
		uppercount+=1
	if i.islower():
		lowercount=lowercount+1

print("uppercount:{0}".format(uppercount))
print("lowercount:{0}".format(lowercount))