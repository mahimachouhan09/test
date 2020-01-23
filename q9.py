no_of_lines=int(input("Enter Input line by line:"))
line=""
for i in range(no_of_lines):
	line=input()+"\n"

for i in line:
	line.append(line.upper())
	print(i)	