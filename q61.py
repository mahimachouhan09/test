x=input("Enter String:")
output=""
for i in x:
	if x.index(i)%2==0:
		output=output+str(i)
print(output)
