num = int(input("enter a number "))
divisors=[]

list = range (2,num)
for x in list :
	if num%x == 0 :
		divisors.append(x)
		
		
print (divisors)