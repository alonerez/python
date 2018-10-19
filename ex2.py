num = int(input("Please neter a number: "))
print("Your number is " + str(num))

if num%4  == 0 :
	print ("4")
elif num%2 == 1 :
	print ("odd")
else:
	print ("even")