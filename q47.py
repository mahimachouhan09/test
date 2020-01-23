
list1=[1,2,3,4,5,6,7,8,9,10]
sqaure_even=map(lambda n : n**2,filter(lambda n : n%2==0 ,list1))
print(list(sqaure_even))

