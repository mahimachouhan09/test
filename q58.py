list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]

#  if list[i+1]!=list[i]:
#    list2.append(list)
print("without rep:")
for i in list1:
	if i not in list2:
		list2.append(i)
print(list2)
print("Reverse without repetion:")
list2.reverse()
print(list2)