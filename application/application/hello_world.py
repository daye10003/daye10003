#-*- coding:utf-8 -*-
k=0
for i in range(2,10):
	for number in range(1,10):
		k=i*number
		print str(i) + "*"+ str(number) + "=" + str(k)

lst=[]
from random import shuffle
x = range(1,46)
shuffle(x)
lst.append(x[0])
lst.append(x[1])
lst.append(x[2])
lst.append(x[3])
lst.append(x[4])
lst.append(x[5])
print lst