from random import randint
mas=[]
max_num=0
buf=0
max_ind=0

for i in range(1,10):
	mas.append(randint(1,30))

print(mas)
max_num=max(mas)
max_ind=mas.index(max_num)

buf=mas[0]
mas[0]=max_num
mas[max_ind]=buf

print(mas)