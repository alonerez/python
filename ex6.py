string = input("enter a sting ")

# rev = string.reverse()
leng = len(string)
print ("leng: " + str(leng))


for i in range(len(string)):
	print ("i = " + str(i) + ", string[i]" + string[i])
	print ("leng -i -1 = " + str(leng-i-1) + ", string[leng-i-1]" + string[leng-i-1])
	# print ("rev[i]" + rev[i])
	if string[i] != string[leng-i-1]:
		print ("Not a palindrome !")
		exit()
	
print("palindrome")