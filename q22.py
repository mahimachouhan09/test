input_str=str(input("Input:")).split(" ")
d={}
		
for word in input_str:
	d[word]=d.get(word,0)+1

for i in sorted(d):
	print("{}:{}".format(i,d[word]))