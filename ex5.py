import random
from collections import OrderedDict

a=[]
b=[]
# create the lists

len = random.sample(range(1, 15), 2)

for i in range(len[0]):
	a.append(random.randint(1, 30))
	
# len = random.randint(1, 15)
for i in range(len[1]):
	b.append(random.randint(1, 30))
	
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonlist = []
  
for x in a :
	if x in b :
		commonlist.append(x)
		
		
print("a:" + ' '.join(map(str, a)))
print("b:" + ' '.join(map(str, b)))

# sorted = commonlist.sort()
# print (sorted)
print("commonlist :" + ' '.join(map(str, commonlist)))
commonlist.sort()
print("commonlist sorted:" + ' '.join(map(str, commonlist)))
nodup = list(dict.fromkeys(commonlist))
print("nodup:" + ' '.join(map(str, nodup)))