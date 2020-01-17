list=[12,24,35,24,88,120,155,88,120,155]
list2=[]
list3=[]
for i in list:
  if list[i+1]!=list[i]:
    list2.append(list)

print("without rep:")
print(list2)
print("Reverse without repetion:")
for i in list2:
	list3=list3+i
print(list3)

