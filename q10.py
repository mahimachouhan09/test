s=str(input("Enter the string:"))
wordcount=0
#for i in s:
#	if s[i]!=" ":
#		for j in s:
#				wordcount+=1
#		else:
#			i=i+1

string2=""
if len(s)>0:
	wordcount=s.split(" ")
	wordcount=sorted(wordcount)
	for i in wordcount:
		if string2.count(i)==0:
			string2+=i
			string2+=" "
	print("outpur string:{0}".format(string2))