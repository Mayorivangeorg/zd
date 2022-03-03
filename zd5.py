dat = int(input("Введите год: "))

if dat>100:
	dat=dat // 100
elif dat>0 and dat<101:
	dat=0

print("Это",dat+1,"век")