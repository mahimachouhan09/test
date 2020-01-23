amount=0
while True:
	tr_input=input("Tranaction input:").split(" ")

	if tr_input[0]=="D" or tr_input[0]=="d":
		amount=amount+int(tr_input[1])
	elif tr_input[0]=="w" or tr_input[0]=="W":
		amount=amount-int(tr_input[1])
	else :
		print("wrong input!!!")
		break

print("result transaction:")
print(amount) 