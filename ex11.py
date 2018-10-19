

def check_divisors(my_num):
	divisors=[]
	list = range (2,my_num)
	for x in list :
		if my_num%x == 0 :
			divisors.append(x)
	return divisors	
	
num = int(input("enter a number "))

res = check_divisors(num)
if not res: 
	print ("Primal")
else:
	print (res)
		
# print (divisors)