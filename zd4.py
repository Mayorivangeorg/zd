import random
k = random.randint(1,365)
print(k)

d=5

for i in range(1,365):
	d+=1
	if d>7: d=1

	if i==k:
		print(d)
		break