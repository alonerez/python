import random
def short_list(mylist):
	# list = []
	list = [mylist[0], mylist[-1]]
	return list

a=[]

# create the list

leng = random.sample(range(1, 15), 1)
for i in range(leng[0]):
	a.append(random.randint(1, 30))
	
print(a)
print(short_list(a))
