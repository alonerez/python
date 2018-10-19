def get_user_input(q="Please enter a number: "):
	return int(input(q))
	

def sum_two_numbers(x,y):
	return x+y
	

	
cnt = get_user_input()

a=0
b=1


while cnt > 0:
	# print ("cnt = " + str(cnt))
	cnt -=1 
	c = b
	b = sum_two_numbers(a,b)
	a = c
	print(str(a) +", ")
 
# print (str(sum_two_numbers(a,b)) + ", ")	