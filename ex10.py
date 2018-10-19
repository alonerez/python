import random

a=[]
b=[]
# create the lists

len = random.sample(range(1, 15), 2)

for i in range(len[0]):
	a.append(random.randint(1, 30))
	
# len = random.randint(1, 15)
for i in range(len[1]):
	b.append(random.randint(1, 30))
	
	
nodup = [ x for x in a for y in b if x==y]  	
	
print(a)	
print(b)
print(nodup)