import math
x,y=0,0


while True:
	steps_taken=input("steps taken :" ).split(" ")
	

	if steps_taken[0]=="Up":
		y=y+int(steps_taken[1])

	elif steps_taken[0]=="Down":

		y=y-int(steps_taken[1])
	elif steps_taken[0]=="Right":

		x=x+int(steps_taken[1])

	elif steps_taken[0]=="Left":
		x=x-int(steps_taken[1])

	else:
		break

print("Result:")
print(round(math.sqrt(x**2+y**2)))