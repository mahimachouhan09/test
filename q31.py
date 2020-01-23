def max_length(s1,s2):
	l1=len(s1)
	l2=len(s2)
	if l1==l2:
		print("Both strings are of same length therfore printing line by line.............")
		print("{0}".format(s1)),
		print("{0}".format(s2)),
		return 
	elif l1>l2:
		result=s1

	else:
		result=s2
	return result

s1=str(input("Enter string 1"))
s2=str(input("Enter string 2"))
print(max_length(s1,s2))

