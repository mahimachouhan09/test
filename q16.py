lst=input("Enter list:").split(",")
#for i in range():
#	if list1[i]%2!=0:
output=[int(i)**2 for i in lst if int(i)%2!=0]
print(output)
