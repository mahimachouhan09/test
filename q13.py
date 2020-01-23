s=str(input("Enter String as input:"))
lettercount=0
digitcount=0
for i in s:
	if i.isalpha():
		lettercount+=1
	if i.isdigit():
		digitcount+=1
print("lettercount:{0}".format(lettercount))
print("digitcount:{0}".format(digitcount))