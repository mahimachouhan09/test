#for i in range(1000,3000):
	#d=i%10  	   #last digit
	#c=(i/10)%10    #second last digit
	#b=(i/100)%10   #third digit 
	#a=(i/1000)%10  #first digit
	#if d/2==0:
		#if c/2==0:
	#if b%2==0:
	#	if a%2==0:
	#		print(i)

	#else:
	#	 continue
#f=0
for i in range(1000,3000):
	f=0
	s=str(i)
	for x in s:
#import pdb;pdb.set_trace()
		if int(x)%2!=0:
			f=1
			break
	if f==0:
		print(s,end=",")
		
