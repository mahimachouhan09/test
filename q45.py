input_list=[1,2,3,4,5,6,7,8,9,10]

check_even=lambda i : i%2 == 0
filter_list=filter(check_even,input_list)
even_list=list(filter_list)
print(even_list)