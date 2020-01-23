#import re
specialChar="$@#"
valid_password=[]

password_list=input("Input password::").split(",")
for password in password_list:
	
	smallcount=0
	digitcount=0
	capitalcount=0
	specialcount=0
		
	for password_char in password:
		#reg=((?=.*[a-z])(?=.*d)(?=.*[A-Z])(?=.*[@$%]).{6,12})
		if password_char.isupper():
			capitalcount+=1
			#print(capitalcount)
		elif password_char.islower():
			smallcount+=1
			#print(smallcount)
		elif password_char.isdigit():
			digitcount+=1
			#print(digitcount)
		elif specialChar.find(password_char)!=-1:
			specialcount+=1
			#print(specialcount)

	if smallcount>=1 and capitalcount>=1 and digitcount>=1 and specialcount>=1 and len(password)>6 and len(password)<12:
		valid_password.append(password)
print("valid password:")
print(",".join(valid_password))	