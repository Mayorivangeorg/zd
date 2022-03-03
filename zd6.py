import random

x=3
y=5
z=11
max=0
min=0

if (x%2==0) or (y%2==0) or (z%2==0):
	if (x>y) and (x>z): max=x
	elif (z>y) and (z>x): max=z
	elif (y>x) and (y>z): max=y
	print("Максимальное число: ",max)
else:
	if (x<y) and (x<z): min=x
	elif (z<y) and (z<x): min=z
	elif (y<x) and (y<z): min=y
	print("Минимальное число: ",min)